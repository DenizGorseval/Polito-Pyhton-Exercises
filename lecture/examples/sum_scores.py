def main():
    scores = []
    input_str = input(" ")
    while input_str != "":
        scores.append(float(input_str))
        input_str = input(" ")
    
    for i in range(2):
        m = min(scores)
        scores.remove(m)

    print("The sum of scores is: ", sum(scores))
main()