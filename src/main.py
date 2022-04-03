from node import *
from functions import *
from queue import *
import time
import heapq

# node : nodeke, parent, matrix, cost, movementlist
# awal program
print("                                                Welcome to :")
print()
print(" ██╗███████╗      ██████╗ ██╗   ██╗███████╗███████╗██╗     ███████╗    ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ ")
print("███║██╔════╝      ██╔══██╗██║   ██║╚══███╔╝╚══███╔╝██║     ██╔════╝    ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗")
print("╚██║███████╗█████╗██████╔╝██║   ██║  ███╔╝   ███╔╝ ██║     █████╗      ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝")
print(" ██║╚════██║╚════╝██╔═══╝ ██║   ██║ ███╔╝   ███╔╝  ██║     ██╔══╝      ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗")
print(" ██║███████║      ██║     ╚██████╔╝███████╗███████╗███████╗███████╗    ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║")
print(" ╚═╝╚══════╝      ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝")
print("                                                                                                                        ")
print("                                         Choose input matrix methods : ")
print("                                              1. Input File")
print("                                              2. Input Manual")
print("                                              3. Randomize Matrix")
print()
methods = int(input("Enter the number of the chosen methods : "))
# ngecek input
while(methods != 1 and methods !=2 and methods!=3):
    print("Invalid input, try again")
    methods = int(input("Enter the number of the chosen methods : "))
# input untuk yang file
if(methods == 1):
    namaFile = str(input("Enter file name in folder test\nex. 'matrix.txt' (without the apostrophe) : "))
    with open("./test/" + namaFile) as f:
        lines = f.readlines()
    matrix = [[int(x) for x in line.split()]for line in lines]
    cost = findcost(matrix, 0)
    root = Node(1, [], matrix, cost)
# input matrix sendiri
elif(methods == 2):
    root = inputOwnMatrix()
else:
    print("Generating random matrix...")
    matrix = generateRandomMatrix()
    cost = findcost(matrix, 0)
    root = Node(1, [], matrix, cost)
#solving
allNode = []
counterNode = 1
print()
print("∷∷∷∷∷∷ Initial Puzzle State ∷∷∷∷∷∷")
printMatrix(root)
print("\n∷∷∷∷∷∷∷ Values of \"Kurang\" ∷∷∷∷∷∷∷")
start_time = time.time()
if(canBeSolved(root.matrix)):
    print()
    print("Puzzle is solvable! \n")
    print("Finding solution...\n")
    time.sleep(0.5)
    activeSet = []
    heapq.heappush(activeSet, (root.cost, root))
    allNode.append(root)
    while(len(activeSet)!= 0):
        check = heapq.heappop(activeSet)
        # get the node only
        checking = check[1]
        if(isFinalState(checking)):
            print("The solution is found!")
            counter = 0
            # print semua solusi
            for nodes in (checking.parent):
                print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
                print("Step "+str(counter))
                printMatrix(allNode[nodes-1])
                print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
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
    print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
    print("Sum of Nodes\n(including the root node) : ", counterNode)
else:
    print("Puzzle is not solvable!")
    print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
print("Execution Time : %.10s Seconds" % (time.time() - start_time))
print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
input("Press any key to exit...")
