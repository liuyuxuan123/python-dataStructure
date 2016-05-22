#Longest Substring Without Repeating Characters
exampleString1 = 'abcabcbb'
exampleString2 = 'bbbb'
exampleString3 = 'pwwkew'

def longestSubstringWithoutRepeat(OriginalString):
#    currentLongestSubstring = ''
    start = 0
    exist = [False for n in range(256)]
    length = 1
    lengthOfOriginalString = len(OriginalString)
    for i in range(lengthOfOriginalString):
        if exist[ord(OriginalString[i])]:
            length = max(length,i - start)
            for j in range(start,i):
                if OriginalString[j] == OriginalString[i]:
                    start = j + 1
                    break
                exist[ord(OriginalString[j])] = False
        else:
            exist[ord(OriginalString[i])] = True
            
    length = max(length,lengthOfOriginalString - start)
    return length
print(longestSubstringWithoutRepeat(exampleString3))
    
            
            
                
            
