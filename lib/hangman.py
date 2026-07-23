import random
import string

class Hangman:

#global varibles
    HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

word_bank = "aardvark alligator alpaca badger bear beaver cat canary cow donkey deer dog elephant elk eagle ferret fish flamingo giraffe goat goose hippopotamus hedgehog hamster iguana impala ibex jellyfish jaguar jackal kangaroo koala kookaburra lemur llama lion monkey meerkat mouse newt narwhal nighthawk otter owl octopus panda penguin pig quokka quail quetzal raccoon rabbit rhinoceros seal snake salmon tiger tortoise toucan unicornfish umbrellabird viper vulture    walrus wolverine wombat yak yellowjacket yellowhammer zebra zebu".split()     
   
BOLD = '\033[1m'
END = '\033[0m'

#def __init__(self, [word_bank], secret_word = None):
    

# This function will return a random string from a list of strings.
def get_random_word(wordList):
    #this is going through word_bank one word at a time to end of list.
    wordIndex = random.randint(0, len(wordList)-1) 
    #this is returning the random word 
    return wordList[wordIndex] 

# This function will return entered user name with welcome message. 

def enter_name():
    name = input("What is your name? ").strip()#.strip in case user adds extra space
    if name == "": 
        name = "Player"
    print()
    print(f" 🤗 Welcome to the game {name}!! 🤗\n")   
    print("How to play Hangman 🕹️: \n\n The computer thinks of a secret word and displays a row of blank dashes on the screen representing the individual letters.\n\n The player guesses one letter that they think is in the word and the computer notifies the player if this is the correct guess by filling in the space that represents the letter. \n\n If the letter is not in the secret word, the computer displays the incorrect letter and displays a single body part of the hangman.\n\n The player has 6 incorrect guesses per word.\n\n The player wins if they figure out the word before the full hangman is displayed and the computer wins if the drawing is complete.") 
    return name
      
# This function will display the game board
#def display_board(self):