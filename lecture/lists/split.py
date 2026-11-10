s = input("Give me some words: ")

list_of_words = s.split()

if len(list_of_words) >= 2:
    print("You gave me at least two words")
    print("The second word is", list_of_words[1])
else:
    print("You didnt give me enough words")

for i in range(len(list_of_words)):
    list_of_words[i] = list_of_words[i].split(",")

list_of_words = s.split(maxsplit=2)
for elem in list_of_words:
    print(elem)