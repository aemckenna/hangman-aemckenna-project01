import random

class WordMakerHuman():
    def __init__(self, words_file, debug):
        self.debug = debug
        self.words = {}
        with open(words_file) as wordfile:
            for line in wordfile:
                word = line.strip()
                if len(word) > 0:
                    self.words[word] = True

    def reset(self, word_length):
        # allow player #1 to provide a word for player #2 to guess
        # we want to be fair, so make sure the word provided has the same number of characters as the `word_length` variable
        # the word selected should be preserved in the `word` property of the instance
        self.word = input("Player #1, provide a word for Player #2 to guess:").lower().strip()

        while len(self.word) != word_length:
            print(f"The word provided must have {word_length} characters.")
            self.word = input("Please provide a word with the corect number of charaters").lower().strip()

    def getValidWord(self):
        # what should we return here?
        valid_word = random.choice(list(self.words.keys()))
        return valid_word
    
    def getAmountOfValidWords(self):
        # what should we return here?
        return len(self.words)

    def guess(self, guess_letter):
        # find how many instances of the `guess_letter` parameter occur in the word
        # return a list of one or more index positions where the letter matches
        # i.e. the word ELSE should return [0, 3] when the guess_letter is e
        positions = [i for i, letter in enumerate(self.word) if letter == guess_letter]
        return positions

class WordMakerAI():    
    """
    A class used to generate words that maximize the inability for the user to correctly guess a word. Also known as "evil hangman".

    Attributes
    ----------
    words_file : str
        path to the location of the dictionary
    words: dict
        a container for the list of words provided
    current_words: dict
        a container for the list of words matching the length of the word identified by the user

    """
    def __init__(self, words_file, debug):
        """
        Parameters
        ----------
        words_file : str
            the filename for the dictionary to use in the game
        debug : bool
            a flag to switch to debug mode
        """
        self.debug = debug
        self.words = {}                             # dictionary to hold words of various lengths
        self.current_words = {}                     # dictionary to hold words of length in the specific session of the game

        with open(words_file) as wordfile:
            for line in wordfile:
                word = line.strip()
                length = len(word)                  # find the length of the current word
                if length> 0:
                    if length not in self.words:    # create a new key in the dictionary, if a word of that length hasn't been processed yet
                        self.words[length] = {}

                    self.words[length][word] = True # an initial value to store the word in the dictionary, preferred over list to retain O(1) lookup
                    

    def reset(self, word_length):
        """
        This method is called when a new game is started. It will always be called before guess() or getValidWord()

        Parameters
        ----------
        word_length : int
            the length of valid words identified by the user when the game is reset

        """
        # given the selected word length, retrieve the corresponding dictionary
        # store in a new dictionary to preserve the original values for subsequent games
        self.current_words = self.words[word_length]    

    def getValidWord(self):
        """
        This method is called when the user runs out of guesses without identifiying the word.

        Returns
        -------
        string
            the first item in the remaining list of valid keys
        """
        # convert the remaining valid keys to a list and return the first element
        # safe assumption given that at least one word must exist if the user failed to correctly guess
        words_list = list(self.current_words.keys())
        return words_list[0]

    def getAmountOfValidWords(self):
        """
        This method is called when running in debug mode. It shows the count of remaining valid words since the last reset() call.

        Returns
        -------
        integer
            the count of remaining valid words
        """
        # find the length of the dictionary that contains the remaining valid words
        return len(self.current_words)

    def guess(self, guess_letter):
        """
        This method is called to process the next letter provided by the user.
        
        Parameters
        ----------
        guess_letter : char
            the next letter guessed by the user, converted to lowercase in word_guess.getGuess()

        Returns
        -------
        list
            the list of positions in which the letter is found that creates the largest set of remaining valid words

        """      
        current_keys = self.current_words.keys()                # retrieve all the valid words of the appropriate length for this session

        # for every valid word in the current session
        for key in current_keys:
            # check each character in the valid word and see if it matches the guessed_letter
            # if match, retain the position in a list (to account for multiple occurences of a letter in a word)
            location = [position for position, character in enumerate(key) if character == guess_letter]
            self.current_words[key] = tuple(location)           # convert the list to a tuple and update the value in the current session dictionary 

        current_sequence_dict = {}                              # new dictionary to track the position of guessed letters in valid words
        
        # iterate over every tuple of positions of guessed letters to find which sequence creates the largest remaining set of words
        for value in self.current_words.values():
            if value not in current_sequence_dict.keys():       # if the sequence hasn't been seen, create a new entry and set count to 1
                current_sequence_dict[value] = 1
            else:
                current_sequence_dict[value] += 1               # if the sequence was previously seen, increase the count

        # find the sequence of positions of characters that retains the most words 
        max_sequence_value = max(current_sequence_dict.values())

        # possible that multiple sequences could retain the same max size of words
        # iterate through the dictionary and retain all the keys retaining max size of words
        max_key_indexes = [k for k,v in current_sequence_dict.items() if v == max_sequence_value]

        # in the event of multiple sequences, ensure that we retain the one that reveals the least amount of characters
        max_sequence_key = min(max_key_indexes, key = len)               

        new_dictionary = {}
        # now that we know what position of letters we need to retain
        # iterate through the dictionary and save all the corresponding words to a new dictionary
        for key, value in self.current_words.items():
            if (value == max_sequence_key):
                new_dictionary[key] = value
        
        # replace the current words with the remaining applicable words
        self.current_words = new_dictionary

        # return the position of characters that retains the most words as a list
        return list(max_sequence_key)