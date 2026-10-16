def astar(graph, h, start, goal):
    open_list = [(h[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                new_g = g + cost
                open_list.append(
                    (new_g + h[neighbor], new_g,
                     neighbor, path + [neighbor])
                )

    print("Path not found")


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'G': 5},
    'E': {'G': 3},
    'G': {}
}

h = {'A': 7, 'B': 6, 'C': 4, 'D': 4, 'E': 2, 'G': 0}

astar(graph, h, 'A', 'G')
