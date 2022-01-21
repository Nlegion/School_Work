a = 1
b = 2
print("start: a = ",a,"b = ",b)

c = a
a = b
b = c
print("end smht: a = ",a,"b = ",b)

a,b = b,a
print("end 2: a = ",a,"b = ",b)