a=[10,20,30,40,50,60]
sum=0
for i in range(0,6):
    if i%2==0:
        sum+=a[i]

print(sum)


# for i in range(0,len(a),2)
# to skip the odd number , avoid travesing to odd index