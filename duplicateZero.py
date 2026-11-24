arr=[1,0,2,3,0,4,5,0]
i=0
while i<len(arr):
    if arr[i]==0:
        for i in range(len(arr)-1,i,-1):
            arr[i]=arr[i-1]
        i+=2
    else:
        i+=1
print(arr)