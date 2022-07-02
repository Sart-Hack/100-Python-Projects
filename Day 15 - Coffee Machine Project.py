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


def prompt():
    prompt = input("What coffee would you like? (espresso/latte/cappuccino) \n"
                   "Enter Menu to display the Menu.\n")

    return prompt.lower()


def menu(MENU):
    for key in MENU.keys():
        print(key.upper() + " - $" + str(MENU[key]["cost"]))


def report(resources, money):
    print(f'Water: {resources["water"]}ml ')
    print(f'Milk: {resources["milk"]}ml ')
    print(f'Coffee: {resources["coffee"]}gm ')
    print(f"Money: ${money}")


def is_sufficient_resources(coffee_type, MENU, resources):
    is_sufficient = True
    for key in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][key] > resources[key]:
            print(f"Sorry there isn't enough {key}")
            is_sufficient = False
    return is_sufficient

def process_coins(): # returns the amount of money entered
    quarters = int(input("Enter number of quarters\n")) * 0.25
    dimes = int(input("Enter number of dimes\n")) * 0.10
    nickles = int(input("Enter number of nickles\n")) * 0.05
    pennies = int(input("Enter number of pennies\n")) * 0.01
    return quarters + dimes + nickles + pennies


def is_enough_money(MENU, prompt, money): # Check if enough money for the drink and returns profit
    money_entered = process_coins()
    excess_money = round((money_entered - MENU[prompt]["cost"]),2)
    if excess_money < 0:
        print("Sorry, That's not enough money. Money refunded.")
        return [False, money]
    elif excess_money > 0:
        print(f"Here is ${excess_money} in change.")
    return [True, (money + MENU[prompt]["cost"])]


def make_coffee(prompt, MENU, resources):
    for key in MENU[prompt]["ingredients"]:
        resources[key] -= MENU[prompt]["ingredients"][key]
    return resources


while True:
    user_prompt = prompt()

    if user_prompt == "off":  # This is for the maintainers
        break

    elif user_prompt == "report":  # This is for the maintainers
        report(resources, money)

    elif user_prompt == "menu":
        menu(MENU)

    elif user_prompt in ["latte", "cappuccino", "espresso"]:
        if is_sufficient_resources(user_prompt, MENU, resources):
            condition, money = is_enough_money(MENU,user_prompt,money)
            if condition:
                resources = make_coffee(user_prompt, MENU, resources)
                print(f'Here is your {user_prompt}. Enjoy!')



