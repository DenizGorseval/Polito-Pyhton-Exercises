def readCsv(filename):
    f = open(filename,"r")
    head = f.readline()
    header = head.split(",")
    table = []
    for line in f:
        fields = line.strip().split(",")
        table.append(fields)
    f.close()
    return table, header

def main():
    table, head = readCsv("data.csv")
    col_idx = 2
    print("The first column name is: ", head[0])
    print("And it contains:", end="")
    for record in table:
        print(record[col_idx], end=" ")


main()