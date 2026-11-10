def reverse_order(inputfile, outputfile):
    try:
        with open(inputfile, "r") as in_file:
            with open(outputfile, "w") as out_file:
                lines = []
                for line in in_file:
                    lines.append(line.strip())
                for i,line in enumerate(lines):
                    out_file.write(f"{lines[3-i]}\n")
                    


    except OSError:
        print("The file cannot be opened")

def main():
    input_file = "input.txt"
    output_file = "output.txt"
    reverse_order(input_file, output_file)

main()