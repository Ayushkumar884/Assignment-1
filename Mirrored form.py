k=str(input("enter word to get mirrored form: "))
l=len(k)
for i in range(l):
    print(k[((l-1)-i)],end="")