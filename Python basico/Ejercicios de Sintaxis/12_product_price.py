
product_price = int(input("Enter the price of your product: "))

if (product_price < 100):
    final_price = (product_price * 0.98)
else:
    final_price = (product_price * 0.9)

print (f"The cost after discount is: {final_price}")