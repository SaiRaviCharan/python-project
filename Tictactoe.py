import tkinter as tk
from tkinter import messagebox

# Function to initialize the game
def initialize_game():
    global board, current_player
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    for button in buttons:
        button.config(text='', state=tk.NORMAL)

# Function to check if a player has won
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

# Function to handle button click
def button_click(row, col):
    global current_player

    if board[row][col] == '':
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            disable_buttons()
        elif all(board[row][col] != '' for row in range(3) for col in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            disable_buttons()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Function to disable all buttons after game ends
def disable_buttons():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize board and current player
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Create buttons for the Tic-Tac-Toe grid
buttons = [[tk.Button(root, text='', font=('normal', 40), width=5, height=2, 
                     command=lambda row=row, col=col: button_click(row, col)) 
            for col in range(3)] for row in range(3)]

# Place buttons in a grid
for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col)

# Create a button to restart the game
restart_button = tk.Button(root, text="Restart", font=('normal', 20), width=10, height=2, command=initialize_game)
restart_button.grid(row=3, column=0, columnspan=3)

# Start the game
initialize_game()

# Run the GUI
root.mainloop()
