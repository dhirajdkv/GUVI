one=int(input())
flag=True
print(one,end=' ')
for i in range(10):
    if flag==True:
        one=one+4
        print(one,end=' ')
        flag=False
    else:
        one=one-3
        print(one,end=' ')
        flag=True
        
