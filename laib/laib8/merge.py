def merge(a,b):

    min_length = min(len(a),len(b))
    merged_list = []
    for i in range(min_length):
        merged_list.append(a[i])
        merged_list.append(b[i])
    if len(a) > len(b):
        for k in range(i+1,len(a)):
            merged_list.append(a[k:])
    elif len(b) > len(a):
        for k in range(i+1,len(b)):
            merged_list.append(b[k])
    return merged_list



def main():
    a = [1, 4, 9, 16]
    b = [9, 7, 4, 9, 11]
    merged_list = merge(a,b)
    print(merged_list)

main()