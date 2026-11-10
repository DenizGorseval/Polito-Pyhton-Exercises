def read_numbers(filename):
    try:
        with open(filename, "r") as file:
            numbers = [number.strip() for number in file]
    except OSError:
        print("The file cannot be opened")

    return numbers



def main():
    filename = "numbers.txt"
    outfile = "armstrong.txt"
    numbers = read_numbers(filename)
    armstrong_list = []
    for number in numbers:
        length = len(number)
        armstrong_check = 0
        for digit in number:
            armstrong_check += int(digit)**length
        if armstrong_check == int(number):
            armstrong_list.append(number)
            
        
    try:
        with open(outfile, "w") as file:
            for num in armstrong_list:
                file.write(num)
                file.write("\n")
    except OSError:
            print("There was an error")       


main()