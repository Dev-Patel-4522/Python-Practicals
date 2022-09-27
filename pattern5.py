n=int(input("Enter number:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(i,n+1):
        print(chr(j+64),end=" ")
    print("")
