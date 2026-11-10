number = int(input("Enter a number: "))

if number < 2:
    print("none of them are prime")

for i in range(2, number + 1):
    isprime = True
    for k in range(2, i):
        if i % k == 0:
            isprime = False
            break
    if isprime:
        print(i)
