from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
   

    menu = Menu()
    coffeemake = CoffeeMaker()
    moneymachine= MoneyMachine()

    is_on = True
    while is_on:
        options=menu.get_items()
        choice=input(f"What would you like? {options}:")
        print(choice)
        #menu.get_items(choice)
        if choice == "report":
            coffeemake.report()
            moneymachine.report()
        elif choice == "off":
            is_on = False
        elif choice== "latte" or choice =="espressor" or choice == "cappuccino":
            #?
            drink = menu.find_drink(choice)
            print(drink)
            if coffeemake.is_resource_sufficient(drink)== True:
                if moneymachine.make_payment(drink.cost) == True:
                    coffeemake.make_coffee(drink)


main()