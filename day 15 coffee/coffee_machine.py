MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}


def check_res(resources, MENU, coffee_type):
    for key, val in MENU[coffee_type]["ingredients"].items():
        if val > resources[key]:
            print(f"Sorry, there is not enough {key}")
            return False
    return True


def check_user_input(coins):
    while True:
        try:
            integer = int(input(f"how many {coins}?"))
            return integer
        except ValueError:
            print(f"Please insert a valid number of {coins}")


def coins_input():
    print("Please insert coins")
    quarters = check_user_input("quarters")
    nickels = check_user_input("nickels")
    dimes = check_user_input("dimes")
    pennies = check_user_input("pennies")
    total_paid = 0.25*quarters + 0.1*nickels + 0.05 * dimes + 0.01 * pennies
    return total_paid


def update_resources(resources, coffee):
    for key, val in MENU[coffee]["ingredients"].items():
        resources[key] -= val
    return resources


on = True
costs = [MENU[coffee]["cost"] for coffee in MENU]
options = ["espresso", "latte", "cappuccino", "off", "report"]

while on:
    user = input(
        f"What would you like? Espresso (${costs[0]:.2f}), Latte (${costs[1]:.2f}) or Cappuccino $({costs[2]:.2f})?").lower()

    if user not in options:
        print("Invalid option, retry")
    elif user == "off":
        on = False
    elif user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['profit']}")
    else:
        suff_res = check_res(resources, MENU, user)
        if suff_res:
            payment = coins_input()
            coffee_cost = MENU[user]["cost"]
            if payment >= coffee_cost:
                resources["profit"] += coffee_cost
                resources = update_resources(resources, user)
                if payment > coffee_cost:
                    change = payment - coffee_cost
                    print(f"Here is ${change:.2f} change")
                print(f"Here is your {user}. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded")
