n=int(input("Enter number:"))
for i in range(0,n+1):
    print(" "*(n-i),end="")
    for j in range(-i,i+1):
        print(n-abs(j)+1 if j!=0 else 0,end="")
    print("")
