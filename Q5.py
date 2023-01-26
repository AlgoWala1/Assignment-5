string = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
rows = int(input("Input the number of rows: "))
indexpos = 0
for i in range(0,rows):
    for j in range(0,i+1):
        if indexpos ==len(string):
            indexpos = 0
        print(string[indexpos],end = '')
        indexpos +=1
    print()
