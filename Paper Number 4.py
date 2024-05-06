def powfun(x,n):
    if x==0:
        return 1
    else:
        return x * pow(x,n-1)


while True:
    print()
    x = int(input("Enter the number : "))
    if(x==-1):
        print("Output : Finished")
        break
    n = int(input("Enter the Power number : "))
    if(n==-1):
        print("Output : Finished")
        break
    elif(n<0):
        print("Invalid number Try again")
    else:
        print("Output :",powfun(x,n))
    
