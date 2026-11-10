def main():
    filename = "names.txt"
    unique_names = []
    count = []
    try:
        with open(filename, "r") as file:
            for name in file:
                name = name.strip()

                if name in unique_names:
                    index = unique_names.index(name)
                    count[index] += 1
                else:
                    unique_names.append(name)
                    count.append(1)
                
        for i,name in enumerate(unique_names):
            print(f"{name}: {count[i]}")
            
                
                    
            
    except OSError:
        print("The file cannot be opened")
main()