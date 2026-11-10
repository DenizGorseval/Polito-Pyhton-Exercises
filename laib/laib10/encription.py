import string
def secret_dict(key_word):
    decryption_dict = dict()
    encryption_dict = {}

    #forms the alphabet
    alphabet_temp = []
    alphabet_list = []
    for i in string.ascii_uppercase:
        alphabet_temp.append(i)
        alphabet_list.append(i)
    
        

    # this adds every letter once in a list
    for letter in key_word:
        if letter not in decryption_dict:
            decryption_dict[letter.upper()] = None
    
    # removes the letter if its in the alphabet
    for letter in decryption_dict:
        alphabet_temp.remove(letter)
    
    # F E A T H R Z Y X W V U S Q P O N M L K J I G D C B this is formed 
    for i in range(len(alphabet_temp)-1,-1,-1):
        decryption_dict[alphabet_temp[i]] = None
        # F E A T H R Z Y X W V U S Q P O N M L K J I G D C B this is formed 
    
    for i, letter in enumerate(decryption_dict):
        decryption_dict[letter] = alphabet_list[i]
    
    for i, letter in enumerate(decryption_dict):
        encryption_dict[alphabet_list[i]] = letter

    
    return encryption_dict,decryption_dict


def encryption(filename, encryption_dict):
    encrypted_words = []
    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file]
    except OSError:
        print("The file can not be opened")

    for line in lines:
        for char in line.upper():
                if char.upper() in string.ascii_uppercase:
                    encrypted_words.append(encryption_dict[char])
                else:
                    encrypted_words.append(char)
            
    print(f"The encrypted version is: {encrypted_words}")



def decryption(filename, decryption_dict):
    decrypted_words = []
    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file]
    except OSError:
        print("The file can not be opened")
    for line in lines:
        for word in line:
            for letter in word:
                if letter.upper() in string.ascii_uppercase:
                    decrypted_words.append(decryption_dict[letter])
                else:
                    decrypted_words.append(letter)
            
    print("The encrypted version is" + "".join(decrypted_words))


        

def main():
    filename = input("Enter a the file name: ")
    user_request = input("Enter your request(encrypt or decrypt): ")
    key_word = input("Enter the key word: ")
    encryption_dict, decryption_dict = secret_dict(key_word)
    if user_request == "encrypt":
        encryption(filename, encryption_dict)
    elif user_request == "decrypt":
       decryption(filename, decryption_dict)
    else:
        raise ValueError("Wrong input! ")
main()