import pprint
def read_seq(filename):
    try:
        sequences = []
        with open(filename,"r") as file:
            for line in file:
                line = line.strip().split(" ")
                seq = []
                for num in line:
                    seq.append(int(num))
                sequences.append(seq)
    except OSError:
        print("The file cannot be opened")

    return sequences
def check_sequences(sequences):
    for seq_i,seq in enumerate(sequences):
        if len(seq) > 1:
            for i in range(len(seq)-1):
                
                if seq[i] % 2 == 0 and seq[i+1] == (seq[i])/2:
                    continue

                elif  seq[i+1] == (3*seq[i])+1:
                    continue

                else:
                    print(f"Sequence {seq_i+1} is a NOT a Munodi sequence")
                    break

            if seq[i+1] == 1:
                print(f"Sequence {seq_i+1} is a Munodi sequence (length {len(seq)})")
            
        elif seq[0] == 1:
            print(f"Sequence {seq_i+1} is a Munodi sequence (length {len(seq)})")
        else:
            print(f"Sequence {seq_i+1} is a NOT a Munodi sequence")


def main():
    filename = "seq_long.dat"
    sequences = read_seq(filename)
    check_sequences(sequences)

main()