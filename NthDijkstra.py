from module_graph import my_graph


def nth_dikstra(graph, start, target):
    que = [(start, [start], 0)]
    path_weights = {node: [] for node in graph}

    while que:
        current, path_part, weight = que.pop(0)
        if not path_weights[current]:
            print(f'appending {["->".join(path_part), weight]} to {current}')
            path_weights[current].append(['->'.join(path_part), weight])
        else:
            index = 0
            while (path_weights[current][index][1] < weight):
                print(path_weights[current][index], '')
                index += 1
            print(index, ' index')
            # path_weights[current].insert(
            #     ['->'.join(path_part), weight], index)

        for neighbor, updated_weight in graph[current]:
            if neighbor not in path_part:
                que.append(
                    (neighbor, path_part + [neighbor], weight + updated_weight))
    print(path_weights)


nth_dikstra(my_graph, 'A', 'D')
