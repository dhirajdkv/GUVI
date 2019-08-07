one=int(input())
two=int(input())
flag=True
print(one,end=' ')
print(two,end=' ')
for i in range(10):
    if(flag==True):
        one=one+5
        print(one,end=' ')
        flag=False
    else:
        two=two+6
        print(two,end=' ')
        flag=True
