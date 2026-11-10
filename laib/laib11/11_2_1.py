def dict_formed(filename):
    income_dict = {}
    try:
        with open(filename, "r") as file:
            lines = [line.strip().split("\t") for line in file]
    except FileNotFoundError:
        print("The file can not be opened")
        return()
    for line in lines:
        country_name = line[1].lower()
        income = line[2]
        income_dict[country_name] = income
    return income_dict





def main():
    filename = "rawdata_2004.txt"
    income_dict = dict_formed(filename)

    user_input = input("Enter a country name (type quit to terminate): ")
    user_input = user_input.lower()
    while user_input != quit and user_input in income_dict:
        print(user_input.capitalize(), income_dict[user_input])
        user_input = input("Enter a country name (type quit to terminate): ")
        user_input = user_input.lower()



main()