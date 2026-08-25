import random

# Travel time matrix between locations
# 0 = A, 1 = B, 2 = C, 3 = D, 4 = E
time = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
]

n = len(time)

# ACO parameters
ants = 10
iterations = 50
alpha = 1.0
beta = 2.0
evaporation = 0.5
pheromone_deposit = 100

# Initial pheromone
pheromone = [[1.0 for j in range(n)] for i in range(n)]


def route_time(route):
    total = 0
    for i in range(len(route) - 1):
        total += time[route[i]][route[i + 1]]
    return total


best_route = None
best_time = float('inf')

for iteration in range(iterations):

    routes = []

    for ant in range(ants):

        route = [0]          # Start from location A
        unvisited = list(range(1, n))

        while unvisited:

            current = route[-1]

            probabilities = []

            for city in unvisited:
                pheromone_value = pheromone[current][city] ** alpha
                visibility = (1 / time[current][city]) ** beta
                probabilities.append(pheromone_value * visibility)

            total = sum(probabilities)

            probabilities = [
                p / total for p in probabilities
            ]

            next_city = random.choices(
                unvisited,
                weights=probabilities,
                k=1
            )[0]

            route.append(next_city)
            unvisited.remove(next_city)

        # Return to starting location
        route.append(0)

        duration = route_time(route)
        routes.append((route, duration))

        if duration < best_time:
            best_time = duration
            best_route = route[:]

    # Evaporation
    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - evaporation)

    # Pheromone update
    for route, duration in routes:
        deposit = pheromone_deposit / duration

        for i in range(len(route) - 1):
            a = route[i]
            b = route[i + 1]

            pheromone[a][b] += deposit
            pheromone[b][a] += deposit


# Location names
locations = ['A', 'B', 'C', 'D', 'E']

best_route_names = [
    locations[i] for i in best_route
]

print("Best Ride-Sharing Route:")
print(" -> ".join(best_route_names))

print("Minimum Trip Duration:", best_time, "minutes")
