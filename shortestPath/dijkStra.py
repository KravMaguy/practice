# my_graph = {
#     'A': [('B', 2), ('D', 8)],
#     'B': [('A', 2), ('D', 5), ('E', 6)],
#     'C': [('E', 9), ('F', 3)],
#     'D': [('A', 8), ('B', 5), ('E', 3), ('F', 2)],
#     'E': [('B', 6), ('D', 3), ('F', 1), ('C', 9)],
#     'F': [('D', 2), ('E', 1), ('C', 3)]
# }

my_graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('A', 3), ('C', 10), ('D', 1)],
    'C': [('A', 2), ('B', 10)],
    'D': [('B', 1)],
}


def shortest_path(graph, start, target):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    mapping = {node: start if node == start else None for node in graph}
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                mapping[node] = current
        unvisited.remove(current)
    distance = distances[target]
    node = target
    paths = [node]
    while node is not start:
        paths = [mapping[node]] + paths
        node = mapping[node]
    print(' -> '.join(paths) + ' dist: '+str(distance))


shortest_path(my_graph, 'A', 'C')
