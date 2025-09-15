# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price   

# Ask user for inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Show result
if discount_percent >= 20:
    print(f"Discount applied! Final price = {final_price}")
else:
    print(f"No discount applied. Final price = {final_price}")
