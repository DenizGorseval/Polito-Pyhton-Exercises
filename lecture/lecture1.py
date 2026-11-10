MAX_NUMBER = 10
MAX_EXPONENT = 4

print("Table: ")

for x in range(1,MAX_NUMBER + 1):
    for n in range(1,MAX_EXPONENT + 1):
        print(f"{x**n:10}", end="|")

