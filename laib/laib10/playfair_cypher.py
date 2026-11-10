import string

def formed_table(Key_word):

    table = []
    for row in range(5):
        row = []
        for col in range(5):
            row.append(None)
        table.append(row)

    Key_word = Key_word.upper()
    cypher_list= []
    for letter in Key_word:
        if letter not in cypher_list:
            cypher_list.append(letter)

    
    # appending the rest of the alphabet without the letter "J"
    alphabet = string.ascii_uppercase.replace("J", "")
    for letter in alphabet:
        if letter not in cypher_list:
            cypher_list.append(letter)

    i = 0
    for row in range(len(table)):
        for col in range(len(table[row])):
            table[row][col] = cypher_list[i]
            i += 1
    return table


def encryption(table, word):
    i = 0
    word = word.upper()
    encrypted_word = []

    if len(word) % 2 != 0:
        word = word + "Z"

    while i < len(word):
        first_cord = None
        sec_cord = None

        # first letter
        for row in range(len(table)):
            if word[i] in table[row]:
                for col in range(len(table[row])):
                    if word[i] == table[row][col]:
                        first_cord = (row, col)
                        i += 1
                        break
                break

        if i >= len(word):
            break

        # second letter
        for row in range(len(table)):
            if word[i] in table[row]:
                for col in range(len(table[row])):
                    if word[i] == table[row][col]:
                        sec_cord = (row, col)
                        i += 1
                        break
                break

        # encryption rule
        if first_cord[0] == sec_cord[0]:  # same row
            encrypted_word.append(table[first_cord[0]][sec_cord[1]])
            encrypted_word.append(table[sec_cord[0]][first_cord[1]])
        else:
            encrypted_word.append(table[first_cord[0]][sec_cord[1]])
            encrypted_word.append(table[sec_cord[0]][first_cord[1]])

    return encrypted_word



def decryption(table,word):
    pass


def main():
    Key_Word = input("Enter a key word for cyphering: ")
    table = formed_table(Key_Word)
    wanted = input("Enter the form of cypher 'encrypt or decrypt': ")
    
    if wanted == "encrypt" or wanted == "decrypt":
        word = input("Enter the word you want to encrypt or decrypt: ")
        encrypted_word = encryption(table, word)
        print("".join(encrypted_word))
    
    else:
        raise ValueError("Wrong Input")

main()