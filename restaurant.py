def main():
    #Define
    food = float(input("Please enter cost of food: "))
    drinks = float(input("Please enter cost of drinks: "))
    #Process
    cost_of_meal = float(food + drinks)
    tax = (.075)
    tip = (.18)

    tax_amount = float(cost_of_meal * tax)
    tip_amount = float(cost_of_meal * tip)
    total = (cost_of_meal + tax_amount + tip_amount)

    #Output
    print(f"Cost of meal: {cost_of_meal:.2f}$")
    print(f"Tax Amount: {tax_amount:.2f}$")
    print(f"Tip Amount: {tip_amount:.2f}$")
    print(f"Total: {total:.2f}$")
    


main()
