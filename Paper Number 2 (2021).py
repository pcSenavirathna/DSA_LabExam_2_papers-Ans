def recursive(n):
    if n==1:
        return 2
    else:
        return recursive(n-1)/2

while True:
    n = int(input("Enter number : "))
    if n == -1:
        print("Output : Finished")
        break
    else:
        print("Output : ",recursive(n))
