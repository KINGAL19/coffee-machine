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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True


def is_sufficient(drink_ingredients):
    for item in drink_ingredients:
        if resources[item] < drink_ingredients[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True


def process_coin():
    print('Please insert coins')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dims?: ')) * 0.1
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total


def is_transaction_successful(pay, drink_cost):
    if pay >= drink_cost:
        change = round(pay - drink_cost, 2)
        print(f'Here is your change ${change}')
        global profit
        profit += drink_cost
        return True
    else:
        print('There is not enough money.')
        return False


def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f'Here is your {drink_name}')


while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
