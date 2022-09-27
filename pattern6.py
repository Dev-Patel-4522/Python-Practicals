n=int(input("Enter number:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(-i+1,i):
        print(chr((abs(j)+65)),end="")
    print("")
