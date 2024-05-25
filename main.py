#Welcome & ask user their name?

print("Welcome to GC Fruit Market!")
name = input("What is your name? ")
print("Welcome, " + name + "." " Which fruit would you like to buy?")

# Display a list of different fruit with prices
#Apple $2
#Grape $1
#Orange $3

fruit_prices = {
    1: {'name': 'Apple', 'price': 2},
    2: {'name': 'Grape', 'price': 1},
    3: {'name': 'Orange', 'price': 3}
}
for key, value in fruit_prices.items():
    print(f"{key}. {value['name']} ${value['price']}")

order_summary = []
running_total = 0

while True:
    selection = input("Enter the number of your choice or 'N' to checkout:")

    if selection == 'N':
        subtotal = running_total
        tax= subtotal * 0.05
        total = subtotal +tax

        print(f"\nOrder for {name}:")
        apples_count = 0
        grapes_count = 0
        oranges_count = 0

        for item in order_summary:
            if 'Apple' in item:
                apples_count += 1
            elif 'Grape' in item:
                grapes_count += 1
            elif 'Orange' in item:
                oranges_count += 1

        if apples_count > 0:
            print(f"{apples_count} Apple(s) at ${fruit_prices[1]['price']} apiece")
        if grapes_count > 0:
            print(f"{grapes_count} Grape(s) at ${fruit_prices[2]['price']} apiece")
        if oranges_count > 0:
            print(f"{oranges_count} Orange(s) at ${fruit_prices[3]['price']} apiece")

        print(f"Subtotal: ${subtotal:.2f}")
        print(f"5% Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")

        break
    try:
        selection = int(selection)
        if selection in fruit_prices:
            item = fruit_prices[selection]
            running_total += item['price']
            order_summary.append(f"1 {item['name']} at ${item['price']} each")
            print(f"You bought 1 {item['name']} at ${item['price']}.")

            choice = input("Would you like to buy another piece of fruit? Y or N: ").strip().upper()
            if choice == 'Y':
                print(f"Welcome {name}. Which fruit would you like to buy?")
                for key, value in fruit_prices.items():
                    print(f"{key}. {value['name']} ${value['price']}")
            elif choice == 'N':
                    continue
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        else:
            print("Invalid selection. Please choose a number from 1 to 3 or 'N' to checkout.")

    except ValueError:
        print("Invalid input. Please enter a number from 1 to 3 or 'N' to checkout.")

#Once they are done, Print "Order for {name}, separate line,
#1 apple(s) at $2 apiece
#etc
#subtotal: $5
#5% tax: $.25
#Total: $5.25