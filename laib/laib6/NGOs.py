def financial_aid(annual_income, children):
    
    while annual_income != -1 or children != -1:
        annual_income = int(input("Enter your annual income(type '-1' to exit): "))
        children = int(input("Enter the number of your children(type '-1' to exit): "))
    
        if (annual_income >= 30000 and annual_income <= 40000) and children >= 3:
            aid = 1000
        elif (annual_income < 30000 and annual_income >= 20000) and children >= 2:
            aid = 1500
        elif annual_income < 20000:
            aid = 2000
        
        print (aid)
    return aid


def main():
    annual_income = int(input("Enter your annual income: "))
    children = int(input("Enter the number of your children: "))
   
    aid_total = financial_aid(annual_income, children)
    print("Aid amount is:", aid_total)

main()