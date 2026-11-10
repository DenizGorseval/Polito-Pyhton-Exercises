
def parking_order(car_park):
    for _ in range(len(car_park)):
        # --- en uzun boşluğu bul ---
        space = 0
        max_start = 0
        max_space = 0
        start = 0
        for i in range(len(car_park)):
            if car_park[i] == False:
                if space == 0:
                    start = i
                space += 1
            else:
                if space > max_space:
                    max_space = space
                    max_start = start
                space = 0
        # listenin sonunda biten boşluk için de kontrol et
        if space > max_space:
            max_space = space
            max_start = start

        # --- ortayı yerleştir ---
        mid = max_start + (max_space // 2)
        car_park[mid] = True

        # --- yazdır ---
        last_list = []
        for k in range(len(car_park)):
            if car_park[k] == True:
                last_list.append("X")
            else:
                last_list.append("_")
        print(" ".join(last_list))
        print()

    
        

def main():
    parking_lot = list()
    space = int(input("Enter the number of parking spaces: "))
    for i in range(space):
        parking_lot = [False] * 10
    answer = parking_order(parking_lot)
main()