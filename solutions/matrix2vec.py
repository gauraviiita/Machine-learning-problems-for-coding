import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float])-> list[int|float]:
    if len(a) == 0 or len(b) == 0 or len(a[0]) != len(b):
        print("Error: matrix and vector dimensions are incompatible for dot product.")

    result = []
    for row in a:
        dot_product = 0
        for i in range(len(b)):
            dot_product = dot_product + row[i]*b[i]
        result.append(dot_product)
    return result
if __name__ == "__main__":
#    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#    b = [1, 0, -1]
#    result = matrix_dot_vector(a, b)
#    print("Dot product is: ")
#    print(result)

    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of cols in the matrix: "))
	
    print(f"Enter the elements of the {rows}x{cols} matrix row by row:")
    a = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Enter element for row{i+1}, column{j + 1}: "))
            row.append(value)
        a.append(row)


    print(f"Enter the {cols}-dimensional vector:")
    b = []
    for i in range(cols):
        value = float(input(f"Enter element {i + 1} of the vector: "))
        b.append(value)

    result = matrix_dot_vector(a, b)
    print("The result of the dot product is: ")
    print(result)
