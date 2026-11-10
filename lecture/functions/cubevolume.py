def main():
    mySide = 3
    vol1 = cubevolume(mySide)
    print(vol1)

def cubevolume(sideLength):
    volume = sideLength ** 3
    return volume


main()