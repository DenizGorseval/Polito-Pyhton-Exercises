def areandperimeter(side):
    area = side ** 2
    perimeter = 4*side
    return area, perimeter

mySide = float(input("Give the number of sides : "))
a, p = areandperimeter(mySide)
print("Area:", a)
print("Perimeter:", p)
