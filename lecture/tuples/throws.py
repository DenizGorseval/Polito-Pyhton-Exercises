def readThrows():
    res = []
    input_str = input("Give me the dice value: ")
    while input_str != "":
        x = int(input_str)
        if x < 1 or x > 6:
            print("Error: invalied dice value")
        else:
            res.append(x)
        input_str = input("Give me the dice value: ")
    return res

def computeStats(throws):
    counters = [0] * 6
    for throw in throws:
        idx = throw - 1
        counters[idx] += 1
    return counters

def main():
    throws = readThrows()
    stats = computeStats(throws)
    print(stats)

main()