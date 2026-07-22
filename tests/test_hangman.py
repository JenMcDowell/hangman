import pytest
from lib.hangman import Hangman 

"""
Given a secret word the game is in an empty state initizes with no incorrect or correct guess (_ _ _)
"""
def test_game_starts_empty_state():
    game = Hangman(["cat"], secret_word = "cat")
    assert game.secret_word == "cat"
    assert game.missed_letters == ""
    assert game.correct_letters == ""
    assert game_status == False
