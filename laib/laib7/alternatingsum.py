
def all_nums():
    num_list = []
    num = input("Enter a number: ")
    while num != "":
        num = int(num)
        num_list.append(num)
        num = input("Enter a number: ")

    return num_list

def sum(num_list):
    total = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            total += num_list[i]
        else:
            total -= num_list[i]
    
    return total

def main():
    num_list = all_nums()
    total = sum(num_list) 
    print(total)
    


main()