menu = {
    "Maggi" : 50,
    "Pasta" : 40,
    "Sandwitch" : 60,
    "Burger" : 70,
    "Pizza" : 110,
    "Frenki" : 30
}

print("welcome to our PY Restaurant.")
print("Maggi        50/-\nPasta        40/-\nSandwitch    60/-\nBurger       70/-\nPizza       110/-\nFrenki       30/-")

Item = input("What whould you like to eat - ").capitalize()
total_item = 0
while True:
    if Item in menu:
        print("Your",Item,"is added successfully in your order list")
        total_item += menu[Item]
        add_order = input("Would you like to order something ? (Yes/No) - ").capitalize()
        if add_order == "Yes":
            Item = input("What whould you like to eat - ").capitalize()
            
        else:
            print("-------------------------------")
            print("Your Bill amount is ",total_item,"Rupees")
            print("-------------------------------")
            print("\tThank You ")
            break
    else:
        print("we can't serve you item")
        break
