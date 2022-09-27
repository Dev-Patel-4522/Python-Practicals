n=int(input("Enter number:"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(i if i>=j else j,end="")
    print("")
