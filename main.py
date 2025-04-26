
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Radek Komárek
email: radekomarek@gmail.com
"""


# Funkce pro vykreslení herní desky
def print_board(board):
    print("+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+")

# Funkce pro ověření, zda hráč vyhrál
def check_winner(board, player):
    # Kontrola řádků
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Kontrola sloupců
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Kontrola obou diagonál
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Funkce pro kontrolu, zda je celá deska zaplněná (remíza)
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Hlavní funkce, která řídí celý průběh hry
def main():
    # Úvodní zpráva a pravidla
    print("Welcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:")
    print("Each player can place one mark (X or O) per turn on the 3x3 grid.")
    print("The WINNER is the player who places three of their marks in a row:")
    print("* Horizontal\n* Vertical\n* Diagonal")
    print("=" * 40)
    print("Let's start the game!")
    
    # Inicializace prázdné herní desky 3x3
    board = [[" "] * 3 for _ in range(3)]
    players = ["X", "O"]  # Seznam hráčů
    turn = 0  # Počet tahů

    # Hlavní herní smyčka
    while True:
        print_board(board)  # Vykreslení aktuálního stavu desky
        player = players[turn % 2]  # Střídání hráčů
        move = input(f"Player {player}, please enter your move (1-9): ")  # Zadání tahu

        # Ověření platnosti vstupu
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        move = int(move) - 1  # Posun na indexy od 0 do 8
        row, col = divmod(move, 3)  # Převod 1D pozice na 2D souřadnice

        # Kontrola, zda není políčko už obsazené
        if board[row][col] != " ":
            print("This position is already taken! Try again.")
            continue

        board[row][col] = player  # Zapsání tahu hráče na desku

        # Kontrola, zda hráč vyhrál
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Kontrola na remízu
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1  # Posun na další tah

# Spuštění hry, pokud je tento soubor spuštěn jako hlavní program
if __name__ == "__main__":
    main()
