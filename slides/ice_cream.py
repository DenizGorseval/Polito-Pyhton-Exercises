import pprint
def dict_formed(filename, sells_dict):
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip().split(":")
                sells_dict[line[0]] = [line[1],line[2], line[3]]

    except OSError:
        print("There was a problem opening the file")


def main():
    filename = "icream.txt"
    sells_dict = {}
    dict_formed(filename, sells_dict)
    print(sells_dict)
main()