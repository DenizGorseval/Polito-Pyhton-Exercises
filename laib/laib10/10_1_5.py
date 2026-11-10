def sum_list(num_list):
    total = 0
    for num in num_list:
        total += num
    print("Total sum:", total)

def main():
    num_list = []
    attempts = 0

    while True:
        if attempts >= 3:
            print("3 wrong attempts reached. Program terminates.")
            break

        user_input = input("Enter a float number (or empty to finish): ")

        if user_input == "":
            sum_list(num_list)
            break

        try:
            value = float(user_input)
            num_list.append(value)
        except ValueError:
            attempts += 1
            if attempts < 3:
                print(f"Wrong input! Try again. ({3 - attempts} attempts left)")
            
        
main()
