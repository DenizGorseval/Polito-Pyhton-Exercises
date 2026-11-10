def get_initials(n):
    initials = ""
    for elem in n:
        initials = initials + elem[0]
    return initials

def all_upper(n):
    new_list = []
    for i in n:
        new_list.append(i.upper())
    return new_list

def main():
    names = ["Alice", "Bob", "Carl"]
    initials = get_initials(names)
    print(initials)
    print(all_upper(names))

main()