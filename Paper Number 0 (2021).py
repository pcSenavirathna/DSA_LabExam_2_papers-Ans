def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
    


while True:
    n = int(input("Enter the number : "))
    if n == -1:
        print("Output : Fnished")
        break
    elif n<1:
        print("invalid number try again")
    else:
        print("Output: ",fact(n))


