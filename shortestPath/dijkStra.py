my_graph = {
    'A': [('B', 2), ('D', 8)],
    'B': [('D', 5), ('E', 6)],
    'C': [('E', 9), ('F', 3)],
    'D': [('A', 8), ('B', 5), ('E', 3), ('F', 2)],
    'E': [('B', 6), ('D', 3), ('F', 1), ('C', 9)],
    'F': [('D', 2), ('E', 1), ('C', 3)]
}


def shortest_path(graph, start):

    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')
    while unvisited:
        current = min(unvisited, key=distances.get)
        unvisited.remove(current)
        for node, distance in graph[current]:
            # print(node, distance)
            # print(graph[current])
            if distances[current]+distance < distances[node]:
                distances[node] = distances[current]+distance
        print('dist: ', distances)


shortest_path(my_graph, 'A')
