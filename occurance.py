n=int(input("enter a long number: "))
freq=[0]*10

while n >0:
    l_d=n%10
    freq[l_d]+=1
    n=n//10
    

print(freq)
