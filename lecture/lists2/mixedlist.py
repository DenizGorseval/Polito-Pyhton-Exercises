def main():
    a = [1, 4, 9, 16]
    b = [9, 7, 4, 9, 11, 2]

    res = []

    #1)fill the begining of the res list 
    #alternating the element from a and b
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        res.append(a[i])
        i += 1
        res.append(b[j])
        j += 1

    if i < len(a):
        while i < len(a):
            res.append(a[i])
            i += 1
    elif j < len(b):
        while j < len(b):
            res.append(b[j])
            j += 1

    print(res)
    #2)complete res adding the remaining elements 
    #of the longest of the two lists


main()