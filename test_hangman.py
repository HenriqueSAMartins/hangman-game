import pytest

from hangman import *


def test_pick_random_word():
    """Tests the pick_random_word function."""
    word = pick_random_word()
    if isinstance(word, tuple):  # This is needed for later changes in the hangman.py file
        word = word[0]
    assert len(word) >= 7, "word is shorter than the shortest word in words.txt"
    assert len(word) <= 15, "word is longer than the longest word in words.txt"
    assert sum([1 for l in word if 97 <= ord(l) <= 122]), "word contains letters not in [a-z]"


def test_format_hidden_word():
    """Tests the format_hidden_word function"""
    word = "centralesupelec"
    assert format_hidden_word(word, "") == "_______________", "format_hidden_word not working with empty letters_guessed"
    assert format_hidden_word(word, "ojzk") == "_______________", "format_hidden_word not working with only wrong letters_guessed"
    assert format_hidden_word(word, "c") == "c_____________c", "format_hidden_word not working with one letter in letters_guessed"
    assert format_hidden_word(word, "aeiou") == "_e___a_e_u_e_e_", "format_hidden_word not working with partial letters guessed"
    assert format_hidden_word(word, "centralsup") == "centralesupelec", "format_hidden_word not working with all letters guessed (sorted order)"
    assert format_hidden_word(word, "tceanlrusp") == "centralesupelec", "format_hidden_word not working with all letters guessed (unsorted order)"


def test_all_letters_guessed():
    """Tests the all_letters_guessed function"""
    word = "centralesupelec"
    assert not all_letters_guessed(word, ""), "all_letters_guessed not working with no letters guessed"
    assert not all_letters_guessed(word, "ojzk"), "all_letters_guessed not working with only wrong letters guessed"
    assert not all_letters_guessed(word, "aeiou"), "all_letters_guessed not working with partial letters guessed"
    assert all_letters_guessed(word, "centralsup"), "all_letters_guessed not working with all letters guessed (sorted order)"
    assert all_letters_guessed(word, "tceanlrusp"), "all_letters_guessed not working with all letters guessed (unsorted order)"


def test_ask_for_valid_input(monkeypatch):
    """Tests the ask_for_valid_input function"""
    # Test valid input first try
    monkeypatch.setattr('builtins.input', lambda _: "a")
    assert ask_for_valid_input("") == "a", "ask_for_valid_input not working with valid input on first try"

    # Test invalid inputs then valid
    inputs = iter(["1", "A", "aa", "z"])  # Invalid: number, uppercase, multiple chars, then valid
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert ask_for_valid_input("") == "z", "ask_for_valid_input not working with invalid then valid input"

    # Test already guessed letter then valid
    inputs = iter(["a", "b"])  # First letter already guessed, second is valid
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert ask_for_valid_input("a") == "b", "ask_for_valid_input not working with already guessed then valid input"

    # Test special characters then valid
    inputs = iter(["@", "#", "c"])  # Special chars then valid
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert ask_for_valid_input("") == "c", "ask_for_valid_input not working with special chars then valid input"

    
def test_update_game():
    """Tests the update_game function"""
    word = "centralesupelec"
    assert update_game(word, "", "o", 10)[0] == "o", "update_game did not update the guess list"
    assert update_game(word, "", "o", 10)[1] == 9, "update_game did not decrease the number of turns on a wrong guess"

    assert update_game(word, "aeiou", "c", 10)[0] == "aeiouc", "update_game did not update the guess list"
    assert update_game(word, "aeiou", "c", 10)[1] == 10, "update_game decreased the number of turns despite a correct guess"

    assert update_game(word, "ojzk", "c", 10)[0] == "ojzkc", "update_game did not update the guess list"
    assert update_game(word, "ojzk", "c", 10)[1] == 10, "update_game decreased the number of turns despite a correct guess"