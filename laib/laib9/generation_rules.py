
def increasing_order():
    l = []
    for i in range(10):
        l.append(i+1)
    return l
def inc_timestwo():
    l = []
    for i in range(11):
        l.append(i*2)
    return l
def index_squared():
    l = []
    for i in range(10):
        l.append((i+1)**2)
    return l
def all_zeros():
    l = []
    for i in range(10):
        l.append(i*0)
    return l




def main():
    increasing_order()
    inc_timestwo()
    index_squared()
    all_zeros()

main()