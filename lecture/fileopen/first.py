def main():
    file = open("/Users/denizgorseval/python 2.0/lecture/fileopen/input.txt", "r")
    line = file.readline()
    sum = 0
    while line != "":
        value = float(line.strip())
        sum = sum + value
        line = file.readline()
    print(value)
    file.close()
main()