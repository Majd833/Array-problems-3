a=[0,1,2,2,1,0,2,0,1,2,1,2,0,1,0,2,1,0]
zero=[]
one=[]
two=[]
new=[]
for i in range(0,len(a)):
    if a[i]==0:
        zero.append(a[i])
    elif a[i]==1:
        one.append(a[i])
    elif a[i]==2:
        two.append(a[i])
for i in range(0,len(zero)):
    new.append(zero[i])
for i in range(0,len(one)):
    new.append(one[i])
for i in range(0,len(two)):
    new.append(two[i])
print("the old array was",a)
print("the new array is", new)