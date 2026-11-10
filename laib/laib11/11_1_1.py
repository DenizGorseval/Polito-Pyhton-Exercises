def num_ofwords(filename):
    word_dict = {}
    try:
        with open(filename, "r") as file:
            lines = [[word.strip(".,;:").lower() for word in line.split()] for line in file]
    except FileNotFoundError:
        print("Wrong file name entered")
        return()
    for line in lines:
        for word in line:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
    return word_dict

    



def main():
    filename = input("Enter the filename: ")
    word_count = num_ofwords(filename)
    for key,value in word_count.items():
        print(f"{key}: {value}")
main()