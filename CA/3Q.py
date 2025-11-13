
def min_window_subsequence(s1, s2):
    n, m = len(s1), len(s2)
    min_len = float('inf')
    start = -1
    i = 0

    while i < n:
        j = 0
    
        while i < n:
            if s1[i] == s2[j]:
                j += 1
                if j == m:
                    break
            i += 1

        if j < m:
            break  

        end = i + 1
        j -= 1
       
        while j >= 0:
            if s1[i] == s2[j]:
                j -= 1
            i -= 1

        i += 1  
        if end - i < min_len:
            min_len = end - i
            start = i

        i = i + 1

    return "" if start == -1 else s1[start:start + min_len]



s1 = "abcdebdde"
s2 = "bde"
print("The result is:", min_window_subsequence(s1, s2))
 
