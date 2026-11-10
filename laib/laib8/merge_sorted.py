def merge_sorted(a,b):
    i = 0
    j = 0
    merge_sorted = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merge_sorted.append(a[i])
            i += 1
        else:
            merge_sorted.append(b[j])
            j += 1
    
    while i < len(a):
        merge_sorted.append(a[i])
        i += 1
    
    while j < len(b):
        merge_sorted.append(b[j])
        j += 1

    return merge_sorted





     
def main():
    a = [1, 4, 9, 16]
    b = [4, 7, 9, 9, 11]
    sorted_list = merge_sorted(a,b)
    print(sorted_list)
main()