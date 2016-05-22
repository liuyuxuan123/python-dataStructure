#interger to English Words
exampleInput = 123
exampleInput2 = 12345
exampleInput3 = 1234567

#Divide it into every three digit


    
def intToEnglishFunc(someInput):
    sigleDigitToEnglish = {
        1 : 'One',
        2 : 'Two',
        3 : 'Three',
        4 : 'Four',
        5 : 'Five',
        6 : 'Six',
        7 : 'Seven',
        8 : 'Eight',
        9 : 'Nine'
        }
    tensDigitToEnglish = {
        10 : "Ten",
        11 : "Eleven",
        12 : "Twelve",
        13 : "Thirteen",
        14 : "Fourteen",
        15 : "Fifteen",
        16 : "Sixteen",
        17 : "Seventeen",
        18 : "Eighteen",
        19 : "Nineteen",
        20 : "Twenty",
        30 : "Thirty",
        40 : "Forty",
        50 : "Fifty",
        60 : "Sixty",
        70 : "Seventy",
        80 : "Eighty",
        90  : "Ninety"
        }

    ten = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    hundred = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    
    unit = ['Hundred','Thousand','Million']    


    outPutString = ''
    numbers = someInput
    if numbers > 0:
        temp = numbers // 100
        
        if temp > 0:
        
            print('I am here',temp)
            outPutString += (ten[temp] + ' ' + unit[0])
            
        temp = numbers % 100
        
        if temp >= 10 and temp < 20:
            outPutString += ' '
            outPutString += twenty[temp % 10]
            return outPutString
        elif temp > 20:
            temp = temp / 10
            outPutString += ' '
            outPutString += hundred[temp -1]

        temp = numbers % 10
        if temp > 0:
            outPutString += ' '
            outPutString += ten[temp]

    return outPutString

#print(intToEnglishFunc(314))


def intToEnglish(someInput):
    outPutString = ''
    i = 0
    unit = ['','Thousand','Million','Billion'] 
    while someInput > 0:
        temp = someInput % 1000
        if temp > 0:
            outPutString = intToEnglishFunc(temp) +' '+ unit[i] + ('' if len(outPutString) == 0 else ' ') + outPutString
  
        someInput //= 1000
        i += 1

    print(outPutString)


intToEnglish(exampleInput3)
        
            
            
    

