def packMan(pac_pos, food_pos, dimensionsXY, graph):
    coords = {}
    [x, y] = dimensionsXY
    for i in range(x):
        for j in range(y):
            coords[(i, j)] = graph[i][j]
    print(coords)


pac_pos = [11, 9]
food_pos = [2, 15]
dimensionsXY = [13, 20]
graph = ["%%%%%%%%%%%%%%%%%%%%",
         "%----%--------%----%",
         "%-%%-%-%%--%%-%.%%-%",
         "%-%-----%--%-----%-%",
         "%-%-%%-%%--%%-%%-%-%",
         "%-----------%-%----%",
         "%-%----%%%%%%-%--%-%",
         "%-%----%----%-%--%-%",
         "%-%----%-%%%%-%--%-%",
         "%-%-----------%--%-%",
         "%-%%-%-%%%%%%-%-%%-%",
         "%----%---P----%----%",
         "%%%%%%%%%%%%%%%%%%%%"]

packMan(pac_pos, food_pos, dimensionsXY, graph)
