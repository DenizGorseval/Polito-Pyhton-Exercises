def main():
    f = open("numbers.txt", "w")
    for i in range(1,11):
        f.write(f"{2*i}\n")#this needs newline
        print(2*i, file=f, end=)#this does not need newline
    f.close()
main()