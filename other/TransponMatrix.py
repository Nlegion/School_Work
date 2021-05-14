def transpose(matrix):
    res = []
    for i in range(len(matrix[0])):
        res.append([j[i] for j in matrix])
    return res
