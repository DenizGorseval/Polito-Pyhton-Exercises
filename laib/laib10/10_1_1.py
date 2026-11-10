def read_input(inputfile, outputfile):
    with open(inputfile, "r") as in_file:
        with open(outputfile, "w") as out_file:
            for i,line in enumerate(in_file):
                line = line.strip()
                out_file.write(f"/*{i+1}*/{line}\n")
    


def main():
    input_file = "input.txt"
    output_file = "numerated_text.txt"
    read_input(input_file, output_file)

main()