#implicit = python does it automatically

a = 5
b = 25.0
print(a+b)
print(type(a+b))


#explicit = done manually

n1 = "100"
n2 = "200"

n3 = int(n1)
n4 = int(n2)

print( int(n1) + int(n2))
print(n1 + n2) #string added
print(n3 + n4)

print(n1, type(n1))
print(n2, type(n2))

p = 3.3
print(int(p))


total = a + b + n3 + n4 + p
print (f"Total = {total}")