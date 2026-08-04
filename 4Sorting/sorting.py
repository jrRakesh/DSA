import random
import time
import matplotlib.pyplot as plt

def swap(a, b):
    temp = a
    a = b
    b = temp

def display(arr):
    for num in arr:
        print(num, end=" ")
    print()

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = arr[i]
        pos = i

        for j in range(i+1, n):
            if arr[j] < min:
                min = arr[j]
                pos = j
        if( i != pos):
            arr[i], arr[pos] = arr[pos], arr[i]

    


n = int(input("Enter n: "))
A = [random.randint(0, 99999) for _ in range(n)]

# display before sorting
display(A)
start_time = time.time()

selection_sort(A)

end_time = time.time()
display(A)  # display after sorting

print(f"Time taken is {end_time - start_time} seconds")

time_taken = end_time - start_time
timeTaken = []
for i in range():
    timeTaken = i
plt.plot(timeTaken, A)
plt.show()
