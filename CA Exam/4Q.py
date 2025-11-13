# Palidrome pair
def palindrome_pairs(words):
    res = []
    
    for i in range(len(words)):
        for j in range(len(words)):
           
            if i != j:  

                combined = words[i] + words[j]
                if combined == combined[::-1]: 
                 
                    res.append([i, j])
    return res
words = ["bat", "tab", "cat"]
print(palindrome_pairs(words))
