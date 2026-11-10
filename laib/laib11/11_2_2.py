def genetic_code(filename):
    genetic_dict = {}
    try:
        with open(filename, "r") as file:
            lines = [[mRNA.strip(',"')for mRNA in line.split()] for line in file]
    except FileNotFoundError:
        print("The file can not be opened")
        return ()
    
    for line in lines:
        if len(line) == 2:
            genetic_dict[line[1]] = line[0]
        else:
            for i in range(1,len(line)-1):
                genetic_dict[line[i]] = line[0]
        
    return genetic_dict


def amino_acidseq(DNA_seq, genetic_dict):
    new_sequence = ""
    i = 0
    codon = ""
    flag = False
    if "AUG" in DNA_seq:
        while i < len(DNA_seq):
            codon = DNA_seq[i:i+3]
            if codon == "AUG" and flag == False:
                codon = DNA_seq[i:i+3]
                new_sequence += genetic_dict[codon]
                flag = True
                i += 3
            elif flag == True and codon != "UGA":
                codon = DNA_seq[i:i+3]
                new_sequence += genetic_dict[codon]
                i+= 3
            elif codon == "UGA":
                new_sequence += genetic_dict[codon]
                return new_sequence
                
            else: 
                i += 1
            

    else:
        raise ValueError("The DNA sequence does not contain the start or stop codons")
        



def main():
    filename = "codice_genetico.csv"
    genetic_dict = genetic_code(filename)
    DNA_seq = "GUAUGCACGUGACUUUCCUCAUGAGCUGAU"
    codon_names = amino_acidseq(DNA_seq,genetic_dict)
    print(codon_names)
main()