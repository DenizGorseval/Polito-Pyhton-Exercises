
def count_words(string):
    counter = 1
    space_counter = 0
    for i in string:
        if i == " " and space_counter < 1:
            counter += 1
            space_counter += 1
        elif i != " " and space_counter > 1:
            space_counter = 0
            
        
    
    return counter

def main():
    input_str = input("Enter a string: ")
    word_counter = count_words(input_str)
    print(word_counter)


main()