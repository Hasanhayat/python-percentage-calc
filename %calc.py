total=input("enter total possible marks of five subjects:")
e = input("enter english marks:")
c = input("enter chemistry marks:")
p = input("enter physics marks:")
b = input("enter biology marks:")
m = input("enter maths marks:")

e = int(e)
c = int(c)
p = int(p)
b = int(b)
m = int(m)
total=int(total)

result1 =  e+c+p+b+m
result2 = (result1 / total) * 100
print("YOUR TOTAL MARKS ARE",result1)
print("YOUR PERCENTAGE ARE:",result2)
print("THANKS")
