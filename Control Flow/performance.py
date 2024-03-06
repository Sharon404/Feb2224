mark = int(input("What marks did you score? "))

if 100 >= mark >= 70:
    print("Distinction")
elif 69 >= mark >= 60:
    print("Credit")
elif 59 >= mark >= 50:
    print("Pass")
elif 49 >= mark >= 40:
    print("Fair")
elif mark < 40:
    print("Fail")
else:
    print("Reenter the marks")