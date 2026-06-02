import time
def Fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)

n = int(input("Enter a number: "))
start = time.time()
result = Fibo(n)
end = time.time()

print(f"The {n}th Fibonacci term is {result}.")
print(f"It took {end - start:.10f} seconds")