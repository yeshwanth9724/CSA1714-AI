def tsp(graph, start):
    n = len(graph)
    visited = {start}
    path = [start]
    cost = 0
    current = start

    while len(visited) < n:
        next_city = min(
            (city for city in range(n) if city not in visited),
            key=lambda city: graph[current][city]
        )
        cost += graph[current][next_city]
        path.append(next_city)
        visited.add(next_city)
        current = next_city

    cost += graph[current][start]
    path.append(start)

    print("Path:", " -> ".join(map(str, path)))
    print("Total Cost:", cost)


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(graph, 0)
