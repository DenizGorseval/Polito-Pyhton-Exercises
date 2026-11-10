def main():

    filename = "names.txt"
    names_dict = {}
    try:
        with open(filename, "r") as file:
            for name in file:
                name = name.strip()
                if name not in names_dict:
                    names_dict[name] = 1
                else:
                    names_dict[name] += 1
        
        for name,apperance in names_dict.items():
            print(f"{name}: {apperance}")
            
    except OSError:
        print("The file can not be opened")

main()