n=int(input("Enter number:"))
for i in range(1,n+1):
        print("0"*(i-1)+chr(i+64)+""+"1" *(n-i))
