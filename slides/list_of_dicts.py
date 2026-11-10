def extract_record(filename):
    record = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                countries = []
                if line != "":
                    line = line.strip().split(":")
                    record["Country"] = line[0]
                    record["Population"] = int(line[1])
                    countries.append(record)
        return countries
    except OSError:
        print("There was a problem with your code")
        
    
    




def main():
    filename = "country_pop.txt"
    countries = extract_record(filename)
main()