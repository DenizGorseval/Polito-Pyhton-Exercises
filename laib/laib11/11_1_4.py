def censored_text(bad_wordsFile, raw_text):
    try:
        with open(bad_wordsFile, "r") as file:
            bad_words = set(word.strip() for word in file)

        with open(raw_text, "r") as file:
            lines = [[word.strip(",.'").lower() for word in line.split()] for line in file]
    except FileNotFoundError:
        print("One of the file can not be found")
        return()
   
    with open("censored.txt", "w") as file:
        for line in lines:
            for word in line:
                if word in bad_words:
                   file.write(len(word) * "*" + " ")
                else:
                    file.write(word + " ")
            file.write("\n")
    

def main():

    bad_words = "bad_words.txt"
    raw_text = "raw_text.txt"
    censored_text(bad_words,raw_text)
main()