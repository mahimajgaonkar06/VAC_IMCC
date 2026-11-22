n1=int(input("enter num: "))
n2=int(input("enter num: "))

freqn1=[0]*10
freqn2=[0]*10

while n1 >0:
    l_d=n1%10
    freqn1[l_d]+=1
    n1=n1//10


while n2 >0:
    l_d=n2%10
    freqn2[l_d]+=1
    n2=n2//10


if freqn1==freqn2:
    print("anagram")
else:
    print("not")


# alternate method without using 2 freq[]

#  for i in range(len(freq)):
#     if freq[i]!=0:
#         return False
# return True