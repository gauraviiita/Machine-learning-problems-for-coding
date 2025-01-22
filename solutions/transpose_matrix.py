def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    rows = len(a)
    cols = len(a[0])

    transposed = []
    for _ in range(cols):
        transposed.append([0]*rows)

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = a[i][j]
    return transposed

if __name__ == "__main__":
    a = [[1,2,3], [4,5,6], [7,8,9]]
    result = transpose_matrix(a)
    for row in result:
        print(row)
