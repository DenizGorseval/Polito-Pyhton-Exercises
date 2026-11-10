def main():
    card_PIN = "1234"
    answer = instructions(card_PIN)




def instructions(card_PIN):
    
    i = 0
    while i <= 3:
        PIN = input("Enter your PIN: ")
        if PIN == card_PIN:
            print("You entered the correct PIN")
            break
        elif PIN != card_PIN:
            print("You entered the wrong PIN")
    
        if i == 3:
            print("Your card is blocked")

        i += 1
        
    



main()
