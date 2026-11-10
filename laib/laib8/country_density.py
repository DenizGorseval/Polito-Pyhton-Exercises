def main():
    f = open("countries.txt", "r")
    f.readlines()
    for line in f:
        line.strip().split()
    f.close()
main()