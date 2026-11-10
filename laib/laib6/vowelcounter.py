def main():
    word = input("Enter a string to learn how many vowels: ")
    num = num_of_vowels(word)
    print(num)

def num_of_vowels(word):
    vowels = "aeiou"
    counter = 0
    for i in word.lower():
        if i in vowels:
            counter += 1
    return counter




main()