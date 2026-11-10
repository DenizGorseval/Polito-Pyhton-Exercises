Long_DNA = input("Enter a long DNA sequence consisting of 'A', 'C', 'T', 'G': ")

Short_DNA = input ("Enter a short DNA sequence: ")

counter = 0
for i in range(len(Long_DNA)): #ACTGACTGACTGACTGGAGAGCTCT
    temp = i
    for p in range(len(Short_DNA)): #ACTG
        if Long_DNA[temp] == Short_DNA[p]:
            temp += 1
            if temp == len(Short_DNA):
                counter += 1
                temp = 0

print(f"the short DNA is inside Long DNA {counter} times")
            