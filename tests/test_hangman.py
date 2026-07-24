import pytest
from lib.hangman import *

"""
Given a secret word the game is in an empty state initizes with no incorrect or correct guess (_ _ _)
"""
def test_game_starts_empty_state():
    game = Hangman(["cat"], secret_word = "cat")
    assert game.secret_word == "cat"
    assert game.missed_letters == ""
    assert game.correct_letters == ""
    assert game.game_status == False 

"""
Given a word list (we will provide) no secret_word selected the game will choose one of the words provided [word_bank] (testing able to pull word from word bank)
"""
def test_pull_from_word_bank():
    game = Hangman(["cat", "dog", "rabbit"])
    assert game.secret_word in ["cat", "dog", "rabbit"]

"""
Given a word list (we will provide) secret_word has been selected
"""
def test_game_selects_secret_word():
    game = Hangman(["cat", "dog", "rabbit"], secret_word = "rabbit")
    assert game.secret_word == "rabbit"

"""
Given the users guesses an a valid alphabetical letter. 
"""
def test_guess_word_returns_valid_alphabetical_letter(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "a")
    result = guess_word("")
    assert result == "a"

"""
Given the users inputs more than one letter a message is displayed to prompt user 
of error and how to correct. 
"""
def test_guess_word_rejects_multiple_letters(monkeypatch):
    answers = iter(["abc", "b"])
    monkeypatch.setattr("builtins.input", lambda: next(answers))
    result = guess_word("")
    assert "⚠️  Please enter a single letter. ⚠️" 
    assert result == "b"

"""
Given the users inputs already used letter a message is displayed to prompt user 
of error and how to correct. 
"""
def test_guess_word_rejects_already_guessed_letter(monkeypatch):
    answers = iter(["a", "b"])
    monkeypatch.setattr("builtins.input", lambda: next(answers))
    result = guess_word("a")
    assert result == "b"
    assert "⚠️  You've already guessed that letter, please guess a different letter! ⚠️"

"""
Given the users inputs a number a message is displayed to prompt user 
of error and how to correct. 
"""
def test_guess_word_rejects_number(monkeypatch):
    answers = iter(["7", "c"])
    monkeypatch.setattr("builtins.input", lambda: next(answers))
    result = guess_word("")
    assert result == "c"
    assert "⚠️  This has to be a letter! ⚠️"

"""
Given the users inputs a symbol a message is displayed to prompt user 
of error and how to correct. 
"""
def test_guess_word_rejects_symbol(monkeypatch):
    answers = iter(["%", "c"])
    monkeypatch.setattr("builtins.input", lambda: next(answers))
    result = guess_word("")
    assert result == "c"
    assert "⚠️  This has to be a letter! ⚠️"

