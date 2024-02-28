a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))


if a >= b and a >= c:
    print(f"The largest number is {a}")
elif b >=a and b >= c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")


#adding and dividing
x = 50
y = x // 0.5
z = y + 20

print(z)
