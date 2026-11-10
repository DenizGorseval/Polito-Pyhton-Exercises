def swap_first_last(the_list):
    last = the_list[-1]
    the_list.pop()
    first = the_list[0]
    the_list.pop(0)
    the_list.insert(0, last)
    the_list.append(first)
    return the_list

def swap_the_list(the_list):
    last = the_list.pop()
    the_list.insert(0,last)
    return the_list

def replace_evens(the_list):
    for i in range(len(the_list)):
        if the_list[i] % 2 == 0:
            the_list[i] = 0

    return the_list

def larger_adjacent(the_list):
    for i in range(1,len(the_list)-1):
        if the_list[i-1] >= the_list[i+1]:
            the_list[i] = the_list[i-1]
        else:
            the_list[i] = the_list[i+1]

    return the_list

def delete_middle(the_list):
    if len(the_list) % 2 == 0:
        the_list.pop(len(the_list)//2)
        the_list.pop(len(the_list)//2)
    else:
        the_list.pop(len(the_list)//2)
    return the_list
        



def main():

    num = input("Enter a number: ")
    num_list = []
    while num != "":
        num_list.append(int(num))
        num = input("Enter a number: ")
    
    print("The unchanged version of the list:", num_list)
    num_list = swap_first_last(num_list)
    print("The last and first element swapped:", num_list)
    num_list = swap_the_list(num_list)
    print("all elements slided 1 position swapped:", num_list)
    num_list = replace_evens(num_list)
    print("all even elements replaced with a 0:", num_list)
    num_list = delete_middle(num_list)
    print("The middle removed", num_list)
    


main()
    