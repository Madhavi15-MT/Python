item_1 = input("Enter the first item to add to the cart: ")
price_1 = float(input("Enter the price of the first item: "))

item_2 = input("Enter the second item to add to the cart: ")
price_2 = float(input("Enter the price of the second item: "))

item_3 = input("Enter the third item to add to the cart: ")
price_3 = float(input("Enter the price of the third item: "))

cart = {
    item_1: price_1,
    item_2: price_2,
    item_3: price_3
}
print("Items added to the cart:")
for item, price in cart.items():
    print(f"{item}: ${price:.2f}")
print("Total price of items in the cart: $", sum(cart.values()))
discount = float(input("Enter discount percentage (0-100): "))
if 0 <= discount <= 100:
    total_price = sum(cart.values())
    discount_amount = (discount / 100) * total_price
    final_price = total_price - discount_amount
    print(f"Total price after {discount}% discount: ${final_price:.2f}")