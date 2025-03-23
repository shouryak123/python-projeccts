board =[[" "," "," "],
        [" "," "," "],
        [" "," "," "]]
def gameboard(board):
    for row in range(len(board)):
        print("  | ".join(board[row]))
        if row<len(board)-1:
            print("---+----+---")

def winner_checker(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False  # No winner yet
            
winner =False
chance =1
while(winner != True):
    try:
        row =int(input("Row: "))
        column =int(input("Column: "))
        while(board[row][column]!=" "):
            print("already done")
            continue
        if chance%2!=0:
            board[row][column]="X"
        else:
            board[row][column]="0"
        gameboard(board)
        winner=winner_checker(board)
        chance=chance+1
        if chance ==10:
            break
    except IndexError:
         print("Invalid input! Please enter numbers only.")


if chance%2==0 and chance!=10 :
    print("Player X Won")
elif chance!=0 and chance!=10:
    print("Player 0 Won")
else:
    print("Its a draw")

        
