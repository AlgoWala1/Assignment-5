###Area by heron's formula
s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))
sem = (s1+s2+s3)/2
area = pow((sem*(sem-s1)*(sem-s2)*(sem-s3)),0.5)
print("Area of the given triangle:",area)
