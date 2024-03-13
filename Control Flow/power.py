def large_power(base, exponential):
    power = base ** exponential
    
    if power > 5000:
        return True
    else:
        return False
    
the_base = int(input('Enter the base number: '))
exp = int(input('Enter the power number: '))

print(large_power(the_base, exp))
