class GameState():
    def __init__(self, guesses, word_length, debug):
        self.word = ["-"] * word_length         # a new game should have enough blank spaces ("-") for each letter in the word
        self.debug = debug                      # a T/F boolean value for whether or not we are in debug mode

        #   when a new game is started, set the following properties:
        self.word_length = word_length          # --how many letters should be in the word?
        self.guessed = []                       # --a list of guessed characters
        self.num_guesses = guesses              # --the total number of allowable guesses
        self.completed_letters = 0              # --the number of the correctly-gessed letters

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
        self.words_file = words_file

    def reset(self, word_length):
        # update the state property of the instance to reflect a new GameState 
        self.state = GameState(guesses=self.guesses, word_length=word_length, debug=self.debug)
    def getGuess(self):
        while True:
        # prompt the user to provide a new character to guess
            char = input("Guess a new character:").lower()
        #   --confirm that there is only 1 character
            if len(char) != 1:
                print("Pleas only enter one character")
                continue
            #   --confirm that the character is a letter (not a digit, symbol, etc.)
            if not char.isalpha():
                print("Please enter a letter")
                continue
            #   --confirm that the character has not be previously guess
            if char in self.state.guessed:
                print("You have already guessed that letter.")
                continue
            break
        #   this function should return that single character
        return char 