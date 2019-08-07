flag=True
num=1
print(num,end=' ')
for i in range(2,16,2):
    if(flag==True):
        num = num * i
        print(num,end=" ")
        flag=False
    else:
        num = num + i
        print(num,end=" ")
        flag=True
