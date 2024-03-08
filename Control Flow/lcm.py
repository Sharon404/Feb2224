#check for the largest number and set it to z
def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
        
    while True:
        #check if z is divisible by both x and y else add 1 to the number till the condition is met
        if z % x == 0 and z % y == 0:
            lcm = z
            break
        z +=1
        
    return lcm

#input the numbers via the console and print the lcm
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(lcm(num1, num2))