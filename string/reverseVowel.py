exampleString1 = 'hello'
exampleString2 = 'leetcode'

listOfVowel = ['a','e','i','o','u']
def reverseVowel(OriginalString):
    global listOfVowel
    vowelString = []
    lengthOfOriginalString = len(OriginalString)
    for word in OriginalString:
        if word in listOfVowel:
            vowelString.append(word)
    print(vowelString)
    for index in range(lengthOfOriginalString): 
        if OriginalString[index] in listOfVowel:
            OriginalString = OriginalString[:index] + vowelString.pop() + OriginalString[index + 1:]
    print(vowelString)
 #   print(vowelString)
    return ''.join(OriginalString)


print(reverseVowel(exampleString2))
