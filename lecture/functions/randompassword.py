from random import randint
from string import ascii_lowercase

def main():
    length = int(input("Desired password length: "))
    if length < 2: 
        print("Error: length must be >= 2")
    pwd = makePassword(length)
    
   
    print("Password:", pwd)

def makePassword(length):
    pwd = initPassword(length)
    random_num = randomCharacter("0123456789")
    pwd = insertAtRandom(pwd, random_num)
    random_sym = randomCharacter("%$£&/()=!")
    pwd = insertAtRandom(pwd, random_sym)
    return pwd

def initPassword(length):
    all_lowercase = "abcdefghij"
    pwd = ""
    for i in range(length):
        pwd = pwd + randomCharacter(all_lowercase)
    return pwd

def insertAtRandom(s, c):
    pos = randint(0, len(s)-1)
    result_s = s[0:pos] + c + s[pos:]
    return result_s

def randomCharacter(s):
    pos = randint(0,len(s)-1)
    return s[pos]

main()