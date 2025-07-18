def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

def fibonacci(p):
    if p==0:
        return 0
    elif p==1:
        return 1
    else:
       return fibonacci(p-1)+fibonacci(p-2)
print(fibonacci(8))
