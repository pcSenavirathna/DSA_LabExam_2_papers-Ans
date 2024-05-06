def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci (n-2)


while True:
    n = int(input("Enter a number : "))
    if n==-1:
        print("Output : Finished")
        break
    else:
        print("The",n,"th number :",Fibonacci(n))
