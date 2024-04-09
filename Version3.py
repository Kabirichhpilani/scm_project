import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word_list = {
            'Animals': ["python", "cat", "dog", "elephant", "lion"],
            'Countries': ["india", "canada", "australia", "japan", "brazil"],
            'Fruits': ["apple", "banana", "grape", "kiwi", "orange"]
        }

        self.selected_category = ""
        self.selected_difficulty = ""
        self.secret_word = ""
        self.guessed_letters = []
        self.num_guesses = 0
        self.max_guesses = 6

        self.setup_game()

    def setup_game(self):
        self.instructions_label = tk.Label(self.root, text="Welcome to Hangman Game!\n\nInstructions:\nEnter a letter from 'a' to 'z' to guess the word. You have 6 attempts to guess the word.", font=("Arial", 14))
        self.instructions_label.pack(pady=10)

        self.category_frame = tk.Frame(self.root)
        self.category_frame.pack()

        self.category_label = tk.Label(self.category_frame, text="Select Category:", font=("Arial", 12))
        self.category_label.grid(row=0, column=0, padx=5)

        self.category_buttons = []
        for idx, category in enumerate(self.word_list.keys()):
            category_button = tk.Button(self.category_frame, text=category, font=("Arial", 12), width=10,
                                        command=lambda c=category: self.select_category(c))
            category_button.grid(row=0, column=idx+1, padx=5, pady=5)
            self.category_buttons.append(category_button)

        self.difficulty_frame = tk.Frame(self.root)
        self.difficulty_frame.pack()

        self.difficulty_label = tk.Label(self.difficulty_frame, text="Select Difficulty:", font=("Arial", 12))
        self.difficulty_label.grid(row=0, column=0, padx=5)

        self.difficulty_buttons = []
        for idx, difficulty in enumerate(["Easy", "Medium", "Hard"]):
            difficulty_button = tk.Button(self.difficulty_frame, text=difficulty, font=("Arial", 12), width=10,
                                           command=lambda d=difficulty: self.select_difficulty(d))
            difficulty_button.grid(row=0, column=idx+1, padx=5, pady=5)
            self.difficulty_buttons.append(difficulty_button)

        self.hangman_display = tk.Label(self.root, text="", font=("Courier", 14))
        self.hangman_display.pack()

        self.start_button = tk.Button(self.root, text="Start Game", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=10)

    def select_category(self, category):
        self.selected_category = category
        for button in self.category_buttons:
            if button['text'] == category:
                button.config(bg='yellow')
            else:
                button.config(bg=self.root.cget('bg'))

    def select_difficulty(self, difficulty):
        self.selected_difficulty = difficulty
        for button in self.difficulty_buttons:
            if button['text'] == difficulty:
                button.config(bg='yellow')
            else:
                button.config(bg=self.root.cget('bg'))

    def start_game(self):
        if not self.selected_category:
            messagebox.showwarning("Category not selected", "Please select a category.")
            return

        if not self.selected_difficulty:
            messagebox.showwarning("Difficulty not selected", "Please select a difficulty.")
            return

        self.instructions_label.pack_forget()
        self.category_frame.pack_forget()
        self.difficulty_frame.pack_forget()
        self.start_button.pack_forget()

        self.secret_word = random.choice(self.word_list[self.selected_category])
        self.guessed_letters = []
        self.num_guesses = 0

        self.word_label = tk.Label(self.root, text=self.get_display_word(), font=("Arial", 24))
        self.word_label.pack()

        self.guess_entry = tk.Entry(self.root, font=("Arial", 18))
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind('<Return>', lambda event: self.check_guess())

        self.guess_button = tk.Button(self.root, text="Guess", font=("Arial", 14), command=self.check_guess)
        self.guess_button.pack()

    def get_display_word(self):
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        return display_word

    def check_guess(self, event=None):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha() or not 'a' <= guess <= 'z':
            messagebox.showwarning("Invalid Guess", "Please enter a single letter from 'a' to 'z'.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You already guessed that letter.")
            return

        self.guessed_letters.append(guess)
        if guess not in self.secret_word:
            self.num_guesses += 1
            self.update_hangman()

        self.update_display()

    def update_display(self):
        self.word_label.config(text=self.get_display_word())

        if self.check_win():
            messagebox.showinfo("Congratulations!", "You won!")
            self.restart_game()

        if self.num_guesses >= self.max_guesses:
            messagebox.showinfo("Game Over", f"Sorry, you lost! The word was '{self.secret_word}'.")
            self.restart_game()

    def check_win(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True

    def update_hangman(self):
        hangman_parts = [
            "   +---+\n"
            "   |   |\n"
            "       |\n"
            "       |\n"
            "       |\n"
            "       |\n"
            "=========",  # Base
            "   +---+\n"
            "   |   |\n"
            "   O   |\n"
            "       |\n"
            "       |\n"
            "       |\n"
            "=========",  # Head
            "   +---+\n"
            "   |   |\n"
            "   O   |\n"
            "   |   |\n"
            "       |\n"
            "       |\n"
            "=========",  # Head + Body
            "   +---+\n"
            "   |   |\n"
            "   O   |\n"
            "  /|   |\n"
            "       |\n"
            "       |\n"
            "=========",  # One arm
            "   +---+\n"
            "   |   |\n"
            "   O   |\n"
            "  /|\\  |\n"
            "       |\n"
            "       |\n"
            "=========",  # Two arms
            "   +---+\n"
            "   |   |\n"
            "   O   |\n"
            "  /|\\  |\n"
            "  /    |\n"
            "       |\n"
            "=========",  # One leg
            "   +---+\n"
            "   |   |\n"
            "   O   |\n"
            "  /|\\  |\n"
            "  / \\  |\n"
            "       |\n"
            "========="   # Two legs
        ]
        hangman = hangman_parts[self.num_guesses]
        self.hangman_display.config(text=hangman)

    def restart_game(self):
        self.word_label.pack_forget()
        self.guess_entry.pack_forget()
        self.guess_button.pack_forget()
        self.hangman_display.config(text="")
        self.instructions_label.pack()
        self.category_frame.pack()
        self.difficulty_frame.pack()
        self.start_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    root.resizable(False, False)
    hangman_game = HangmanGame(root)
    root.mainloop()

