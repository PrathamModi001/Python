def money_input():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def material_enough(name):
    condition = False; water = False; milk = False; coffee = False
    if report["Water"] >= resources_req[name.title()]['ingrediants']['Water']:
        water = True
    if report["Milk"] >= resources_req[name.title()]['ingrediants']['Milk']:
        milk = True
    if report["Coffee"] >= resources_req[name.title()]['ingrediants']['Coffee']:
        coffee = True
    if water == True and milk == True and coffee == True:
        condition = True
    return condition

def usage(name):
    report["Water"] -= resources_req[name.title()]['ingrediants']['Water']
    report["Coffee"] -= resources_req[name.title()]['ingrediants']['Coffee']
    report["Milk"] -= resources_req[name.title()]['ingrediants']['Milk']
    report["Money"] += resources_req[name.title()]['Cost']

def material_present():
    print(f"Water: {report['Water']}ml")
    print(f"Milk: {report['Milk']}ml")
    print(f"Coffee: {report['Coffee']}g")
    print(f"Money: ${report['Money']}")

print("MENU:","\nEspresso", "\nLatte", "\nCappuccino")
print("You can also check the 'Report' of the available resources\n\n")
print("If you want to leave the Coffee Machine (which you totally shouldn't): press 'Quit'")


report = {
    "Water" : 300,
    "Milk" : 200,
    "Coffee" : 100,
    "Money" : 0
}

resources_req = {
    "Espresso" : {
        "ingrediants" : {
                "Water" : 50,
                "Coffee" : 18,
                "Milk" : 0
                },
        "Cost" : 1.5
    },
    
    "Latte" : {
        "ingrediants" : {
                "Water" : 200,
                "Coffee" : 24,
                "Milk" : 150
                },
        "Cost" : 2.5
    },
    
    "Cappuccino" : {
        "ingrediants" : {
                "Water" : 200,
                "Coffee" : 24,
                "Milk" : 100
                },
        "Cost" : 3
    },
}


run_machine = True
while run_machine:
    
    user = input("What would you like? ").lower()
    
    if user == "report":
        material_present()

    if user == "latte":
        money = money_input()
        if resources_req['Latte']['Cost'] < money:
            if material_enough(user):
                usage(user)
                print(f"Transaction Successful! Amount paid by the user: {money}")
                print(f"The due change: {money-resources_req['Latte']['Cost']}")
                print(f"Here You Go! Your {user} ☕️ is ready to serve!")
            else:
                print("Not enough Materials available. Sorry Comeback at a later time")
        else:
            print("Not Sufficient Coins")

    if user == 'quit':
        run_machine = False
        print("Thanks for using our machine! ❤")

