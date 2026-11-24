arr=[1,0,2,3,0,4,5,0]

for i in range(0,len(arr)-1,1):
    if(arr[i]==0):
        for j in range(len(arr)-1,i+1,-1):
            arr[j]=arr[j-1]
        i=i+1
print(arr)