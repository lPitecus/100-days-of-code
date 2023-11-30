from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
    choice = input(f"Choose your drink ({menu.get_items()}): ")
    drink_object = menu.find_drink(choice)
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_on = False
    else:
        if coffee_maker.is_resource_sufficient(drink_object) and money_machine.make_payment(drink_object.cost):
            coffee_maker.make_coffee(drink_object)
        else:
            machine_on = False
