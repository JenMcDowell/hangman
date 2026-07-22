import random

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
   

#def __init__(self, [word_bank], secret_word = None):
    

# This function will return a random string from a list of strings.
def get_random_word(wordList):
    #this is going through word_bank one word at a time to end of list.
    wordIndex = random.randint(0, len(wordList)-1) 
    #this is returning the random word 
    return wordList[wordIndex] 

# This function will return entered user name with welcome message. 
def enter_name():
    name = input("what is your name?").strip()
    if name == "": 
        name = "Player"
    print(f"Welcome to the game {name}!! 🤗")    
    return name
    
    
# This function will display the game board
#def display_board(self):