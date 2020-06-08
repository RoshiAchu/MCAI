s=int(input("Enter the list size n"))
a=[]
p=[]
for i in range(s):
    t=int(input("Enter list element"))
    a.append(t)
    if(t>0):
        p.append(t)
print("Positive Numbers:")
print(p)
