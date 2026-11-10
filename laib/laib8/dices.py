import random

def dice_rolls():
    dice_rolls = []
    for i in range(20):
        roll = random.randint(1,6)
        dice_rolls.append(roll)
    return dice_rolls

def longest_seq(dice_rolls):
    temp = dice_rolls[0]
    lenght_of_seq = 0
    max_length = 0
    for i in range(len(dice_rolls)):
        if dice_rolls[i] == temp:
            lenght_of_seq += 1
            if lenght_of_seq > max_length:
                max_length = lenght_of_seq
                start_index = (i-2)   
        else:
            lenght_of_seq = 1
            temp = dice_rolls[i]
        
    for i in range(len(dice_rolls)):
        if i == start_index:
            dice_rolls.insert(start_index, "(")
            last_num = start_index + max_length
            dice_rolls.insert(last_num + 1, ")")
    return dice_rolls
        


        


def main():
    dice_list = dice_rolls()
    last_list = longest_seq(dice_list)
    for i in last_list:
        print(i, end=" ")
    

main()