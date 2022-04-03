from node import *
from functions import *
from queue import *
import time
import heapq

# node : nodeke, parent, matrix, cost, movementlist
# awal program
print("                                            Selamat datang di")
print()
print(" ██╗███████╗      ██████╗ ██╗   ██╗███████╗███████╗██╗     ███████╗    ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ ")
print("███║██╔════╝      ██╔══██╗██║   ██║╚══███╔╝╚══███╔╝██║     ██╔════╝    ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗")
print("╚██║███████╗█████╗██████╔╝██║   ██║  ███╔╝   ███╔╝ ██║     █████╗      ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝")
print(" ██║╚════██║╚════╝██╔═══╝ ██║   ██║ ███╔╝   ███╔╝  ██║     ██╔══╝      ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗")
print(" ██║███████║      ██║     ╚██████╔╝███████╗███████╗███████╗███████╗    ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║")
print(" ╚═╝╚══════╝      ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝")
print("                                                                                                                        ")
print("                                         Pilih cara input matrix : ")
print("                                              1. Input File")
print("                                              2. Input Manual")
print("                                              3. Randomize Matrix")
print()
methods = int(input("Ketik angka metode yang dipilih : "))
# ngecek input
while(methods != 1 and methods !=2 and methods!=3):
    print("Masukkan salah, silakan ulangi!")
    methods = int(input("Ketik angka metode yang dipilih : "))
# input untuk yang file
if(methods == 1):
    namaFile = str(input("Masukkan nama file yang berada di folder test\ncontoh 'matrix.txt' (tanpa tanda kutip) : "))
    with open("./test/" + namaFile) as f:
        lines = f.readlines()
    matrix = [[int(x) for x in line.split()]for line in lines]
    cost = findcost(matrix, 0)
    root = Node(1, [], matrix, cost)
# input matrix sendiri
elif(methods == 2):
    root = inputOwnMatrix()
else:
    matrix = generateRandomMatrix()
    cost = findcost(matrix, 0)
    root = Node(1, [], matrix, cost)
start_time = time.time()
#solving
allNode = []
counterNode = 1
print()
print("15-Puzzle yang akan diselesaikan :")
printMatrix(root)
print("Berikut nilai fungsi Kurang :")
if(canBeSolved(root.matrix)):
    print()
    print("Persoalan dapat diselesaikan!")
    print("Mencari solusi...")
    time.sleep(0.5)
    activeSet = []
    heapq.heappush(activeSet, (root.cost, root))
    allNode.append(root)
    while(len(activeSet)!= 0):
        check = heapq.heappop(activeSet)
        # get the node only
        checking = check[1]
        if(isFinalState(checking)):
            print("Berikut langkah menuju solusi :")
            counter = 0
            # print semua solusi
            for nodes in (checking.parent):
                print("=====================")
                print("Langkah ke-"+str(counter))
                printMatrix(allNode[nodes-1])
                print("Cost simpul : ", allNode[nodes-1].cost)
                print("=====================")
                counter+=1
            break
        else:
            # ngecek untuk setiap movement di node itu
            for i in range(1,5):
                #kalau movementnya ga bikin balik ke state sebelumnya, dan bisa pindah(ga nabrak pinggir")
                if(isGaBalik(checking, allNode) and isPossible(checking.matrix, i)):
                    #hitung jumlah simpul
                    counterNode += 1
                    #buat simpul baru yang udah pindah
                    newNode = moveNode(checking, i, counterNode)
                    #masukkin simpul baru ke array semua node
                    allNode.append(newNode)
                    #masukkin simpul baru ke queue
                    heapq.heappush(activeSet, (newNode.cost, newNode))
                    del newNode
    print("Jumlah simpul yang dibangkitkan\n(termasuk simpul akar) : ", counterNode)
else:
    print("Mohon maaf! Persoalan tidak dapat diselesaikan!")
print("Waktu eksekusi : %s detik" % (time.time() - start_time))
input("Tekan tombol apa saja untuk keluar...")

