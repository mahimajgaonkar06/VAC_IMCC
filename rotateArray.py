arr = [10, 20, 30, 40, 50, 60]
n=int(input("enter no. of shifts: "))

for i in range(n):
    first = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = first

print(arr)