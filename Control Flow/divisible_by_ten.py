def divisible(num):
    value = num % 10
    
    if value == 0:
        return True
    else:
        return False
    
num1 = int(input("Enter the integer: "))

print(divisible(num1))