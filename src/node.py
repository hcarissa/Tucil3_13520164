from typing import NamedTuple
import copy
from sympy import root
from functions import *

class Node(NamedTuple):
    nodeKe: int
    parent: list
    matrix: list[list]
    cost: int

def inputOwnMatrix():
    print("Masukkan matrix dengan menggunakan spasi untuk tiap elemen\ndalam sebuah baris dan enter jika akan menuju ke baris selanjutnya\nMatrix harus berukuran 4 x 4")
    newMatrix = []
    for i in range(4):
        line = input("Masukkan baris ke-"+str(i+1)+": ")
        newRow = [int(x) for x in line.split()]
        newMatrix.append(newRow)
    cost = findcost(newMatrix, 0)
    root = Node(1, [], newMatrix, cost)
    return root

def printMatrix(Node):
    for i in range(4):
        print("+----+----+----+----+")
        for j in range(4):
            print("| ", end="")
            if(Node.matrix[i][j] < 10):
                print(Node.matrix[i][j], end='  ')
            elif(Node.matrix[i][j] == 16):
                print('  ', end=' ')
            else:
                print(Node.matrix[i][j], end=' ')
            if(j==3):
                print("|", end="")
        print()
    print("+----+----+----+----+")


def moveNode(rootNode, movement, nodeKe):
    # movement
    # 1 - atas
    # 2 - kanan
    # 3 - bawah
    # 4 - kiri
    isTraded = False
    #parent dari root ditambahin ke node
    parent = copy.deepcopy(rootNode.parent)
    if(rootNode.nodeKe not in parent):
        parent.append(rootNode.nodeKe)
    #matrix dari root ditambahkan ke node
    nMatrix = copy.deepcopy(rootNode.matrix)
    #tile 16 dipindah ke atas
    if(movement==1):
        for i in range(4):
            for j in range(4):
                if(nMatrix[i][j] == 16):
                    # trade tile 16 dengan atasnya
                    temp = nMatrix[i-1][j]
                    nMatrix[i-1][j] = nMatrix[i][j]
                    nMatrix[i][j] = temp
                    # cari cost new matrix
                    cost = findcost(nMatrix, len(parent))
                    parent.append(nodeKe)
                    # make new node
                    newNode = Node(nodeKe, parent, nMatrix, cost)
                    isTraded = True
                    break
            if(isTraded):
                break
    #tile 16 dipindah ke kanan
    elif(movement==2):
        for i in range(4):
            for j in range(4):
                if(nMatrix[i][j] == 16):
                    # trade tile 16 dengan kanannya
                    temp = nMatrix[i][j+1]
                    nMatrix[i][j+1] = nMatrix[i][j]
                    nMatrix[i][j] = temp
                    # cari cost new matrix
                    cost = findcost(nMatrix, len(parent))
                    parent.append(nodeKe)
                    # make new node
                    newNode = Node(nodeKe, parent, nMatrix, cost)
                    isTraded = True
                    break
            if(isTraded):
                break
    elif(movement==3):
    #tile 16 dipindah ke bawah
        for i in range(4):
            for j in range(4):
                if(nMatrix[i][j] == 16):
                    # trade tile 16 dengan bawahnya
                    temp = nMatrix[i+1][j]
                    nMatrix[i+1][j] = nMatrix[i][j]
                    nMatrix[i][j] = temp
                    # cari cost new matrix
                    cost = findcost(nMatrix, len(parent))
                    parent.append(nodeKe)
                    # make new node
                    newNode = Node(nodeKe, parent, nMatrix, cost)
                    isTraded = True
                    break
            if(isTraded):
                break
    elif(movement==4):
    #tile 16 dipindah ke kiri
        for i in range(4):
            for j in range(4):
                if(nMatrix[i][j] == 16):
                    # trade tile 16 dengan kirinya
                    temp = nMatrix[i][j-1]
                    nMatrix[i][j-1] = nMatrix[i][j]
                    nMatrix[i][j] = temp
                    # cari cost new matrix
                    cost = findcost(nMatrix, len(parent))
                    parent.append(nodeKe)
                    # make new node
                    newNode = Node(nodeKe, parent, nMatrix, cost)
                    isTraded = True
                    break
            if(isTraded):
                break
    else:
        print("Invalid Movement Input")
    return newNode
    
def isFinalState(finalNode):
    for i in range (4) :
        for j in range(4) :
            if(finalNode.matrix[i][j] != 4*i+j+1):
                return False
    return True

def findcost(matrix, jarak):
    cost = jarak
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] != 4*i+j+1 and matrix[i][j] != 16):
                cost+=1
    return cost

def isPossible(matrix, movement):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] == 16):
                if(movement==1 and i == 0):
                    return False
                elif(movement==2 and j==3):
                    return False
                elif(movement==3 and i==3):
                    return False
                elif(movement==4 and j==0):
                    return False
                elif(movement < 5 and movement > 0):
                    return True

def isGaBalik(node, allNode):
    if(node.nodeKe == 1):
        return True
    idxparent = len(node.parent) - 2
    for i in range(4):
        for j in range(4):
            if(node.matrix[i][j] != allNode[idxparent].matrix[i][j]):
                return True
    return False
            