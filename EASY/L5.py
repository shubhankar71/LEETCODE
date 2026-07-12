ex = [40,10,20,30]
# 10,20,30,40 == > 1,2,3,4
def arrayRankTransform(arr):
    arr.sort()
    #10,20,30,40 ==> 1,2,3,4
    num = []
    for i in range(len(arr)):
        print(i+1)
    

print(arrayRankTransform(ex))