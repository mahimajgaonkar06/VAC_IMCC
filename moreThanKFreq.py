n=123214265434766138121
k=3
def countFreq(n,k):

    freq=[0]*10

    while n>0:
        l_d=n%10
        freq[l_d]+=1
        n=n//10


    res=[]
    for i in range(len(freq)):
        if freq[i]>=k:
            res.append(i)
    return res
            
res=countFreq(n,3)
print(res)

