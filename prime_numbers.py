x= int (input("Enter lowest value"))
y= int (input("Enter the highest value"))
for number in range(x,y+1):
    if number > 1:
        for i in range(2, number):
            if number%i == 0:
                break
        else:
            print(number)