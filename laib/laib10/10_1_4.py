def service_spendings(filename):
    try:
        with open(filename, "r") as file:
            lines = [line.strip().split(";") for line in file]
    except OSError:
        print("The file could not be opened")
        return
    price_dict = {}
    for line in lines:
        if len(line) != 4:
            raise IndexError("one line has the length of values different than 4")
        service_type = line[1]

        try:
            price = float(line[2])
        except ValueError:
            raise ValueError("The price is not a float")
        
        if service_type not in price_dict:
            price_dict[service_type] = price
        else:
            price_dict[service_type] += price
        
    for key in price_dict:
        print(key, price_dict[key])
          

        

def main():
    input_file = "file.txt"
    service_spendings(input_file)

    
main()