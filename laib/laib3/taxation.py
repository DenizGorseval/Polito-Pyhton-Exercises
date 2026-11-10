income = int(input("Enter your income: "))
status = input("Enter your martial status ('unmarried or married'): ")

if status == "unmarried":
    if income <= 8000:
        tax = income * (10/100)
        income = income - tax
    elif income > 8000 and income <= 32000:
        tax = income * 15/100
        tax = tax + 800

