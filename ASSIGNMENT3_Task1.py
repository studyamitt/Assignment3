### Task 1: Calculate Factorial Using a Function

#1. Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion

def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)


val1=int(input("Enter the value for factorial: "))
result=factorial(val1)
print("Factorial of:",val1,"is:",result)