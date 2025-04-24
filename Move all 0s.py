def push0(a,asize):
    zero=0
    nonzero=0
    while nonzero!=asize:
        if a[nonzero]!=0:
            a[nonzero],a[zero]=a[zero],a[nonzero]
            zero+=1
        nonzero+=1
a=[1,3,0,56,87,0,0,2,7,0,7,0,89]
asize=len(a)
print(a)
push0(a,asize)
print("The array after pushing all the zeros to the end;")
print(a)