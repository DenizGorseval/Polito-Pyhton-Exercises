def main():
    a = float(input("Enter a number: "))
    print("absolute value: ", absolute(a))

def absolute(x):
    if x < 0:
        return  -1 * x
    else:
        return x

main()