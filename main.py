# project 1.
# Dor maudi - 207055138.
# Sapir natanov - 322378068.
# Noa yesharzadeh - 208595157.
# Segev izac - 207938085.
# Yinon alfasi - 208810374.

def make_matrix(size):
    mat = []

    for i in range(mat_size):
        vector = []
        for j in range(mat_size):
            vector.append(float(input("enter a value: ")))
        mat.append(vector)

    return mat

def print_matrix(mat):
    for i in range(mat_size):
        print(mat[i])


def sum_matrix(matA, matB):
    sum_mat = []
    for i in range(mat_size):
        vector = []
        for j in range(mat_size):
            vector.append(matA[i][j] + matB[i][j])
        sum_mat.append(vector)
    return sum_mat

def dot_product(matA, matB):
    dot_mat = []
    for i in range(mat_size):
        vector = []
        for j in range(mat_size):
            vector.append(0)
        dot_mat.append(vector)

    for i in range(mat_size):
        for j in range(mat_size):
            for k in range(mat_size):
                dot_mat[i][j] += matA[i][k] * matB[k][j]
    return dot_mat


if __name__ == '__main__':
    mat_size = int(input("Enter the size of the matrix: "))

    if mat_size <= 1:
        raise ValueError("value is invalid")

    print("Print matrixA: ")
    matA = make_matrix(mat_size)
    print_matrix(matA)
    print('\n')

    print("Print matrixB: ")
    matB = make_matrix(mat_size)
    print_matrix(matB)
    print('\n')

    print("sum of matrixA and matrixB: ")
    mat_sum = sum_matrix(matA, matB)
    print_matrix(mat_sum)
    print('\n')

    print("Dot product of matrixA and matrixB: ")
    cmat = dot_product(matA, matB)
    print_matrix(cmat)
