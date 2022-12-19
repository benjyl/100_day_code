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
}

on = True
costs = [MENU[coffee]["cost"] for coffee in MENU]
print(costs)
print(f"What would you like? Espresso (${costs[0]:.2f}), Latte (${costs[1]:.2f}) or Espresso $({costs[2]:.2f})")
while on:
    # user = input(f"What would you like? Espresso (${costs[0]:.2f}), Latte (${costs[1]:.2f}) or Espresso $({costs[2]:.2f})")
    pass
