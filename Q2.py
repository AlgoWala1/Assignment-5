num = int(input(("Enter number:")))
n1 = int(input(("Enter lower term of range:")))
n2 = int(input(("Enter higher term of range:")))
for i in range(n1,n2+1):
    if i%num==0:
        print(i)
    
