n=int(input("Enter number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64)+chr(j+96),end="")
    print("")
