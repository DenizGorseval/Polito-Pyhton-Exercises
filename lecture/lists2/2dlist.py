map = []
n_rows = int(input("N. of rows: "))
n_cols = int(input("N. of cols: "))
for i in range(n_rows):
    row = []
    for j in range(n_cols):
        char = int(input(f"Enter a number for the position {i} row and {j} column: "))
        row.append(char)
    map.append(row)

for i in range(n_rows):
    for j in range(n_cols):
        print(map[i][j], end= " ")
    print()
