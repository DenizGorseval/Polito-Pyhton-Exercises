def main():
    output_filename = 'processed_numbers.txt'
    file = open("/Users/denizgorseval/python 2.0/lecture/fileopen/input_numbers.txt", "r")
    values = []
    for line in file:
        val = float(line.strip())
        values.append(val)
    file.close()
    

    fwrite = open(output_filename, "w")
    for val in values:
        fwrite.write(f'{val:.2f}\n')
    tot = sum(values)
    avg = tot / len(values)
    fwrite.write('-'*10 + "\n")
    fwrite.write(f'Total: {tot}\n')
    fwrite.write(f'Average: {avg}\n')


    fwrite.close()



main()