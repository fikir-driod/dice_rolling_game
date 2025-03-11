import tkinter as tk
from tkinter import messagebox
import random
from itertools import cycle


def roll_dice():

    roll_button.config(state=tk.DISABLED)
    

    rolls = [random.randint(1, 6) for _ in range(10)]
    current_player = next(player_cycle)
    
    def animate_roll(index=0):
        if index < len(rolls):
            dice_label.config(text=f"🎲 {rolls[index]} 🎲")
            root.after(100, animate_roll, index + 1)
        else:
            final_roll = rolls[-1]
            dice_label.config(text=f"🎲 {final_roll} 🎲")
            

            if current_player == "Player 1":
                player1_score.set(player1_score.get() + final_roll)
                player1_label.config(text=f"Player 1: {player1_score.get()}")
            else:
                player2_score.set(player2_score.get() + final_roll)
                player2_label.config(text=f"Player 2: {player2_score.get()}")
            
        
            roll_button.config(state=tk.NORMAL)
            
           
            check_winner()
    
    animate_roll()


def check_winner():
    if player1_score.get() >= 20:
        announce_winner("Player 1")
    elif player2_score.get() >= 20:
        announce_winner("Player 2")


def announce_winner(winner):
    messagebox.showinfo("Game Over", f"{winner} wins the game!")
    reset_game()


def reset_game():
    player1_score.set(0)
    player2_score.set(0)
    player1_label.config(text="Player 1: 0")
    player2_label.config(text="Player 2: 0")
    dice_label.config(text="🎲 Roll the Dice! 🎲")
    global player_cycle
    player_cycle = cycle(["Player 1", "Player 2"])


def on_enter(event):
    roll_button.config(bg="#4CAF50", fg="white")

def on_leave(event):
    roll_button.config(bg="#45a049", fg="white")

root = tk.Tk()
root.title("Dice Rolling Game")
root.geometry("400x300")
root.configure(bg="#f0f0f0")


player1_score = tk.IntVar(value=0)
player2_score = tk.IntVar(value=0)


player1_label = tk.Label(root, text="Player 1: 0", font=("Helvetica", 14), bg="#f0f0f0", fg="#333")
player1_label.pack(pady=10)

player2_label = tk.Label(root, text="Player 2: 0", font=("Helvetica", 14), bg="#f0f0f0", fg="#333")
player2_label.pack(pady=10)

dice_label = tk.Label(root, text="🎲 Roll the Dice! 🎲", font=("Helvetica", 20), bg="#f0f0f0", fg="#333")
dice_label.pack(pady=20)


roll_button = tk.Button(root, text="Roll Dice", font=("Helvetica", 14), bg="#45a049", fg="white",
                        activebackground="#4CAF50", command=roll_dice)
roll_button.pack(pady=10)


roll_button.bind("<Enter>", on_enter)
roll_button.bind("<Leave>", on_leave)


player_cycle = cycle(["Player 1", "Player 2"])


root.mainloop()