class GameState():
    def __init__(self, guesses, word_length, debug):
        self.word = ["-"] * word_length         # a new game should have enough blank spaces ("-") for each letter in the word
        self.debug = debug                      # a T/F boolean value for whether or not we are in debug mode

        pass # TODO: implement this
        #   when a new game is started, set the following properties:
        #   word_length         --how many letters should be in the word?
        #   guessed             --a list of guessed characters
        #   num_guesses         --the total number of allowable guesses
        #   completed_letters   --the number of the correctly-gessed letters
        

    def print_state(self, wordsRemaining):
        if not self.debug:
            wrStr = ""
        else:
            wrStr = f" ({wordsRemaining} words remain)"

        print(f"\nYou have {self.num_guesses} incorrect guesses left{wrStr}.")
        used_letters = " ".join(self.guessed)
        print(f"Used letters: {used_letters}")

        print("Word: {}".format("".join(self.word)))

class WordGuesserHuman():
    def __init__(self, guesses, words_file, debug):
        self.debug = debug
        self.guesses = guesses

    def reset(self, word_length):
        # update the state property of the instance to reflect a new GameState 
        pass # TODO: implement this

    def getGuess(self):
        # prompt the user to provide a new character to guess
        #   --confirm that there is only 1 character
        #   --confirm that the character is a letter (not a digit, symbol, etc.)
        #   --confirm that the character has not be previously guess
            
        #   this function should return that single character
        pass # TODO: implement this
 