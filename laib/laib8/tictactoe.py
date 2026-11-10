def board():
    table = []
    for r in range(3):
        row = []
        for c in range(3):
            row.append(" ")
        table.append(row)
    return table

def check_winner(board, player):
    # Satır kontrolü
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    # Sütun kontrolü
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    # Çapraz kontrolü
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def game(board):
    counter = 0
    current_player = "O"  # Player 1 başlıyor

    while counter < 9:
        print(f"PLAYER {1 if current_player == 'O' else 2} TURN")
        row = int(input("Enter the row(1,2 or 3): ")) - 1
        col = int(input("Enter the col(1,2 or 3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That place is already filled, game is over")
            break

        for r in board:
            print(r)

        if check_winner(board, current_player):
            print(f"The game is over Player {1 if current_player == 'O' else 2} won")
            break

        counter += 1
        if counter == 9:
            print("The board is filled up, nobody won the game")
            break

        # Oyuncu değiştir
        current_player = "X" if current_player == "O" else "O"

def main():
    table = board()
    game(table)
main()
