#Display Menu
print("Welcome to Cornucopia's Dine and Dash!")

#This input entry triggers the entire system
entry = input("\nAre you ready to order?(Y/N): ").lower()

#The menu/list of all available food selections.
menu = {"pizza": 20.00,
        "burger":17.00,
        "bacon and eggs": 20.00,
        "waffles": 15.00,
        "sandwich": 5.00,
        "nachos": 4.00,
        "donut": 5.00,
        "hotdog": 10.00,
        "popcorn": 7.00,
        "french fries": 3.00,
        "onion rings": 5.00,
        "ice cream": 7.00,
        "crossiant": 8.00,
        "muffin": 5.00,
        "cupcake": 5.00,
        "cake": 20.00,
        "orange juice": 10.00,
        "milk": 3.00,
        "soda": 6.00,
        "latte": 5.00,
        "milkshake": 6.00,
        }

#This serves as the cart that all the items the user has chosen.
addtocart = []

#This def function displays the menu list.
def menulist():
     for key, value in menu.items():
                print(f"{key:15}: {value:.2f}")

#This is the main body of the program.
if entry == "y":
    print()
    menulist()
    print()
    #This while loop is active once the user presses "y" on the program.
    while entry == "y":
        #This block of code adds the item to the cart.
        food = input("Enter the food you would like to buy (Z to complete carting): ").lower()
        if food == "z":
               entry = "x"
        elif menu.get(food) is not None:
             addtocart.append(food)
    else:
         #Once the user is done carting and enters "z", the program wll print out the contents of the cart.
         print("\nDone!")
         print(addtocart)

         #This is the total calculation section, for each item in the cart, its value will be added to the total.
         total = 0
         for food in addtocart:
              total = total + menu.get(food)

         else:
              print("\nTotal is:", total)
        
         #This is the payment section. Here, you need to input your payment.
         payment = float(input("\nPlease input your payment amount: "))
         while True:
            if payment < total:
                 #This code block triggers where the payment is less than the total.
                 print("\nI'm sorry, it seems you inputted an insufficient amount of money, please try again.")
                 payment = float(input("\nPlease input your payment amount: "))
            
            else:
                 #If the payment is more than the total, this giant code block will then calculate your change.
                 change = payment - total
                 if change > 0:
                      #This code block will print out your change, and will greet you goodbye.
                      print("\nYour change is:", change)
                      print("\nThank you! Please come again!")
                      break
                 
                 else:
                      #This code block triggers when you have paid sufficiently.
                      print("\nYou gave the sufficient amount of money!")
                      print("\nThank you! Please come again!")
                      break

#If, for some reason, the user presses the other option (n), then this elif code block will activate.
elif entry == "n":
    while True:
        print("\nGoodbye then! Please come again if you desire to buy from our menu.")
        break

#if the user accidentally mistypes, the user must reset to try again :(.
else:
     print("\nError. Please reset the program to try again.")
          