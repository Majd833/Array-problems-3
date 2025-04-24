def getmax(a,asize):
    counter=0
    maxones=0
    for i in range(0,asize):
        if a[i]==0:
            counter=0
        else:
            counter+=1
            maxones=max(maxones,counter)
    return maxones
a=[1,1,0,0,1,0,1,1,0,0,1,1,1,1]
asize=len(a)
print(getmax(a,asize))