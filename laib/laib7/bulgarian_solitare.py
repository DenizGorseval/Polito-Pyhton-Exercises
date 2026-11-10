import random

def random_cards(random_list):
    num = 45
    temp = 0
    for i in range(0,5):
        piles = 5
        max_val = num - (piles - 1)
        if i == 4:
            random_list.append(num)
        else:
            temp = random.randint(1,max_val)
            random_list.append(temp)
        num = num - temp
    return random_list

def game(rand_list):
    steps = 0
    while rand_list != [1,2,3,4,5,6,7,8,9]:
        steps += 1
        new_pile = 0
        while 0 in rand_list:
            rand_list.remove(0)
        if rand_list == [1,2,3,4,5,6,7,8,9]:
            print(f"It took {steps} steps to finish the game")
            break
            
        for i in range(len(rand_list)):
            rand_list[i] = rand_list[i] - 1
            new_pile += 1
        rand_list.append(new_pile)
        print(rand_list)
        print()
    return rand_list

def main():
    random_list = []
    mod_list = random_cards(random_list)
    print(random_list)
    last_list = game(mod_list)
    print("The game is over", last_list)



main()