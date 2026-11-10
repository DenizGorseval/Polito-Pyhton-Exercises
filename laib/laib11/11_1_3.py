def same_char(first, second):
    char_set = set()
    same_chars = set()
    different_chars = set()
    for char in first:
        char_set.add(char)
    for char in second:
        if char in char_set:
            same_chars.add(char)
        char_set.add(char)
        
    different_chars = set(char_set)
    for char in same_chars:
        different_chars.remove(char)
    



    print("Different characthers are: ", *different_chars)
    print("Same characthers are: ", *same_chars)

        


def main():
    first = input("Enter a string: ")
    second = input("Enter a second string: ")
    same_char(first, second)
    

main()
