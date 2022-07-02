from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
maker = CoffeeMaker()
money_register = MoneyMachine()


while True:
    order_name = input(f"What would you like to order? {coffee_menu.get_items().rstrip('/')} \n").lower()

    if order_name == "off":
        break

    elif order_name == "report":
        maker.report()
        money_register.report()

    elif order_name in coffee_menu.get_items().split("/"):
        coffee_type = coffee_menu.find_drink(order_name)

        if maker.is_resource_sufficient(coffee_type):
            if money_register.make_payment(coffee_type.cost):
                maker.make_coffee(coffee_type)

