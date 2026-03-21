import tkinter as tk
import random

magic_number = random.randint(1, 10)
attempts = 3

def check_guess(guess):
    global attempts

    attempts -= 1

    if guess == magic_number:
        result_label.config(text="🎉 Congratulations! You found the magic number!")
        disable_buttons()
        show_close_button()

    elif attempts == 0:
        result_label.config(text=f"❌ Game Over! The magic number was {magic_number}")
        disable_buttons()
        show_close_button()

    elif guess < magic_number:
        result_label.config(text=f"Higher! Attempts left: {attempts}")

    else:
        result_label.config(text=f"Lower! Attempts left: {attempts}")

def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

def show_close_button():
    close_button.pack(pady=10)

# Create window
root = tk.Tk()
root.title("Magic Number Game")
root.geometry("320x300")

title_label = tk.Label(root, text="Guess the Magic Number (1–10)", font=("Arial", 14))
title_label.pack(pady=10)

result_label = tk.Label(root, text="You have 3 attempts.", font=("Arial", 10))
result_label.pack(pady=5)

# Frame for number buttons
frame = tk.Frame(root)
frame.pack(pady=10)

buttons = []

# Create buttons 1–10
for i in range(1, 11):
    btn = tk.Button(frame, text=str(i), width=5, height=2,
                    command=lambda num=i: check_guess(num))
    btn.grid(row=(i-1)//5, column=(i-1)%5, padx=5, pady=5)
    buttons.append(btn)

# Close button (hidden at start)
close_button = tk.Button(root, text="Close Game", command=root.destroy)

root.mainloop()
