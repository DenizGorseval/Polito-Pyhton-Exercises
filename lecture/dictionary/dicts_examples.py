def main():
    my_dictionary = {
        'Alice': [10,20,30],
        'Bob': [28,30,2],
        'Carl': [26,27,18,22]
    }
    contacts_dict = {}
    s_name = input("Give me a contact name: ")
    while s_name != "":
        s_num = input("Give me their phone number: ")
        try:
            num = int(s_num)
            contacts_dict[s_name] = num
        except ValueError:
            print(f"Invalid number {s_num}. Try Again...")
        s_name = input("Give me a contact name: ")


    s = input("Give me the person you want to know the result of: ")
    if s in contacts_dict:
        print(f"The phone number of {s} is {contacts_dict[s]}")
    else:
        print("I cannot find student ")

    for x in contacts_dict:
        print(x) # the key is printed

    for value in contacts_dict.values():
        print(value)
    for key, value in my_dictionary.items():
        print(key, value)
        
main()

