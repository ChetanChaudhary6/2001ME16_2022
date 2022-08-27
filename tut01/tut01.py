def factorial(x):
    if(x==1):
        return 1
    return x*factorial(x-1)

x=int(input("Enter the number whose factorial is to be found\n"))
print("Factorial of ",x," is ",factorial(x))