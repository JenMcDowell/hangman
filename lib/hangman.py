import random
import string

word_bank = "aardvark alligator alpaca badger bear beaver cat canary cow donkey deer dog elephant elk eagle ferret fish flamingo giraffe goat goose hippopotamus hedgehog hamster iguana impala ibex jellyfish jaguar jackal kangaroo koala kookaburra lemur llama lion monkey meerkat mouse newt narwhal nighthawk otter owl octopus panda penguin pig quokka quail quetzal raccoon rabbit rhinoceros seal snake salmon tiger tortoise toucan unicornfish umbrellabird viper vulture walrus wolverine wombat yak yellowjacket yellowhammer zebra zebu".split()

class Hangman:

#global variables
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

    def __init__(self, word_bank, secret_word=None):
        self.word_bank = word_bank

        if secret_word is not None:
            self.secret_word = secret_word
        else:
            self.secret_word = random.choice(self.word_bank)

        self.missed_letters = ""
        self.correct_letters = ""
        self.game_status = False

# word_bank = "aardvark alligator alpaca badger bear beaver cat canary cow donkey deer dog elephant elk eagle ferret fish flamingo giraffe goat goose hippopotamus hedgehog hamster iguana impala ibex jellyfish jaguar jackal kangaroo koala kookaburra lemur llama lion monkey meerkat mouse newt narwhal nighthawk otter owl octopus panda penguin pig quokka quail quetzal raccoon rabbit rhinoceros seal snake salmon tiger tortoise toucan unicornfish umbrellabird viper vulture walrus wolverine wombat yak yellowjacket yellowhammer zebra zebu".split()     

BOLD = '\033[1m'
END = '\033[0m'    

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

#end is used for the addition of any string at the end of the output of the python print statement and 
#by default a new line char is added by the print()

#empty prints are used here to give additional space (new line)

def display_board(missed_letters, correct_letters, secret_word):
    print(Hangman.HANGMAN_PICS[len(missed_letters)])
    print()
    print("Your missed letters are:", end = " ")
    for letter in missed_letters:
        print(BOLD + letter, end = " " + END)
    print()
    blank = "_" * len(secret_word)
    #getting the rage of secret word and replace blanks with correctly guessed letters:
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blank = blank[:i] + secret_word[i] + blank[i + 1:] 
    #this for loop will show the secret_word with spaces in between each letter
    print()
    print("Your word is:\n\n")
    for letter in blank:
        print(BOLD + letter, end = " "+ END)
    print()
    print()

#This function will return the letter that the player has entered and 
#will also make sure that the player had entered a single letter and nothing additional.

def guess_word(already_guessed):
    while True:
        print("Please guess a letter 🔤 :")
        guess = input() 
        guess = guess.lower()
        if len(guess) != 1:
            print("⚠️  Please enter a single letter. ⚠️")
        elif guess in already_guessed:
            print("⚠️  You've already guessed that letter, please guess a different letter! ⚠️")
        elif guess not in string.ascii_lowercase:
            print("⚠️  This has to be a letter! ⚠️")
        else:
            return guess
        
#This function will return True if the player wants to play again
#Otherwise it will return False if the player doesn't want to play.

def reset_game():
    print("Do you want to play again? Y/N")
    return input().lower().startswith("y")

def main():

    #Declaring variables that will be used in the game
    missed_letters = ""
    correct_letters = ""
    secret_word = get_random_word(word_bank)
    game_status = False

    #This while loop iterates over the secret word to determine if guess is a letter in the word. 
    # If it set completed_words to True, otherwise reassign to False. 
    enter_name()
    while True:
        display_board(missed_letters, correct_letters, secret_word)
        guess = guess_word(missed_letters + correct_letters)
        if guess in secret_word:
            correct_letters = correct_letters + guess
            #This will check if the player has won the game
            completed_word = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    completed_word = False
                    break
            if completed_word:
                print("🎉🎉🎉 Congratulations, the secret word is: ' " + BOLD + secret_word + " ' You've won the game!! 🎉🎉🎉"+ END)
                game_status = True
        else:
            missed_letters = missed_letters + guess
            if len(missed_letters) == len(Hangman.HANGMAN_PICS) -1:
                display_board(missed_letters, correct_letters, secret_word) # edited this line because we had display_board(missed_letters, completed_word, secret_word) which was calling completed_word as a variable
                print("😵 You ran out of guesses! After " + str(len(missed_letters)) + " guesses. You have lost the game! 😵 \n\n The correct word was: " +  BOLD + secret_word + END)
                game_status = True
        if game_status:
            if reset_game():
                missed_letters = ""
                correct_letters = ""
                secret_word = get_random_word(word_bank)
                game_status = False
            else:
                break

if __name__ == "__main__":
    main()




# enter_name()

# display_board(missed_letters="rtg", correct_letters="ca", secret_word="cat")
# guess(already_guessed= "ca") 
#def display_board(self):