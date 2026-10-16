def map_coloring(graph, colors):
    result = {}

    def solve(node):
        if node == len(graph):
            return True

        region = list(graph.keys())[node]

        for color in colors:
            if all(result.get(neighbor) != color
                   for neighbor in graph[region]):
                result[region] = color

                if solve(node + 1):
                    return True

                del result[region]

        return False

    if solve(0):
        for region, color in result.items():
            print(region, ":", color)
    else:
        print("No solution")


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
map_coloring(graph, colors)
