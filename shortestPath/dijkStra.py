from module_graph import my_graph


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
