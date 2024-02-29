import game_manager as GM

# ------SETTINGS------
ai = False                                                                                                       # should the words be provided by a human or selected by the computer?
difficulty = input("What level of difficulty? (Debug, Easy, Hard) ")                                             # if computer-generated, what difficulty level should it play at?
word_locs = {"debug": "words/debug_dict.txt", "easy": "words/easy_dict.txt", "hard": "words/hard_dict.txt"}      # depending on the selection of difficulty, use the appropriate text file
words = word_locs[difficulty.lower()]
num_guesses = 10                                                                                                 # how many guesses should be the maximum?
debug = False                                                                                                    # can modify this to see helpful information (such as how many words remain for a computer-generated word)

# ------BEGIN GAME------
# create a new instance of GameManager using the appropriate settings above
my_game = GM.GameManager(ai, words, num_guesses, debug)

# run the control_loop() function of the new game
my_game.control_loop()