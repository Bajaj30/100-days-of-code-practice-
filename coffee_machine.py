print("Price of an espresso is - $1.5")
print("Price of a latte is - $2.5")
print("Price of a cappuccino is - $3.5")

choice = int(input("Enter your choice of coffee - espresso(1)/latte(2)/cappuccino(3): "))
cent_50_coin = int(input("Enter no of 50-cent coins you inserted: ")) * 0.5
cent_10_coin = int(input("Enter no of 10-cent coins you inserted: ")) * 0.1
dollar_1_coin = int(input("Enter no of 1-dollar coins you inserted: ")) * 1
n = int(input("Enter the number of cups you want to order: "))

def ingredients_report():
    global milk, water, coffee
    milk = 1000  
    water = 2000
    coffee = 500

    for _ in range(n):  
        if choice == 1:  # Espresso
            water -= 50
            coffee -= 18
        elif choice == 2:  # Latte
            milk -= 150
            water -= 200
            coffee -= 24
        elif choice == 3:  # Cappuccino
            milk -= 100
            water -= 250
            coffee -= 24

    print(f"Remaining ingredients: Milk={milk}ml, Water={water}ml, Coffee={coffee}g")


def process_order(price):
    total_inserted = cent_10_coin + cent_50_coin + dollar_1_coin
    total_price = price * n

    if total_inserted == total_price:
        print("Coming right up!")
    elif total_inserted < total_price:
        print("Insufficient funds. Please insert more money.")
    else:
        change = total_inserted - total_price
        print(f"Coming right up! Here is your change of ${change:.2f}")


if choice == 1:
    process_order(1.5)
elif choice == 2:
    process_order(2.5)
elif choice == 3:
    process_order(3.5)

ingredients_report()
