from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while on:
    order = input(f"What coffee would you like {menu.get_items()}? ")

    if order == "off":
        on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(order)
        if coffee:
            if coffee_maker.is_resource_sufficient(
                coffee
            ) and money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
