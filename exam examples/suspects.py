def read_customrnsuspect(customer_file,suspects_file):
    suspects = []
    customers_dict = {}
    suspects_dict = {}
    try:
        with open(customer_file,"r") as file:
            lines = [line.strip().split(",")for line in file]
    except OSError:
        print("The file cannot be opened")

    
    try:
        with open(suspects_file,"r") as file:
            names = [name.strip()for name in file]
    except OSError:
        print("The file cannot be opened")
    
    for name in names:
        suspects.append(name)
        
    for line in lines:
        name = line[0]
        duration = int(line[3]) - int(line[2])
        days_stayed = set()
        for i in range(int(line[2]),int(line[3])+1):
                days_stayed.add(i)
        if name not in suspects:
            phone_num = line[1]
            
            customers_dict[name] = [phone_num, days_stayed]
        else:
            suspects_dict[name] = days_stayed 

    return(suspects_dict,customers_dict)

def customer_suspects(suspects_dict,customers_dict):
    for sus_name, sus_days in suspects_dict.items():
        for cus_name in customers_dict:
            days_stayed = customers_dict[cus_name][1]
            print(f"** Contacts of the guest: {sus_name}: **")
            for day in sus_days:
                if day in days_stayed:
                    phone_num = customers_dict[cus_name][0]
                    print(f"Contact with {cus_name}, phone\n {phone_num}")
                    break
                    
                


                

def main():
    suspect_file = "suspects.txt"
    customer_file = "customers.txt"
    suspects_dict,customers_dict = read_customrnsuspect(customer_file,suspect_file)
    customer_suspects(suspects_dict,customers_dict)
    
main()