def read_game(filename):
    try:
        with open(filename, "r") as file:
            lines = [line.strip().split("|") for line in file]
    except OSError:
        print("The file can not be opened")
    
    default = lines[0:8]
    moves = lines[9:]

    return default, moves

def board_forming(default):
    board = []
    seperator = "--+--+--+--+--+--+--+--"
    
    for line in default:
        board.append(seperator)
        temp = []
        for p in range(len(line)):
            temp.append(line[p])
            if p < 7:
                temp.append("|")
        board.append(temp)
    
    return board
            
                
    
    
def move_onboard(board, moves):
    pass
                        
                            
                            
def positions_formed(board):
    positions_dict = {}
    for letter in "abcdefgh":
        positions_dict[]
            
            


            

       



        
    

def main():
    filename = "game.txt"
    default, moves = read_game(filename)
    board = board_forming(default)
    positions_dict = positions_formed()
    move_onboard(board, moves)


main()