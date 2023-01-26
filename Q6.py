def isPrime(i):
    for j in range(2,i):
        if i%j == 0:
            return False
    return True

n1= int(input("Enter lower range:"))
n2 = int(input("Enter higher range:"))
for i in range(n1,n2+1):
    if i == 2:
        print("2")
    if isPrime(i):
        print(i)
