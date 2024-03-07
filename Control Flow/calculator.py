def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select the operator")
print("1.Add\n")
print("1.Subtract\n")
print("1.Multiply\n")
print("1.Divide\n")

while True:
    choice = input("Enter choice 1/2/3/4: ")
    if choice in ('1', '2', '3', '4'):
        try:
            first = float(input("Enter the first number: "))
            second = float(input('Enter the second number: '))
        except ValueError:
            print("Invalid Input. Please enter a number")
            continue
        
        if choice == '1':
            print(first, '+', second, '=', add(first, second))
        elif choice == '2':
            print(first, '-', second, '=', subtract(first, second))
        elif choice == '3':
            print(first, '*', second, '=', multiply(first, second))
        elif choice == '4':
            print(first, '/', second, '=', divide(first, second))
        
        nextcalculation = input("Want another calculation? (yes/no): ")
        if nextcalculation == 'no':
            break
    else:
            print("Invalid Input")    
    
    
    
