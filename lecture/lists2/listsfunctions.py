def readFloats():
    res = []
    input_str = input("Give me a number: ")
    while input_str != "":
        res.append(float(input_str))
        input_str = input("Give me a number: ")
    return res

def multiply(val, factor):
    for i in range(len(val)):
        val[i] = val[i] * factor
    #dont need a return becasue val == values and it changes the values variable

def printReversed(val):
    print("Your values in reverse are:")
    for x in val[::-1]:
        print(x, end= " ")
    



def main():
    values = readFloats()
    multiply(values,10)
    printReversed(values)

main()