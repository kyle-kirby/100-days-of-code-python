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
    "money": 0,
}


def choice():
    """Takes input from user as instruction for the machine"""
    decision = input("What would you like? (espresso/latte/cappuccino): ")
    return decision

def report(resources_available):
    """Produces report of remaining ingredients and money earned"""
    resource_water = resources_available["water"]
    resource_milk = resources_available["milk"]
    resource_coffee = resources_available["coffee"]
    resource_money = resources_available["money"]
    print(f"Water: {resource_water}ml")
    print(f"Milk: {resource_milk}ml")
    print(f"Coffee: {resource_coffee}g")
    print(f"Money: ${resource_money:.2f}")

def input_coins():
    """Takes user payment in coins and returns their total"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickel?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

def task(decision):
    """Logic for Coffee Machine"""
    if decision == "report":
        report(resources)
        task(choice())
    elif decision == "off":
        print("Machine off, ready for maintenance.")
        return
    elif decision == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            drink_total = input_coins()
            if drink_total >= MENU["espresso"]["cost"]:
                resources["money"] += MENU["espresso"]["cost"]
                change = drink_total - MENU["espresso"]["cost"]
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                print(f"Here is ${change:.2f} in change.")
                print("Here is your espresso ☕ Enjoy! ")
            else:
                print("Sorry that's not enough money. Money refunded")
        elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        task(choice())
    elif decision == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= \
                MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            drink_total = input_coins()
            if drink_total >= MENU["latte"]["cost"]:
                resources["money"] += MENU["latte"]["cost"]
                change = drink_total - MENU["latte"]["cost"]
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                print(f"Here is ${change:.2f} in change.")
                print("Here is your latte ☕ Enjoy! ")
            else:
                print("Sorry that's not enough money. Money refunded")
        elif resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        task(choice())
    elif decision == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= \
                MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            drink_total = input_coins()
            if drink_total >= MENU["cappuccino"]["cost"]:
                resources["money"] += MENU["cappuccino"]["cost"]
                change = drink_total - MENU["cappuccino"]["cost"]
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                print(f"Here is ${change:.2f} in change.")
                print("Here is your cappuccino ☕ Enjoy! ")
            else:
                print("Sorry that's not enough money. Money refunded")
        elif resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        task(choice())


task(choice())
