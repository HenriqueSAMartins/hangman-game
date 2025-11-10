import random
import os
from datetime import date
import time

# ANSI color codes
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"

def pick_random_word(difficulty_level, today):

    """
    Picks a random word from the word list. The word list is the provided words.txt file.
    Returns:
        str : random word picked
    """
    if today:
        random.seed(int(date.today().strftime("%Y%m%d")))

    dirpath = os.path.dirname(__file__)
    path = os.path.join(dirpath, "words.txt")

    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    line = random.choice(lines)
    parts = line.split("|")
    word = parts[0].strip().lower()
    hint = parts[1].strip() if len(parts) > 1 else ""

    return word, hint


def format_hidden_word(word_to_guess, letters_guessed):
    """
    Formats the word to guess by replacing all non-guessed letters by "_"

    Args:
        word_to_guess (str): Word that the user has to guess
        letters_guessed (str): String containing all the letters already guessed by the user

    Returns:
        str: Word to display, where all of the letters not in letters_guessed are replaced by the "_" symbol
    """
    formatted = ""
    for letter in word_to_guess:
        if letter.lower() in letters_guessed.lower():
            formatted += letter
        else:
            formatted += "_"
    return formatted
 


def all_letters_guessed(word_to_guess, letters_guessed):
    """
    Checks whether all letters of word_to_guess are in letters_guessed.

    Args:
        word_to_guess (str) : word that the user has to guess
        letters_already_guessed (str) : string containing all the letters already guessed by the user.

    Returns:
        bool : True if all letters have been guessed, False otherwise
    """
    a=True
    for i in word_to_guess:
        if not(i in letters_guessed):
            a=False
    return(a)


def ask_for_valid_input(letters_guessed):
    a = input("Enter a letter [a-z]: ")
    while not (len(a) ==1 and 97 <= ord(a) <= 122 and not a in letters_guessed):
        a = input("Enter a letter [a-z]: ")
    """
    Asks the user to pick a letter, using input("Enter a letter [a-z]: "). 
    Checks that the input is a single character (len(i) == 1) and that it is a lowercase letter 
    (97 <= ord(a) <= 122), and that it is not already in letters_guessed (a not in letters_guessed).
    If not, prompts the user to pick a letter again (using a while loop until all criteria are respected)
    
    Args:
        letters_guessed (str) : string containing all the letters already guessed by the user
    
    Returns:
        str : one-character string containing the letter picked by the user
    """
    return a


def update_game(word_to_guess, letters_guessed, new_guess, remaining_attempts):
    letters_guessed += new_guess
    if new_guess not in word_to_guess:
        remaining_attempts -= 1
    return letters_guessed, remaining_attempts
        
    """
    
    Based on the new_guess, updates the letters_guessed (letters_guessed.append(new_guess))
    and remaining_attempts variables (remaining_attempts decreases by one if new_guess not in word_to_guess).

    Args:
        word_to_guess (str) : word that the user has to guess
        letters_guessed (str) : string containing all the letters already guessed by the user
        new_guess (str) : one-character string containing the letter picked by the user
        remaining_attempts (int) : number of attempts remaining

    Returns:
        str : new string containing all letters guessed 
        int : new number of attempts remaining 
    """


def game():
    """
    Allows the user to play one game of hangman:
        - picks a random word using pick_random_word()
        - sets remaining_attempts to 8, and letters_guessed to ''
        - while there remaining_attempts > 0 AND not all_letters_guessed() , do:
            - print the word, formatted using format_hidden_word()
            - print the number of remaining attempts
            - ask for a valid input from the user using ask_for_valid_input()
            - call update_game(), and update letters_guessed and remaining_attempts based on the returned values
        - once exiting the loop, if remaining_attempts > 0, print("You won"), otherwise, print("You lost")
    """
    play_today = None
    while play_today not in ["yes", "no"]:
        play_today = input("Do you want to guess today's word? [yes/no]")
    play_today = True if play_today == "yes" else False
    if not(play_today):
        print("\033[H\033[J", end="")

    difficulty_input = None
    while difficulty_input not in ["easy", "medium", "hard"]:
        difficulty_input = input("Choose difficulty [easy/medium/hard]:").strip().lower()
    else:
        difficulty_input="medium"

    remaining_attempts = 8
    letters_guessed = ""
    word_to_guess,hint = pick_random_word(difficulty_input,play_today)


    # Show the hint and wait 5 seconds
    print(f"Hint: {hint}")
    time.sleep(5)

    while (remaining_attempts>0) and not (all_letters_guessed(word_to_guess, letters_guessed)):
        print (CYAN, format_hidden_word(word_to_guess, letters_guessed)+  "  "+"♥ "*remaining_attempts+ "  " + ','.join(letters_guessed), RESET)
        print(remaining_attempts)
        new_guess = ask_for_valid_input(letters_guessed)
        tup = update_game(word_to_guess, letters_guessed, new_guess, remaining_attempts)
        remaining_attempts = tup[1]
        letters_guessed = tup[0]
    if remaining_attempts>0:
        print(GREEN, "You won", RESET)
    else:
        print(RED, "You lost", RESET)


def calculate_difficulty(word):
    """Calculate word difficulty based on letter frequency.
    Uses common letter ordering: E,T,A,O,N,R,I,S,H,D,L,F,C,M,U,G,Y,P,W,B,V,K,J,X,Z,Q
    Returns: 'easy', 'medium', or 'hard'
    """
    frequency = "ETAONRISHDLFCMUGYPWBVKJXZQ"
    total_index = sum(frequency.index(letter.upper()) for letter in word if letter.upper() in frequency)
    avg_index = total_index / len(word)
    
    if avg_index <= 6:
        return "easy"
    elif avg_index <= 8:
        return "medium"
    else:
        return "hard"
        
        

if __name__ == "__main__":
    game()