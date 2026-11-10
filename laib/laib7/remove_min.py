import random

def remove_min(v):
    
    v.sort()
    return v


def rand_list():
    counter = 0
    num_list = []
    while counter < 10:
        num = random.randint(1,100)
        num_list.append(num)
        counter += 1
        num = 0
    return num_list

def main():
    v = rand_list()
    min_removed = remove_min(v)
    print(min_removed[1::])
main()
