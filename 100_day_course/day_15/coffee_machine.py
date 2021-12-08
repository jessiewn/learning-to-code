MENU = {
    "espresso": {
        "ingredients": {
            "milk":0,
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
    "money":0
}



def check_resource(flavor):
    if MENU[flavor]["ingredients"]["water"]>resources["water"]:
        print('Sorry there is not enough water.')
        return False
    if MENU[flavor]["ingredients"]["milk"]>resources["milk"]:
        print('Sorry there is not enough milk.')
        return False
    if MENU[flavor]["ingredients"]["coffee"]>resources["coffee"]:
        print('Sorry there is not enough milk.')
        return False
    else:
        return True
def process_coins(flavor):
    print("Please insert coins.\n")
    quaters=int(input("how many quarters?: "))
    dimes=int(input("hom many dimes?: "))
    nickles=int(input("how many nickles?: "))
    pennies=int(input("how many pennies?: "))
    total=quaters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
    print(f'your total is {total:.2f}')
    if total<MENU[flavor]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if total>MENU[flavor]["cost"]:
        charge=total-MENU[flavor]["cost"]
        print(f"Here is ${charge:.2f} dollars in change.")
        return total
    if total==MENU[flavor]["cost"]:
        return total
def make_coffee(flavor):
    resources["water"]-=MENU[flavor]["ingredients"]["water"]
    resources["milk"]-=MENU[flavor]["ingredients"]["milk"]
    resources["coffee"]-=MENU[flavor]["ingredients"]["coffee"]
    resources["money"]+=MENU[flavor]["cost"]
    
def main():
    while True:

        ask=input('What would you like? (espresso/latte/cappuccino):')
        if ask == 'report':
            print(f"water: {resources['water']}ml")
            print(f"milk: {resources['milk']}ml")
            print(f"coffe: {resources['coffee']}g")
            print(f"money: ${resources['money']}")
        elif ask=='latte' or ask=='espresso' or ask=='cappuccino':
            if check_resource(ask)==True:
                if process_coins(ask)!=False:
                    make_coffee(ask)
                    print(f"here is your {ask}☕️,please enjoy it")
        elif ask == "off":
            return
main()

