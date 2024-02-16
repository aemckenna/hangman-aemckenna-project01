import game_manager as GM

# ------SETTINGS------
# should the words be provided by a human or selected by the computer?
ai = False

# if computer-generated, what difficulty level should it play at?
difficulty = input("What level of difficulty? (Debug, Easy, Hard) ")

# depending on the selection of difficulty, use the appropriate text file
word_locs = {"debug": "words/debug_dict.txt", "easy": "words/easy_dict.txt", "hard": "words/hard_dict.txt"}
words = word_locs[difficulty.lower()]

# how many guesses should be the maximum?
num_guesses = 10

# can modify this to see helpful information (such as how many words remain for a computer-generated word)
debug = True

# ------BEGIN GAME------
# create a new instance of GameManager using the appropriate settings above
pass # TODO: implement this

# run the control_loop() function of the new game
pass # TODO: implement this
