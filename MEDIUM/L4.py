
n = "1000"
q = [
    [0,3],
    [1,1]
]

def sumAndMultiply(n, queries):
    new_1= []
    for start, end in queries:
        word = (n[start:end+1].replace("0", ""))
        if word == "":
            new_1.append(0)
            continue
        new_1.append(word)
        
    print(new_1)
    
    new_2 = []
    for i in range(len(new_1)):

        if new_1[i] == 0:
            new_2.append("")
            continue

        for j in range(len(new_1[i])):
            new_2.append(int(new_1[i][j]))
        new_2.append("")

    print(new_2)
    
    multiplier = 0
    output = []
    for i in range(len(new_2)):
        if new_2[i] == "":
            output.append(multiplier)
            multiplier = 0
            continue
        multiplier += int(new_2[i])
       
    new_3 = []

    for i in range(len(new_1)):

        if new_1[i] == 0:
            new_3.append(0)
            continue

        new_3.append(output[i] * int(new_1[i]))

    print(new_3)

            
sumAndMultiply(n,q)