def discount(prices, is_pet):
    total = 0
    product_counter = 0
    discount_flag = False
    if True in is_pet:
        for i in is_pet:
            if is_pet[i] == False: #only sum the products
                product_counter += 1
                total += prices[i]
        if product_counter >= 5:
            discount_amount = ((total*20) / 100)
            return discount_amount
    else:
        discount_amount = 0
        return discount_amount

        



def main():
    price_input = input("Enter the price(to quit type '-1'): ")
    
    prices = []
    is_pet = []
    while price_input != "-1":
        pet_status = input("Enter 'Y' if it's an animal 'N' if it's not an animal: ")
        
        if pet_status == "Y":
            is_pet.append(True)
        else:
            is_pet.append(False)
        prices.append(float(price_input))
        price_input = input("Enter the price(to quit type '-1'): ")
    
    discount_amount = discount(prices, is_pet)
    print("You have this much discount:", discount_amount)
    

main()