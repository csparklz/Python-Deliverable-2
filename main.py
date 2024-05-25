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
        for item in order_summary:
            print (item)
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