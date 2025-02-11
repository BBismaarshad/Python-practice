
menu = {
    "Pizza": 600,
    "Burger": 200,
    "Biryani": 500,
    "Chaat": 250,
    "Gulab Jamun": 200,
    "Rabri": 1200,
    "Lassi": 100,
    "Doodh Patti Chai": 300,
}

print("Welcome to Flaming Python Grill")
print("Menu:")
print("Pizza : Rs.600\nBurger: Rs.200\nBiryani : Rs.500\nChaat : Rs.250\nGulab Jamun : Rs.200\nRabri : Rs.1200\nLassi : Rs.100\nDoodh Patti Chai : Rs.300")

# Initialize total order price
order_total = 0  

# Taking First Order
item_1 = input("Enter your Order: ").strip()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available.")

# Asking for another order
another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()

if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").strip()
    
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available.")

# Display final total
print(f"The total amount of your order is: Rs. {order_total}")
