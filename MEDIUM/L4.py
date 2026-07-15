w1 = "abcd"
w2 = "pq"

def mergeAlternately(word1, word2):
    n = max(len(word1), len(word2))
    output = []
    for i in range(n):
        if i>= len(word1):
            output.append(word2[i])
        elif i>= len(word2):
            output.append(word1[i])
        else:
            output.append(word1[i])
            output.append(word2[i])
    return "".join(output)

print(mergeAlternately(w1,w2))