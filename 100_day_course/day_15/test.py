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


def resource_calculation(flavor):
    report={}
    report["water"]=resources["water"]-MENU[flavor]["ingredients"]["water"]
    report["milk"]=resources["water"]-MENU[flavor]["ingredients"]["milk"]
    report["coffee"]=resources["water"]-MENU[flavor]["ingredients"]["coffee"]
    print(report)

#print(resource_calculation("latte"))
print(resources["water"])