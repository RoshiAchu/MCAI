t=-1
b=1
s=int(input("Enter the limit value n"))
a=[]
for i in range(s):
    a.append(0)
for i in range(s):
    if(i==0):
        a[i]=t+b
    elif(i==1):
        a[i]=a[0]+b
    else:
        k=i-1
        l=i-2
        a[i]=a[k]+a[l]
print("Fibonacci Series:")
for i in range(s):
    print(a[i])
