def main():
    try:
        filename = input("Enter filename: ")
        infile = open(filename, "r")
        line = infile.readline()
        value = int(line)
        print(value)
    except FileNotFoundError:
        print("I could not open the file")

    
    
main()