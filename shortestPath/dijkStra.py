my_graph = {
    'A': [('B', 2), ('D', 8)],
    'B': [('D', 5), ('E', 6)],
    'C': [('E', 9), ('F', 3)],
    'D': [('A', 8), ('B', 5), ('E', 3), ('F', 2)],
    'E': [('B', 6), ('D', 3), ('F', 1), ('C', 9)],
    'F': [('D', 2), ('E', 1), ('C', 3)]
}


def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[start] = 0
        else:
            distances[node] = float('inf')
    print(unvisited)
    print(distances)


shortest_path(my_graph, 'A')
