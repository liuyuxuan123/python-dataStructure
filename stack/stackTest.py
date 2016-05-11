#the very first thing is create a stack
#2016 May 10

class stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)== 0

    def push(self,x):
        self.items.append(x)
  

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]

    def pop(self):
        
        return self.items.pop()

#then how to convert a mid-fix order to post order

operationList = ['+','-','*','%','/','(',')']
operationOrder = {'+':2,'-':2,'*':3,'%':3,'/':3,'(':1}


'''
    for string in originalOperation:
        if string == ' ':
            continue
        elif not string in operationList:
            returnString += string
        else:
            while (not operandStack.isEmpty()) and (operationOrder[string] <= operationOrder[operandStack.top()]):
                returnString += operandStack.pop()
            operandStack.push(string)
   
    while not operandStack.isEmpty():
          returnString += operandStack.pop()
'''

def midToPostOrder(originalOperation):
    returnString = ''
    operandStack = stack()

          
    for string in originalOperation.split():
        if not string in operationList:
            returnString += string
        elif string == '(':
            operandStack.push('(')
        elif string == ')':
            topToken = operandStack.pop()
            while topToken != '(':
                returnString += topToken
                topToken = operandStack.pop()
        else:
            while (not operandStack.isEmpty()) and (operationOrder[string] <= operationOrder[operandStack.top()]):
                returnString += operandStack.pop()
            operandStack.push(string)

    while not operandStack.isEmpty():
        returnString += operandStack.pop()
            
    return returnString

ops ={
        '+' : lambda x,y:x + y,
        '-' : lambda x,y:x - y,
        '*' : lambda x,y:x * y,
        '/' : lambda x,y:x / y,
        '%' : lambda x,y:x % y
    }

def calculatePostOrder(postOrderString):
    numberStack = stack()

  
    for string in postOrderString:
        if string not in operationList:
            numberStack.push(int(string))
        else:
            right = numberStack.pop()
            left = numberStack.pop()
            number = ops[string](left,right)
            numberStack.push(number)
    return numberStack.top()
            


#to checkout whether this string is mid order 
def checkRight(originalString):
    checkOperand = stack()
    secondString = ''
    for string in originalString:
        if string == ' ':
            continue
        else:
            secondString += string
  
    
    for string in secondString:
        if not checkOperand.top() != None:
            if ( (checkOperand.top() in operationList) and (string not in operationList) ) or ( (string in operationList) and (checkOperand.top() not in operationList)):
                checkOperand.push(string)
            else:
                return False
    return True

#print(midToPostOrder( "( 1 + 4 ) * 5 - ( 2 - 4 ) * ( 2 + 5 )"))
hah = calculatePostOrder(midToPostOrder( "( 1 + 4 ) * 5 - ( 2 - 4 ) * ( 2 + 5 )"))
print(hah)                  


        
