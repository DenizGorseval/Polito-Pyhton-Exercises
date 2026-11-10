string = input("Enter a line of string: ")
s1 = ''
s2 = ''
s3 = ''
for ch in string:
    if ch.isupper():
        s1 += ch
    
print("only the uppercase letters of the string;", s1)
for i,ch in enumerate(string):
    if i % 2 == 0:
        s2 += ch
    
print("letters in even positions in the string;", s2)
for ch in string:
    ch = ch.lower()
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        s3 += "_"
    else:
        s3 += ch
    
print("the same string in which, instead of vowels (upper or lowercase), there is an underscore (_);", s3)



    


