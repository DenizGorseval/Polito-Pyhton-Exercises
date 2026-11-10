def main():
    in_file = "exteremas.dat"
    out_file = "differences.dat"
    fin = open(in_file, "r")
    fout = open(out_file, "w")
    for line in fin:
        values = line.strip().split(',')
        first = int(values[0])
        second = int(values[1])
        diff = first - second
        print(diff, file= fout)
main()
