def StudentNotes(ID, clas):
    filename = clas + ".txt"
    with open(filename, "r") as file:
        IDandNotes = [line.strip().split() for line in file]
        
        for line in IDandNotes:
            if ID == line[0]:
                print(f"{clas} {line[1]}")

def main():
    try:
        with open("classes.txt", "r") as file:
            classes = [line.strip() for line in file]
    except OSError:
       print("The file can not be opened")

    StudentID = input("Enter the StudentID: ")
    print("Student  ID:"+StudentID)
    for clas in classes:
        StudentNotes(StudentID, clas)


main()