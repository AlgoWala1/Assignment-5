def isPrime(i):
    if i == 1:
        return False
    for j in range(2,i):
        if i%j == 0:
            return False
    return True

n1= int(input("Enter lower range:"))
n2 = int(input("Enter higher range:"))
for i in range(n1,n2+1):
    if isPrime(i):
        print(i)
