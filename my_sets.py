def common_member(a,b):
    a_set = set(list_1)
    b_set = set(list_2)
if(a_set & b_set):
    print(a_set & b_set)
else:
    print("No common elements")
    
list1 = str(input("Enter Random numbers separating with space "))
list_1 = list1.split()
print(list_1)

list2 =str(input("Enter more random numbers "))
list_2 = list2.split()
print(list_2)

