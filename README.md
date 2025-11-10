# 🪓 Hangman Game (Python)

A simple command-line **Hangman game** built in Python.  
The game selects a random word from a text file (`words.txt`) and challenges the player to guess it letter by letter before running out of attempts — with hints, difficulty levels, and colorful terminal output.

---

## 🎮 Features

- Random word selection from `words.txt`
- Hints shown at the beginning of each game
- Difficulty levels: `easy`, `medium`, `hard`
- Optional "word of the day" mode (based on system date)
- Colored and formatted terminal display (ANSI codes)
- Input validation for letter guesses
- Tracks remaining attempts visually with hearts (♥)
- Calculates difficulty automatically from word frequency

---

## 🧠 How It Works

1. **Word Selection**  
   Uses `pick_random_word()` to read from `words.txt` and randomly select a word (and its hint if provided).

2. **Gameplay Loop**  
   - The player chooses difficulty and whether to play the “word of the day”.  
   - The game shows the hint for 5 seconds.  
   - The player guesses letters one by one until either:
     - All letters are guessed ✅, or  
     - All attempts are used ❌.

3. **Validation and Updates**  
   - Inputs must be single letters `[a-z]`.
   - Incorrect guesses reduce remaining attempts.
   - Correct guesses reveal letters in the hidden word.

---

## 📁 Project Structure

📂 hangman-game/
├── hangman.py # main script (game logic)
├── words.txt # list of words and hints (format: word|hint)
└── README.md # project documentation

go
Copiar código

Example of `words.txt`:
python|Programming language
apple|A common fruit
computer|Used to run code

yaml
Copiar código

---

## 🚀 Running the Game

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   cd hangman-game
Run the game

bash
Copiar código
python hangman.py
Follow the prompts

Choose whether to play the “word of the day”.

Select difficulty: easy, medium, or hard.

Guess letters to reveal the word!

🧩 Key Functions
Function	Description
pick_random_word()	Picks a random word (and hint) from words.txt
format_hidden_word()	Replaces unguessed letters with _
all_letters_guessed()	Checks if the user guessed all letters
ask_for_valid_input()	Validates user input
update_game()	Updates attempts and guessed letters
calculate_difficulty()	Classifies words into difficulty levels
game()	Main loop controlling the game flow

🎨 Example Output
makefile
Copiar código
Hint: A programming language
_____  ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥
Enter a letter [a-z]:
If you win:

nginx
Copiar código
You won 🎉
If you lose:

nginx
Copiar código
You lost 💀
🧰 Requirements
Python 3.7 or higher

A words.txt file in the same directory as hangman.py

🧑‍💻 Author
Developed by [Your Name] as part of a Python programming assignment.
Feel free to fork, modify, or improve the game!

📜 License
This project is open-source under the MIT License.




