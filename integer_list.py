listing = str(input("Enter the numbers "))
new_list = listing.split()
print(new_list)

#converting the string into integer
for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
    
print("new_list", new_list)

#adding
addition = sum(new_list)
print("The sum is", addition)

