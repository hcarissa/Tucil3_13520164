import numpy as np

# Check posisi x di matrix
def posisi(x, matrix):
    index = 0
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == x:
                index = (4*i)+j
    return index

# Fungsi kurang
def kurang(x, matrix):
    hasil = 0
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] < x and posisi(matrix[i][j], matrix) > posisi(x, matrix)):
                hasil += 1
    return hasil

# Cek apakah posisi kosong ada di tile yang diarsir
def cekPosisiKosong(matrix):
    finalPos = 0
    shadedArea = [1, 3, 4, 6, 9, 11, 12, 14]
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 16 and ((4*i+j) in shadedArea)):
                finalPos = 1
    return finalPos

# Cek apakah matrix dapat disolve
def canBeSolved(matrix):
    kurangi = 0
    # display fungsi kurang untuk semua tile
    for i in range(1, 17):
        kurangi += kurang(i, matrix)
        print("● Kurang("+str(i)+") = ", kurang(i, matrix))
    kurangi += cekPosisiKosong(matrix)
    print("\nSum Of Kurang(i) + X = ", kurangi)
    # bila genap, bisa di solve
    if(kurangi%2 == 0):
        return True
    return False