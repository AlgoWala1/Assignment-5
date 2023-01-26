string = input("Enter a string:")
words = string.split()
dupliList = []
for k in words:
    if k in dupliList:
        continue
    print("Count of ",k," is ",words.count(k))
    dupliList.append(k)
