import random

marbles = random.randint(10,100)
starter = random.randint(0,1)
smartness = random.randint(0,1)

print("The number of marbles: ", marbles)
counter = 0
if starter == 0: #computer starts
    print("Computer starts")
    while marbles > 0:
        if smartness == 0: #stupid
            print("stupid mode")
            taken = random.randint(1,marbles//2)
            marbles -= taken
            print("Remaining marbles: ", marbles)
        elif smartness == 1: #intelligent
            print("Inteligent mode")
            for num in range(1,(marbles//2)):
                if (marbles - num) == 7 or (marbles - num) == 15 or (marbles - num) == 31 or (marbles - num) == 63:
                    marbles -= num
                    print("Remaining marbles: ", marbles)
                    break
        player = int(input("Enter the number of marbles to be removed: "))
        marbles -= player
    
    
elif starter == 1: #player starts
    player = int(input("Enter the number of marbles to be removed: "))
    marbles -= player
    while marbles > 0:
        if smartness == 0: #stupid
                print("stupid mode")
                taken = random.randint(1,marbles//2)
                marbles -= taken
                print("Remaining marbles: ", marbles)
        elif smartness == 1: #intelligent
             print("Inteligent mode")
             for num in range(1,(marbles//2)):
                if (marbles - num) == 7 or (marbles - num) == 15 or (marbles - num) == 31 or (marbles - num) == 63:
                    marbles -= num
                    break
                    print("Remaining marbles: ", marbles)
