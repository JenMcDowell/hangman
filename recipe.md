# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As the user
I want to play a game of hangman where I guess the letters of a mystery word 
and for incorrect responses I decrease the number of incorrect response I can have.  

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Hangman:
    # User-facing properties:
    #   secret_word: str (word we are trying guess)
    #   missed_letters: str (incorrect guesses)
    #   correct_letters: str (correct guess, print out of ___ with correct letters)    
    #   boolean if game is finished (Game over (won_game), when users looses (lost_game); for winner, You won with "celebration")
    #   set maximum (6) number of incorrect guesses ("you have made "5" incorrect guesses")
    #   greeting of player after name entry
    
    def __init__([word_bank], secret_word = None):  #Python random library to help with picking of secret word
        # Parameters:
        #   word_bank: list of str from which a secret word is selected
        #   secret_word: str 
        # Side effects:
        #   Sets the name property of the self object and choose random word from word bank if secret word is set to none
        #   game_status should be set to false
        pass # No code here yet

    def enter_name(name):
        # Parameters:
        #   name: string representing users name
        # Returns:
        #   users name with welcome message (Welcome Alicja!)
        # Side-effects
        #   Print the statement from name entered in: "Welcome Jennifer, Daphna, and Alicja!" 
        pass # No code here yet

    def guess_word(letter):
        # Parameters: 
        #   letter: string representing the guessed letter
        # Returns:
        #   correct will change string showing dashes and correct letter
        #   incorrect if not in secret word and print letters not used
        #   Win/Lose: boolean 
        #       Won: guess word with all correct letters 
        #       Lose: when used up all missed letters
        # Side-effects:
        #   add correct guess to list of correct letters
        #   add incorrected to list of missed letters
        #   Says game complete at end: 
        #       Game is won
        #       Game is lost/over
        pass # No code here yet

    def display_board(self):
        # Parameters: 
        #   missed_letters, correct_letters, secret_word 
        # Returns:
        #   hangman (body parts) picture for the missed guess  (No incorrect guesses will have empty stand)
        #   returned missed letters to remind user of letters used
        #   partially uncovered word with the correct guesses (_ a _, underscore for missing letters and correct letters)
        # Side-effects:
        #   None
        pass # No code here yet

        def won_game():
        # Parameters: 
        #   self 
        # Returns:
        #   True if every letter in the secret word was guessed.
        #   Print "You WON!!!" with celebration 🎉
        # Side-effects:
        #   None
        pass # No code here yet

        def lost_game():
        # Parameters: 
        #   self 
        # Returns:
        #   False if all guesses are used and user did not guess the secret word
        #   Print "You LOST! with sad face 😞 
        # Side-effects:
        #   None
        pass # No code here yet

        def reset_game(secret_word = None):
        # Parameters: 
        #   self 
        # Returns:
        #   secret_word: str 
        # Side effects:
        #   Sets the name property of the self object and choose new random word from word bank if secret word is set to none
        #   secret word is replace with new word
        #   set game_status to false (local variable inside main game)
        pass # No code here yet

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a secret word the game is in an empty state initizes with no incorrect or correct guess (_ _ _)
"""
def test_game_starts_empty_state():
    game = Hangman(["cat"], secret_word = "cat")
    assert game.secret_word == "cat"
    assert game.missed_letters == ""
    assert game.correct_letters == ""
    assert game_status == False

"""
Given a word list (we will provide) no secret_word selected the game will choose one of the words provided [word_bank] (testing able to pull word from word bank)
"""
def test_pull_from_word_bank():
    game = Hangman(["cat", "dog", "rat"])
    assert game.secret_word is in ["cat", "dog", "rat"]

"""
Given the users guesses a correct letter record and report the correct guess
"""
def test_correct_letter():
    game = Hangman(["cat"], secret_word = "cat")
    result = game.guess("a")
    assert result == "You guessed correctly"
    assert game.correct_letter == "a"
    assert game.missed_letter == ""

"""
Given the users guesses an incorrect letter record and report the incorrect guess
"""
def test_correct_letter():
    game = Hangman(["cat"], secret_word = "cat")
    result = game.guess("y")
    assert result == "You guessed correctly"
    assert game.missed_letter == "y" 
    assert game.correct_letter == ""   

"""
Give an uppercase letter, the letter is convert and reported as a correct guess
"""
def test_normlize_an_uppercase_letter():
    game = Hangman(["cat"], secret_word = "cat")
    result = game.guess("A")
    assert result == "You guessed correctly"
    assert game.correct_letter == "a"

"""
Given a non-alphabetical char guess, guess will be rejected 
with a error statment.
"""
def test_nonalpha_rejected():
    game = Hangman(["cat"], secret_word = "cat")   
    with pytest.raises(ValueError, match "You need to enter a letter"):
        game.guess("3") # will still raise error the same if number or symbol

"""
Given correct and incorrect guesses the display board will display correct_letters and missed_letters 
"""
def test_display_board_state():
    game = Hangman(["cat"], secret_word = "cat") 
    game.guess("t")
    game.guess("g")
    board = game.display_board()
    assert "Missed Letters: g" in board 
    assert "_ _ t" in board

"""
Given an empty string, guess will be rejected with a error statment.
"""
def test_empty_string():
    game = Hangman(["cat"], secret_word = "cat")   
    with pytest.raises(ValueError, match "You did not enter a letter, please enter a letter."):
        game.guess("") 

"""
Given a letter that has been guessed already, guess will be rejected with error statement
"""

def test_already_guessed_letter():
    game = Hangman(["cat"], secret_word = "cat")   
    with pytest.raises(ValueError, match "You have already guessed this letter, please enter a different letter."):
        game.guess("c")         

"""
If a words contains a letter multiple times, all space of that letter will be filled
"""
def test_letter_that_repeats():
    game = Hangman(["llama"], secret_word = "llama")
    game.guess("l")
    assert "l l _ _ _" in game.display_board()

"""
Given that the player has correctly guessed all letters in the word
the game will print out "🎉 You Win! 🎉" 
"""    
def test_player_wins():
    game = Hangman(["cat"], secret_word = "cat") 
    game.guess("c")
    game.guess("a")
    result = game.guess("t")
    assert result == "🎉 You Win! 🎉"
    assert game.won_game is True
    assert game.lost_game is False

"""
Given that the player has used their maximum of incorrect guesses (6)
the game will print out "You Lost!" 
"""    
def test_player_looses():
    game = Hangman(["cat"], secret_word = "cat") 
    missed_letters("sefrwd")
    for letter in missed_letters[:-1]:
        assert game.guess(letter) == "incorrect" 
    result = game.guess(missed_letters[-1])
    assert result == "😩 You Lost! 😩"
    assert game.lost_game is True
    assert game.won_game is False

"""
Given an empty word bank an error will be raised
"""
def test_game_will_not_start_without_word_bank():
    with pytest.raises(ValueError, match = "Game will not start without wordbank. \nPlease insert a list of words of your chosen category."):
        Hangman([]) #self.word_bank

"""
Given end of game the game board will reset and a new game will start.
"""
def test_reset_board():
    game = Hangman(["cat", "dog"], secret_word = "cat")
    game.guess("c")
    game.guess("a")
    game.guess("t")
    game.reset_game(secret_word = "dog")
    assert game.secret_word == "dog"
    assert game.missed_letters == ""
    assert game.correct_letters == ""
    assert game_status == False 


