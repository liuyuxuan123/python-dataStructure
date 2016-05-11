#this algorithm is used to solve some problems concern to least spanning tree


weightMatrix = [[0,4,9,21],[4,0,8,17],[9,8,0,16],[21,17,16,0]]

class weightEdge(object):
    def __init__(self):
        self.startIndex = 0
        self.endIndex = 0
        self.weight = 0
    def __repr__(self):
        return "startIndex = %d endIndex = %d weight = %d" % (self.startIndex,self.endIndex,self.weight)

class weightEdgeUnion(object):
    def __init__(self):
        self.weightEdgeUnion = []
    def insertEdge(self,weightEdge):
        self.weightEdgeUnion.append(weightEdge)

myWeightEdgeUnion = weightEdgeUnion()




#for row in range(len(weightMatrix)):
#    for col in range(len(weightMatrix)):
#        newWeightEdge = weightEdge()
#        newWeightEdge.startIndex = row
#        newWeightEdge.endIndex = col
#        newWeightEdge.weight = weightMatrix[row][col]
#        myWeightEdgeUnion.insertEdge(newWeightEdge)

for row in range(len(weightMatrix)-1):
    newWeightEdge = weightEdge()
    newWeightEdge.startIndex = 0
    newWeightEdge.endIndex = row+1
    newWeightEdge.weight = weightMatrix[0][row+1]
    myWeightEdgeUnion.insertEdge(newWeightEdge)
    print(myWeightEdgeUnion.weightEdgeUnion[row].startIndex,myWeightEdgeUnion.weightEdgeUnion[row].endIndex,myWeightEdgeUnion.weightEdgeUnion[row].weight)

#for i in range(16):
#    print(myWeightEdgeUnion.weightEdgeUnion[i].startIndex)
#    print(myWeightEdgeUnion.weightEdgeUnion[i].endIndex)
#    print(myWeightEdgeUnion.weightEdgeUnion[i].weight)

MAX = 1000

#tmpEdge = weightEdge()
#tmpEdge = myWeightEdgeUnion.weightEdgeUnion[5]
#print(tmpEdge.startIndex)
        
def findMinimumSpanningTreePRIM(weightMatrix,myWeightEdgeUnion):
    for i in range(4):
        weight = MAX
        minWeightIndex = i
            
        for j in range(i,4):
        
            if myWeightEdgeUnion.weightEdgeUnion[j].weight > myWeightEdgeUnion.weightEdgeUnion[minWeightIndex].weight:
                weight = myWeightEdgeUnion.weightEdgeUnion[j].weight
                minWeightIndex = j

        tmpEdge = myWeightEdgeUnion.weightEdgeUnion[j]
        myWeightEdgeUnion.weightEdgeUnion[j] = myWeightEdgeUnion.weightEdgeUnion[minWeightIndex]
        myWeightEdgeUnion.weightEdgeUnion[minWeightIndex] = tmpEdge

        for k in range(i + 1,4):
            if myWeightEdgeUnion.weightEdgeUnion[k].weight > weightMatrix[i][k]:
                myWeightEdgeUnion.weightEdgeUnion[k].startIndex = i
                myWeightEdgeUnion.weightEdgeUnion[k].endIndex = k
                myWeightEdgeUnion.weightEdgeUnion[k].weight = weightMatrix[i][k]



## this is the using 
#findMinimumSpanningTreePRIM(weightMatrix,myWeightEdgeUnion)

#for i in range(4):
#    print(myWeightEdgeUnion.weightEdgeUnion[i].weight)


newWeightEdgeUnion = weightEdgeUnion()

def findMinimumSpaningTreeKRUSKAL(weightMatrix,newWeightEdgeUnion):
    status = []

    lenth = len(weightMatrix)
    num = 0
    for i in range(lenth):
        status.append(i)
    print(status)
    while num < lenth - 1:
   
        weight = MAX
        minWeightIndex = (0,0)
        for i in range(lenth):
            for j in range(lenth):

                if weightMatrix[i][j] != 0 and weightMatrix[i][j] < weight:
                    weight = weightMatrix[i][j]
                    minWeightIndex = (i,j)
                    
        #print(minWeightIndex)
        if weight == MAX:
            print('No solution')
            return 0

        if status[minWeightIndex[0]] != status[minWeightIndex[1]]:
            newEdge = weightEdge()
            newEdge.startIndex = minWeightIndex[0]
            newEdge.endIndex = minWeightIndex[1]
            newEdge.weight = weightMatrix[minWeightIndex[0]][minWeightIndex[1]]
            newWeightEdgeUnion.insertEdge(newEdge)
            num += 1
            for i in range(lenth):
                if status[i] == status[minWeightIndex[1]]:
                    status[i] = status[minWeightIndex[0]]
                
        weightMatrix[minWeightIndex[0]][minWeightIndex[1]] = MAX
        weightMatrix[minWeightIndex[1]][minWeightIndex[0]] = MAX
     
    print(status)
    for i in range(lenth - 1):
        print(newWeightEdgeUnion.weightEdgeUnion[i].weight)
    
    return 1

#findMinimumSpaningTreeKRUSKAL(weightMatrix,newWeightEdgeUnion)


for i in range(3):
    print(myWeightEdgeUnion.weightEdgeUnion[i])
print()
lenth = len(weightMatrix)
for i in range(lenth - 1):
    print(i)


def INeedSomeKindOfPractice(weightMatrix,myWeightEdgeUnion):
    lenth = len(weightMatrix)
    
    for i in range(lenth - 1):
        weight = MAX
        minWeightIndedx = i
        for j in range(i,lenth - 1):
            if weight > myWeightEdgeUnion.weightEdgeUnion[j].weight:
                weight = myWeightEdgeUnion.weightEdgeUnion[j].weight
                minWeightIndex = j

        tmpEdge = myWeightEdgeUnion.weightEdgeUnion[minWeightIndex]
        myWeightEdgeUnion.weightEdgeUnion[minWeightIndex] = myWeightEdgeUnion.weightEdgeUnion[i]
        myWeightEdgeUnion.weightEdgeUnion[i] = tmpEdge

        for k in range(i + 1,lenth - 1):
            if myWeightEdgeUnion.weightEdgeUnion[k].weight > weightMatrix[i + 1][myWeightEdgeUnion.weightEdgeUnion[k].endIndex]:
                myWeightEdgeUnion.weightEdgeUnion[k].startIndex = i + 1
 #               myWeightEdgeUnion.weightEdgeUnion[k].endIndex = myWeightEdgeUnion.weightEdgeUnion[k].endIndex
                myWeightEdgeUnion.weightEdgeUnion[k].weight = weightMatrix[i + 1][myWeightEdgeUnion.weightEdgeUnion[k].endIndex]

    for m in range(lenth - 1):
        print(myWeightEdgeUnion.weightEdgeUnion[m])
        
        

        
#INeedSomeKindOfPractice(weightMatrix,myWeightEdgeUnion)

def INeedSomePractice(weightMatrix):
    lenth = len(weightMatrix)
    newWeightEdgeUnion = weightEdgeUnion()
    status = []
    for i in range(lenth):
        status.append(i)

    num = 0
    while(num < lenth - 1):
        weight = MAX
        minWeightIndex = (0,0)
        
        for i in range(lenth):
            for j in range(lenth):
                if weightMatrix[i][j] != 0 and weightMatrix[i][j] < weight:
                    weight = weightMatrix[i][j]
                    minWeightIndex = (i,j)

        if weight == MAX:
            return 0
        

        if status[minWeightIndex[0]] != status[minWeightIndex[1]]:
            newEdge = weightEdge()
            newEdge.startIndex = minWeightIndex[0]
            newEdge.endIndex = minWeightIndex[1]
            newEdge.weight = weightMatrix[minWeightIndex[0]][minWeightIndex[1]]
            newWeightEdgeUnion.insertEdge(newEdge)
            num += 1
            for k in range(lenth):
                if status[minWeightIndex[1]] == status[k]:
                    status[k] = status[minWeightIndex[0]]

        weightMatrix[minWeightIndex[0]][minWeightIndex[1]] = MAX
        weightMatrix[minWeightIndex[1]][minWeightIndex[0]] = MAX
    for m in range(3):
        print(newWeightEdgeUnion.weightEdgeUnion[m])
    return 1
    
INeedSomePractice(weightMatrix)
print(weightMatrix)
    
        
        


    
        
          



        
        
        

      

       
        
