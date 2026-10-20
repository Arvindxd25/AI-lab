""" Assignment 8 - Tic-Tac-Toe using Minimax """

# Play Tic-Tac-Toe against a Minimax AI
HUMAN = "X"
AI = "O"
board = [" "] * 9

wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def show_board():
    for row in range(3):
        cells = board[row * 3:row * 3 + 3]
        print(" | ".join(cell if cell != " " else str(row * 3 + i + 1)
                         for i, cell in enumerate(cells)))
        if row < 2:
            print("--+---+--")

def winner():
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

def minimax(ai_turn):
    result = winner()
    if result == AI:
        return 1
    if result == HUMAN:
        return -1
    if " " not in board:
        return 0

    if ai_turn:
        best_score = -2
        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = 2
        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def ai_move():
    best_score = -2
    best_position = None

    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_position = i

    return best_position

print("You are X and the computer is O.")
while True:
    show_board()

    try:
        position = int(input("Choose a position (1-9): ")) - 1
    except ValueError:
        print("Please enter a number.")
        continue

    if position < 0 or position > 8 or board[position] != " ":
        print("That position is not available. Try again.")
        continue

    board[position] = HUMAN
    if winner() == HUMAN:
        show_board()
        print("You win!")
        break
    if " " not in board:
        show_board()
        print("It is a draw!")
        break

    position = ai_move()
    board[position] = AI
    print("Computer chooses position", position + 1)

    if winner() == AI:
        show_board()
        print("Computer wins!")
        break
    if " " not in board:
        show_board()
        print("It is a draw!")
        break
