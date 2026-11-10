counter = 0
total = 0
even = 0
odd = 0
x = input("Enter an integer (leave blank to exit): ")
while x != "":
    x = int(x)
    total += x
    number = x
    if counter > 0:
        if number > max:
            max = number
        if number < min:
            min = number
    elif counter == 0:
        min = x
        max = x
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
    
    x = input("Enter an integer (leave blank to exit): ")
    counter += 1

print("total:", total)
print("minimum:", min)
print("maximum:", max)
print("number of evens:", even)
print("number of odds:", odd)
