def calculate_discount(price, discount_percent):
    if discount_percent>= 20:
        return price - price*(discount_percent/100)
    else:
        return price
    
price =float(input("Pleas enter the price: "))
discount = float(input("Pleas enter discount percentage: "))
print("The price is: ",calculate_discount(price,discount))