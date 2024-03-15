import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word_list = ["python", "java", "javascript", "html", "css", "ruby", "swift", "php"]
        self.secret_word = ""
        self.guessed_letters = []
        self.num_guesses = 0
        self.max_guesses = 6

        self.setup_game()

    def setup_game(self):
        self.secret_word = random.choice(self.word_list)
        self.guessed_letters = []
        self.num_guesses = 0

        self.word_label = tk.Label(self.root, text=self.get_display_word())
        self.word_label.pack()

        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack()

        self.hangman_display = tk.Label(self.root, text="")
        self.hangman_display.pack()

    def get_display_word(self):
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        return display_word

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Guess", "Please enter a single letter.")
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
            self.setup_game()

        if self.num_guesses >= self.max_guesses:
            messagebox.showinfo("Game Over", f"Sorry, you lost! The word was '{self.secret_word}'.")
            self.setup_game()

    def check_win(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True

    def update_hangman(self):
        hangman_parts = [
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",  # Base
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",  # Head
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",  # Body
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",  # One arm
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",  # Two arms
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",  # One leg
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="   # Two legs
        ]
        hangman = hangman_parts[self.num_guesses]
        self.hangman_display.config(text=hangman)

if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()

