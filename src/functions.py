import numpy as np

def posisi(x, matrix):
    index = 0
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == x:
                index = (4*i)+j
    return index

def kurang(x, matrix):
    hasil = 0
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] < x and posisi(matrix[i][j], matrix) > posisi(x, matrix)):
                hasil += 1
    return hasil

def cekPosisiKosong(matrix):
    finalPos = 0
    shadedArea = [1, 3, 4, 6, 9, 11, 12, 14]
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 16 and ((4*i+j) in shadedArea)):
                finalPos = 1
    return finalPos

def canBeSolved(matrix):
    kurangi = 0
    for i in range(1, 17):
        kurangi += kurang(i, matrix)
        print("Nilai fungsi Kurang("+str(i)+") = ", kurang(i, matrix))
    kurangi += cekPosisiKosong(matrix)
    print("Nilai dari fungsi Kurang(i) untuk semua ubin + X = ", kurangi)
    if(kurangi%2 == 0):
        return True
    return False

# Generate a random 4x4 matrix
def generateRandomMatrix():
    matrix = np.arange(1, 17)
    np.random.shuffle(matrix)

    matrix = np.reshape(matrix, (4,4))
    return matrix.tolist()
