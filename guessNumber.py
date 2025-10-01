import random
import tkinter as tk

root = tk.Tk()
root.title("Guessing Number")
root.geometry("650x500")

# Game variables
low = None
high = None
num = None
chance = 5
guess_counter = 0

# GUI elements
welcome_label = tk.Label(root, text="Welcome to the Guessing Number Game", font=("Helvetica", 18))
welcome_label.pack(pady=10)

# Bounds input
low_label = tk.Label(root, text="Enter lower bound:",font=("helvetica",18))
low_label.pack(pady =10)
low_entry = tk.Entry(root,font=("helvetica",18))
low_entry.pack(pady =10)

high_label = tk.Label(root, text="Enter upper bound:",font=("helvetica",18))
high_label.pack(pady =10)
high_entry = tk.Entry(root,font=("helvetica",18))
high_entry.pack(pady =10)

start_button = tk.Button(root, text="Start Game", command=lambda: start_game())
start_button.pack(pady=10)

# Guessing elements
guess_label = tk.Label(root, text="Enter your guess: you have only 5 Chance ",font=("helvetica",18))
guess_label.pack(pady =5)
guess_entry = tk.Entry(root,font=("helvetica",18))
guess_entry.pack(pady =5)
guess_entry.config(state='disabled')

guess_button = tk.Button(root, text="Guess", command=lambda: make_guess())
guess_button.pack(pady=10)
guess_button.config(state='disabled')

message_label = tk.Label(root, text="", font=("Helvetica", 12))
message_label.pack(pady=5)

attempts_label = tk.Label(root, text="", font=("Helvetica", 12))
attempts_label.pack(pady=5)

def start_game():
    global low, high, num, guess_counter
    try:
        low = int(low_entry.get())
        high = int(high_entry.get())
        if low >= high:
            message_label.config(text="Lower bound must be less than upper bound.")
            return
        num = random.randint(low, high)
        guess_counter = 0
        message_label.config(text=f"You have {chance} chances to guess the number between {low} and {high}. Let's start!")
        attempts_label.config(text=f"Attempts left: {chance - guess_counter}")
        # Disable bounds input, enable guessing
        low_entry.config(state='disabled')
        high_entry.config(state='disabled')
        start_button.config(state='disabled')
        guess_entry.config(state='normal')
        guess_button.config(state='normal')
    except ValueError:
        message_label.config(text="Please enter valid integers for bounds.")

def make_guess():
    global guess_counter
    try:
        guess = int(guess_entry.get())
        guess_entry.delete(0, tk.END)
        guess_counter += 1
        if guess == num:
            message_label.config(text=f"Congratulations! The number was {num}. You guessed it in {guess_counter} attempts.")
            guess_entry.config(state='disabled')
            guess_button.config(state='disabled')
        elif guess_counter >= chance:
            message_label.config(text=f"Sorry! The number was {num}. Better luck next time!")
            guess_entry.config(state='disabled')
            guess_button.config(state='disabled')
        elif guess > num:
            message_label.config(text="Too high! Try a lower number.")
        else:
            message_label.config(text="Too low! Try a higher number.")
        attempts_label.config(text=f"Attempts left: {chance - guess_counter}")
    except ValueError:
        message_label.config(text="Please enter a valid integer for guess.")

root.mainloop()

