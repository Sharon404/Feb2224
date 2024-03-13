def calculate_discount(price, discount):
    percentage_discount = discount/100
    discounted_value = price * percentage_discount
    resulting_value = price - discounted_value
    
    if discount >= 20:
        return resulting_value
    else:
        return price
    
pricing = float(input("Enter the initial price: "))
discounting = float(input("Enter the discount: "))

print(calculate_discount(pricing, discounting))