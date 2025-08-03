from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


order = Menu()
resources = CoffeeMaker()
money = MoneyMachine()

power_on = True
while power_on:
    drink_choice = input(f"What would you like? ({order.get_items()}): ")
    if drink_choice == "off":
        power_on = False
    elif drink_choice == "report":
        resources.report()
        money.report()
    else:
        drink = order.find_drink(drink_choice)
        if resources.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                resources.make_coffee(drink)
