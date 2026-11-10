def addTax(price, rate):
    tax = price * rate / 100
    # no affect outside the function
    price += tax

total = 10
addTax(total, 7.5)