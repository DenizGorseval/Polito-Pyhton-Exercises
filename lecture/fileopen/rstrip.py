def main():
    f = open("input.txt", "r")
    for l in f:
        l = l.rstrip()
        words = l.split()
        for w in words:
            print(w.rstrip(',.!;:'))

    f.close()

main()