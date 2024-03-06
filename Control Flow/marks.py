marks = int(input('Enter your marks '))

if marks < 30:
    print('Failed')
elif marks > 75:
    print('Passed with distinction')
else:
    print('Passed')