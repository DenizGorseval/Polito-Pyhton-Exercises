def main():
    number = int(input("Enter a number: "))
    answer = primes(number)

def primes(number):
    i = 2
    while number > 1:
        if number % i == 0:
            number = number / i
            print(i)
        else: 
            i += 1
    

    



main()