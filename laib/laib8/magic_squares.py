def input_square():
    num = 0
    counter = 0

    square = []
    size = 4
    for i in range(size):
        rows = []
        for j in range(size):
            if num != "" and counter <= 16:
                num = int(input("Enter a number: "))
                counter += 1
                rows.append(num)
        print(f"{rows} \n {counter} numbers entered")
        square.append(rows)
    return square
        

def check_magic(square):
    magic_sum = sum(square[0])  # referans toplam

    # satır kontrol
    for row in square:
        if sum(row) != magic_sum:
            return False

    # sütun kontrol
    for col in zip(*square):
        if sum(col) != magic_sum:
            return False

    # diagonal 1
    left_diag = 0
    for i in range(4):
        left_diag += square[i][i]
    if left_diag != magic_sum:
        return False

    # diagonal 2
    right_diag = 0
    for i in range(4):
        right_diag += square[i][3-i]
    if right_diag != magic_sum:
        return False

    

    return True


                    


                







def main():
    square = input_square()
    for i in square:
        print(i)
    answer = check_magic(square)
    if answer:
        print("This is a magic square")
    else:
        print("This is not a magic square" )


main()