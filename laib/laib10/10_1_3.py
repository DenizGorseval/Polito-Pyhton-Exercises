def find_word(filename, word):
    with open(filename, "r") as file:
        sentences = []
        for line in file:
            if word.lower() in line.lower():
                sentences.append(line.strip())
        if len(sentences) >= 1:
            return sentences

def main():
    file_names = input("Enter the file names as a single line: ")
    file_list = [file_name.strip() for file_name in file_names.split(",")]
    
    search_word = input("Enter a word to be searched: ")
    for file in file_list:
        sentences = find_word(file, search_word)
        if sentences != None:
            print(f"{file}: {sentences}")


