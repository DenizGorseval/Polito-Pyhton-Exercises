def dict_form(seq):
    seq_dict = {}
    for i,num in enumerate(seq):
        if num != 0:
            seq_dict[i] = num
    return seq_dict

def sparse_array_sum(a, b):
    last_seq = []
    
    for i in range(10):
        if i not in a or i not in b:
            last_seq.append(0)
        elif i in a and i in b:
            last_seq.append(a[i]+b[i])
        elif i in a:
            last_seq.append(a[i])
        elif i in b:
            last_seq.append(b[i])
        


 











def main():
    i = 0
    seq_1 = []
    seq_2 = []
    while i < 10:
        num = input("Enter a number for the first sequence: ")
        seq_1.append(int(num))

        num = input("Enter a number for the second sequence: ")
        seq_2.append(int(num))

        i += 1
    
    a = dict_form(seq_1)
    b = dict_form(seq_2)

    last_list = sparse_array_sum(a, b)
    for i in last_list:
        print(last_list[i], end=" ")
    

    

        

main()