#Welcome & ask user their name?

print("Welcome to GC Fruit Market!")
name = input("What is your name? ")
print("Welcome " + name + "." " Which fruit would you like to buy?")

# Display a list of different fruit with prices
#Apple $2
#Grape $1
#Orange $3
fruit_choice=['1. Apple $2', '2. Grape $1', '3. Orange $3']
for item in fruit_choice:
    print(item)

selection = input("Enter the number of your choice: ")
(selection) = int(selection)

if selection == 1:
    print("You bought 1 apple at $2")
elif selection == 2:
    print("You bought 1 grape at $1.")
elif selection ==3:
    print("You bought 1 orange at $3.")

#Ask Again



#Once they are done, print how many of each fruit, along with the subtotal and the total cost