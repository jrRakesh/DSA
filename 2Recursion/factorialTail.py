def tailfact(n, acc):
    if (n == 0 or n==1):
        return acc
    else:
        return tailfact(n-1, acc*n)
result = tailfact(5,1)
print(f"The factorial is : {result}")