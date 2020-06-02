money = 50
shopping_cart = []

fruits = {"Apple": 5, "Raspberry": 10, "Lemon": 20}
i = True
while i:
    if money <= 0:
        print("[+]----------------------[+]")
        print("Here is your cart: ")

        print(shopping_cart)
        print("You are out of money: ")
        money = abs(money)
        print('You owe :' + str(money))
        print("[+]----------------------[+]")

        break
    else:
        print(fruits)
        players_choice = input('What would you like?').title()
        if players_choice in fruits:
            shopping_cart.append(players_choice)
            money -= fruits[players_choice]
            print('You have this amount of money : ' + str(money))

        else:
            print("Sorry Not on the menu")