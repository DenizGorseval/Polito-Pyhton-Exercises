def same_set(a,b):
    check_list = []
    flag = True
    counter = 0
    for i in a:
        if i not in check_list:
            check_list.append(i)
    for k in b:
        if k not in check_list:
            flag = False
            break
    for i in check_list:
        if i not in b:
            flag = False
            break
    return flag

def main():
    num_list = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    num_list2 = [11, 11, 7, 9, 16, 4, 1]
    num_list3 = [1, 4, 9, 16, 7, 4]

    answer = same_set(num_list,num_list3)
    print(answer)
main()