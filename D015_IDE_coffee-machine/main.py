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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(dict_of_ingredients):
    """Loops through the ingredients and returns True if they are sufficient, False if not."""
    for ingredient in dict_of_ingredients:
        if dict_of_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def total_coins():
    """Returns the total value of the coins inserted."""
    print("Please insert coins")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.10
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Checks if the total money given by the user is enough to buy the drink. Returns True if yes, False if no."""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here's your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Removes the amount of ingredients from the resources based on the chosen drink."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕")


profit = 0
machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink_information = menu[choice]
        if is_resources_sufficient(drink_information["ingredients"]):
            payment = total_coins()
            if is_transaction_successful(payment, drink_information["cost"]):
                make_coffee(choice, drink_information["ingredients"])
