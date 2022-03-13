k=[]
v=0
c=0
n=int(input("enter the number of elements"))
print("now enter the number")
for i in range(0,n):
    o=int(input())
    k.append(o)
print(k)
for i in range(n):
    if k[i]==0 or k[i]%2==0:
        v=v+1
    else:
        c+=1
print("Number of even numbers= ",v)
print("Number of odd numbers= ",c)