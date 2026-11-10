def main():
    file = open("/Users/denizgorseval/python 2.0/lecture/fileopen/input.txt", "r")
    sum = 0
    for line in file:
        value = float(line)
        sum = sum + value
    file.close()
    print("The sum is:", sum)
main()