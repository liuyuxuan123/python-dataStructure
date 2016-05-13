sequence  = [1,2,2,4,4,8,10,12,13,14,15]

def binarySearchLowerBound(num):
    global sequence
    startIndex = 0
    endIndex = len(sequence) - 1
    while startIndex <= endIndex :
        midIndex = (startIndex + endIndex) // 2
        if sequence[midIndex] >= num:
            endIndex = midIndex - 1
        else:
            startIndex = midIndex + 1
    return startIndex

def binarySearchUpperBound(num):
    global sequence
    startIndex = 0
    endIndex = len(sequence) - 1
    while startIndex <= endIndex:
        midIndex = (startIndex + endIndex) // 2
        if sequence[midIndex] <= num:
            startIndex = midIndex + 1
        else:
            endIndex = midIndex - 1
    return endIndex

print(binarySearchLowerBound(2),'ss')
print(binarySearchUpperBound(2))
