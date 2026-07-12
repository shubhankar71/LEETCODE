ex = [40,10,20,30]
# 10,20,30,40 == > 1,2,3,4
def arrayRankTransform(arr):
    arr.sort()
    num = []
    for i in range(len(arr)):
        print(len(arr)-i)
    

print(arrayRankTransform(ex))