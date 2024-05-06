#declare the funtion
def Multiply (M,n):
    if (n==1):
        return M
    else:
        return M + Multiply(M,n-1) # recursive method


while True:
    M = int(input("Enter a number : "))
    if(M==-1):
        break
    
    n = int(input("Enter a number : "))
    if(n==-1):
        break

    else:
        print("multiplication of numbers",Multiply (M,n)) #call recursive funtion
