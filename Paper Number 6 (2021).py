def recursive(n):
    if(n==1):
        return 1
    else:
        return 2*recursive(n-1)+1

while True:
    n = int(input("Enter the number : "))
    if(n==-1):
        print("Output : Finished")
        break
    else:
        print("Output",recursive(n))
