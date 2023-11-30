menu = {
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
    "water": 45,
    "milk": 200,
    "coffee": 100,
}


def money_given():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    return total


def check_water(water_at_moment, options, chosen_option):
    if water_at_moment >= options[chosen_option]["ingredients"]["water"]:
        water_at_moment -= options[chosen_option]["ingredients"]["water"]
        return water_at_moment
    else:
        print("There's not enough water")
        machine_on = False
        return machine_on

# contents inside the machine
water_amount = resources["water"]
milk_amount = resources["milk"]
coffee_amount = resources["coffee"]

machine_on = True

while machine_on:
    print(f"Water: {water_amount}ml\n"
          f"Milk: {milk_amount}ml\n"
          f"Coffee: {coffee_amount}ml")

    choice = input("What would you like? Espresso, latte or capuccino?: ").lower()
    if choice == "off":
        break
    price = menu[choice]["cost"]


    # remove ingredients from the machine based on the user choice
    if choice == "espresso":
        # TODO: If there are ingredients enough, ask for the user to insert coins.
        water_amount = check_water(water_amount, menu, choice)
        if coffee_amount >= 18:
            coffee_amount -= menu[choice]["ingredients"]["coffee"]
        else:
            print("There's not enough coffee")
            machine_on = False