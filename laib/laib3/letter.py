word = input("Enter a string: ")

if word.isalpha():
    print("Only contains letters")
    if word.isupper():
        print("All characters are uppercase")
    elif word.islower():
        print("All characters are lowercase")

if word.isdecimal():
    print("All characters are decimal numeric")

if word.isalpha():
    print("It contains only letters and digits")

if word[0].isupper():
    print("Starts with a capital letter")

if word[-1] == ".":
    print("it ends with a point")
    