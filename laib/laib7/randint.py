import random



def rand_list():
    counter = 0
    num_list = []
    while counter < 10:
        num = random.randint(1,100)
        num_list.append(num)
        counter += 1
        num = 0
    return num_list

def even_index(num_list):
    even_list = []
    for i in range(len(num_list)):
        if i % 2 == 0:
            even_list.append(num_list[i])
    
    return even_list

def even_value(num_list):
    even_values = []
    for i in num_list:
        if i % 2 == 0:
            even_values.append(i)
    
    return even_values

def reverse_order(num_list):
    new_list = num_list[::-1]
    return new_list

def first_last(num_list):
    first = num_list[0]
    last = num_list[-1]
    return first, last

def main():
    num_list = rand_list()
    even_i = even_index(num_list)
    even_val = even_value(num_list)
    reverse = reverse_order(num_list)
    first, last = first_last(num_list)
    
    print("The even index numbers: ", *even_i)
    
    print("The even valued number: ", *even_val)
    
    print("The reverse order of the numbers: ", *reverse)

    print("The first and last elements: ", first, last)

main()

