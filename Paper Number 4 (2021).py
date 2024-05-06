def recursive(n):
    if n==1:
        return 1
    else:
        return (n-1)+recursive(n-1)

while True:
    n = int(input("Enter the number : "))
    if(n==-1):
        print("Output : Finishyed")
        break
    else:
        print("Output",recursive(n))
