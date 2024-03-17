**project title**-Creating Hangman Game on Python 
 
**Manager**-Kabir

**Developer**-Manan Sharma

**Tester**-Jatin Patter

To play the Hangman Game implemented using tkinter in Python, follow these steps:

1. When you run the script, a GUI window will appear titled "Hangman Game."
2. You will see two dropdown menus:
   - Category: Choose a category from Animals, Countries, or Fruits.
   - Difficulty: Choose the difficulty level from Easy, Medium, or Hard.
3. Select your desired options from the dropdown menus.
4. Click on the "Start Game" button to begin the game.
5. Once the game starts, the selected category's secret word will be chosen randomly, and the display will show underscores representing each letter in the word.
6. Below the display, there will be an entry field where you can guess a letter and a "Guess" button to submit your guess.
7. Enter a single letter in the entry field and click the "Guess" button.
   - If the letter is correct and part of the secret word, it will be revealed in its respective position(s).
   - If the letter is incorrect, it will count as a wrong guess, and part of the hangman will be displayed.
8. Continue guessing letters one at a time until you either:
   - Guess all the letters in the word correctly and win the game (you will see a congratulatory message).
   - Exceed the maximum allowed wrong guesses (6 by default) and lose the game (the word will be revealed, and you will see a game over message).
9. After winning or losing, you can restart the game by clicking the "Start Game" button again and choosing new options from the dropdown menus.

Note: The hangman display will update as you make wrong guesses, showing the hangman figure progressively as you approach the maximum allowed wrong guesses.

Manager is reaching out to assign Develpor an exciting task: developing a Hangman game in Python.
This project will not only showcase your programming skills but also provide a fun and interactive experience for users.

Here are the instructions and guidelines for the task:

Project Overview:
Your goal is to create a text-based Hangman game using Python. The game should allow players to guess a word within a limited number of attempts.

Random Module:
Utilize the random module to randomly select a word from a predefined list. This will add variability to the game and enhance the player experience.

User Interface:
Design a simple text-based interface using print statements. Display the current state of the word, guessed letters, remaining attempts, and any other relevant information.

Game Logic:

1.Implement the core game logic:

2.Select a random word from a list.

3.Display the word as underscores initially.

4.Prompt the player to guess a letter.

5.Check if the letter is in the word and update the display accordingly.

6.Track incorrect guesses and decrement remaining attempts.

7.End the game when the word is guessed correctly or attempts run out.

8.Add quit option at the end of it.

Code Structure:
Organize your code into functions for better modularity and readability. Consider functions for word selection, display update, guess validation, game status check, etc.

Error Handling:
Implement proper error handling for user input validation. Ensure that the game handles invalid inputs gracefully.

Testing:
Thoroughly test your game with various scenarios, including correct and incorrect guesses, to ensure it functions as expected under different conditions.

Documentation and Comments:
Provide clear documentation and comments within your code to explain the purpose of functions, logic flow, and any complex algorithms used. 

**Tester**-

 **version1**
 
Testing for the Hangman game code includes validating valid and invalid guesses for correct feedback, handling repeated guesses without affecting the game state, and ensuring accurate recognition of winning and losing conditions with appropriate messages. The hangman display updates with each incorrect guess, UI elements interact smoothly, and game state resets reliably for a seamless gaming experience across sessions. These tests collectively ensure the game functions as intended, providing an engaging and error-free user experience.....
but
The current implementation relies solely on basic Tkinter widgets like labels, entry fields, and buttons, resulting in a simplistic and potentially unengaging user interface. Adding visual enhancements such as better styling, graphical elements for the hangman display, and improved feedback messages could significantly enhance the overall user experience and make the game more appealing to players.And at last it should ask to start the game again but automaticaly starts the game again...

**version2**

The improved version of the Hangman game code enhances the user interface by using larger fonts for better readability and organizing UI elements more neatly. It introduces a "Play Again" button after winning or losing, providing users with the option to restart the game or quit. Unlike the initial version, which automatically resets the game, the enhanced version gives players control over starting a new game. Additionally, the improved code handles win/lose scenarios with appropriate message boxes while maintaining a cleaner and more interactive user experience......
consider adding visual cues like changing text colors for correct guesses and displaying hangman images for wrong guesses. Implement difficulty levels to cater to different player skills, and add word categories for variety. Introducing graphics or animations for the hangman display can enhance the game's appeal and engagement.......

**version3**

Hangman game code features categorized word lists (Animals, Countries, Fruits), allowing players to select categories and difficulty levels (Easy, Medium, Hard) for a tailored gaming experience. It provides interactive UI elements for category and difficulty selection before starting the game, enhancing user engagement......
