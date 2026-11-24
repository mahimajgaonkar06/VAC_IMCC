arr=[10,20,30,40,50]
n=int(input("enter no. of shifts: "))

for i in range(n):
    last=arr[-1]

    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last
print(arr)