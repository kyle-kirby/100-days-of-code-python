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
money = 0

def give_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money:.2f}")

def enough_resources():
    for resource in MENU[choice]["ingredients"]:
        if resources[resource] < MENU[choice]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True

def process_coins():
    quarters = int(input("How many quarters?")) * .25
    dimes = int(input("How many dimes?")) * .10
    nickels = float(input("How many nickels?")) * .05
    pennies = float(input("How many pennies?")) * .01
    total_paid = quarters + dimes + nickels + pennies
    return total_paid

def check_amount_paid(total_paid):
    if total_paid < MENU[choice]["cost"]:
        print("Sorry, not enough money. You have been refunded")
        return False
    global money
    money += MENU[choice]["cost"]
    refund = total_paid - MENU[choice]["cost"]
    print(f"Here is ${refund:.2f} in change.")
    return True

def make_coffee():
    for resource in MENU[choice]["ingredients"]:
        resources[resource] -= MENU[choice]["ingredients"][resource]
    print(f"Here is your {choice} ☕. Enjoy!")


power_on = True
while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == "off":
        power_on = False
    elif choice == "report":
        give_report()
    else:
        if enough_resources():
            total = process_coins()
            if check_amount_paid(total):
                make_coffee()
