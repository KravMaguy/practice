def solve(arr):
    hash_dict = {}
    for i in range(len(arr)):
        hash_dict[arr[i][0]] = arr[i][1]
    sorted_arr = sorted(arr, key=lambda x: int(x[0]))
    linked = []
    for i in range(len(sorted_arr)):
        next_val_index = int(
            sorted_arr[i][0]) + 1 if hash_dict.get(str(int(sorted_arr[i][0]) + 1)) else None

        linked.append({
            'char': sorted_arr[i][1],
            'index': sorted_arr[i][0],
            'nextValIndex': next_val_index
        })

    solutions = []
    current_str = ""
    while len(linked) > 0:
        elem = linked.pop(0)
        if not elem['nextValIndex']:
            if len(current_str) > 0:
                solutions.append(current_str)
            current_str = ""
        else:
            if elem['char'] != "*":
                current_str += elem['char']

    return solutions


input_data = [
    ["5632583", "*"],
    ["1", "*"],
    ["4", "*"],
    ["2", "a"],
    ["5632585", "*"],
    ["25", "X"],
    ["3", "@"],
    ["5632584", "w"],
]

result = solve(input_data)
print(result)
