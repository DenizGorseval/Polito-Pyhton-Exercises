


def Roman_to_decimal(s):
    total = 0
    while s != "":
        val_first = Roman_rep(s[0])
        if len(s) > 1:
            val_second = Roman_rep(s[1])
        if len(s) == 1 or val_first >= val_second:
            total += val_first
            s = s[1:]
        else:
            diff = val_second - val_first
            total += diff
            s = s[2:]
    return total
    
def Roman_rep(s):
    value = 0
    if s == "M":
        value += 1000
    elif s == "C":
        value += 100
    elif s == "L":
        value += 50
    elif s == "X":
        value += 10
    elif s == "V":
        value += 5
    elif s == "I":
        value += 1
    else:
        print("You didn't enter a roman number")
    
    return value

def main():
    string = input("Enter a Roman number: ")
    answer = Roman_to_decimal(string)
    print(answer)
main()
