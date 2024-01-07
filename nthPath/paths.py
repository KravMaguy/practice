from module_graph import my_graph


def return_2nd_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        order_by_wieght = sorted(res, key=lambda x: x[1])
        shortest_route_time = order_by_wieght[0][1]
        second_quickest_group = []
        for path_and_weight in order_by_wieght:
            [_, weight] = path_and_weight
            if weight > shortest_route_time:
                if not second_quickest_group or second_quickest_group[-1][1] == weight:
                    second_quickest_group.append(path_and_weight)
        return second_quickest_group

    return wrapper


@return_2nd_decorator
def all_paths_bfs(graph, start, target):
    que = [(start, [start], 0)]
    paths = []
    while que:
        current, path_part, weight = que.pop(0)
        if current == target:
            paths.append(['->'.join(path_part), weight])

        for neighbor, updated_weight in graph[current]:
            if neighbor not in path_part:
                que.append(
                    (neighbor, path_part + [neighbor], weight + updated_weight))

    return paths


second_fastest = all_paths_bfs(my_graph, 'A', 'C')
print(second_fastest)
