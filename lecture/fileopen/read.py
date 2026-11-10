def main():
    
    f = open("mary.txt", "r")
    """
    short_text = f.read(10)
    while short_text != "":
        print(short_text)
        short_text = f.read(10)
    f.close()
    """
    lines = []
    for line in f:
        lines.append(line)
    
    f.close()
    print(lines)
main()