def two_d_list(rows,cols):
    table = []
    
    for row in range(rows):
        column = []
        for col in range(cols):
            column.append(0)
        table.append(column)
    print(table)
    return table

def form_ones(zeros):
    for row in zeros:
        for i in range(len(row)):
            row[i] = 1
    print(zeros)
    return zeros

def checkerboard(ones):
    for i,row in enumerate(ones):
        for el_i in range(len(row)):
            if i % 2 == 0:
                if el_i % 2 == 0:
                    ones[i][el_i] = 0
                else:
                    ones[i][el_i] = 1
            else:
                if el_i % 2 == 0:
                    ones[i][el_i] = 1
                else:
                    ones[i][el_i] = 0
    print(ones)
    return ones


def bottom_top(the_list):
    for i,row in enumerate(the_list):
        for el_i in range(len(row)):
            if i == 0 or i == len(row):
                the_list[i][el_i] = 0
                
    print(the_list)
    return(the_list)

def left_right(the_list):
    for i,row in enumerate(the_list):
        for element in range(len(row)):
            if element == 0 or element == (len(row)-1):
                the_list[i][element] = 1
    print(the_list)
    return the_list

def sum_all(the_list):
    total = 0
    for row in the_list:
        for elem in row:
            total += elem
    print("The sum is: ", total)
            

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    the_list = two_d_list(rows,cols)
    the_list = form_ones(the_list)
    the_list = checkerboard(the_list)
    the_list = bottom_top(the_list)
    the_list = left_right(the_list)
    sum_all(the_list)

main()