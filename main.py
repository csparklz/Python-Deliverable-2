#Welcome & ask user their name?

print("Welcome to GC Fruit Market!")
name = input("What is your name? ")
print("Welcome, " + name + "." " Which fruit would you like to buy?")

# Display a list of different fruit with prices
#Apple $2
#Grape $1
#Orange $3

fruit_choice=['1. Apple $2', '2. Grape $1', '3. Orange $3']
for fruit in fruit_choice:
    print(fruit)
#Ask Again
while True:
    selection = input("Enter the number of your choice or 'N' to checkout: ")

    if selection == 'N':
        running_total =sum([2, 1, 3])
        print(f"Current running_total: ${running_total}")
        break
    try:
        selection = int(selection)
        if selection == 1:
            print("You bought 1 apple at $2")
        elif selection == 2:
            print("You bought 1 grape at $1.")
        elif selection ==3:
            print("You bought 1 orange at $3.")
        else:
            print("Invalid selection. Please choose a number from 1 to 3 or 'N' to checkout.")
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 3 or 'N' to checkout.")


#Once they are done, Print "Order for {name}, seperate line,
#1 apple(s) at $2 apiece
#etc
#subtotal: $5
#5% tax: $.25
#Total: $5.25