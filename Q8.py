posnum = []
negnum = []
evenum = []
oddnum = []
allnum = []
i = int()
for i in range(0,10):
    k = int(input("Enter number :"))
    allnum.append(k)
    if k>0:
        posnum.append(k)
    else:
        negnum.append(k)
    if k%2 == 0:
        evenum.append(k)
    else:
        oddnum.append(k)        
print("Positive numbers: ",posnum)
print("Negative numbers: ",negnum)
print("Even Numbers: ",evenum)
print("Odd Numbers: ",oddnum)
###Code for counting the occurences
dupliList = []
for j in allnum:
    if j in dupliList:
        continue
    print("Count of ",j,"is",allnum.count(j))
    dupliList.append(j)
