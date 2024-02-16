# hangman-aemckenna-project01
# CPSC 2030 (Proj_01)
Due: Friday, March 1st at 11:00am

# Overview:
The game known as Hangman is a guessing game in which one player selects a word that other players guess by offering a series of letters until the full word is revealed or a maximum number of guesses is reached.

# Contents: 
The zipped folder (‘CPSC 2030-Project 01’) contains the following files/folders:
- run.py
    - This file will run the game. I have provided initial settings that you will need to use to run the game.
    - Complete the 2 TODO statements
- game_manager.py
    - This file is used in run.py and relies on word_guesser.py and word_maker.py.
    - I have fully implemented this file, and you do not need to make any changes. Though it would be beneficial for you to place breakpoints and step through the control_loop() and run_game() functions.
- word_guesser.py
    - This file contains two classes: GameState and WordGuesserHuman.
- GameState
    - This class is used to track the mechanics of the game being played, such as what letters have been guessed, how many guesses are allowed, etc.
    - Complete the TODO statement in the __init__ function
- WordGuesserHuman
    - This class is used to prompt the user for the next letter to guess.
    - One of its properties is an instance of the GameState class, so that any input from the user can be retained and tracked.
    - Complete the 2 TODO statements for the reset and getGuess() functions.
- word_maker.py
    - This file contains two classes: WordMakerHuman and WordMakerAI.
    - WordMakerHuman
        - This class is used to prompt the user providing the secret word for the game.
        - We are going to be fair, so the word has to be present in the text file selected in run.py.
        - Notice how lines 50 + 51 in game_manager.py are working. The WordGuesser class gets the guess, and the WordMaker class finds where the guessed character is present in the word.
        - The __init__ function is completed for you and does not need to be modified.
    - Complete the 4 TODO statements for the reset(), getValidWord(), getAmountOfValidWords(), guess()functions.
- WordMakerAI
    - This class is fully implemented and you do not need to modify it in order to
use it. You may interact with it by setting ai = True in run.py.
    - This is a particularly devious “AI” agent though. Can you tell what it is doing?
- words
    - This folder contains three text files that are options to use as a “dictionary” for the given game depending on what difficulty you select in run.py.
    - It will be easiest to use debug_dict.txt as you are working through an initial implementation. But you should test your work against the other dictionaries as well when interacting with the AI agent.
    - Contents
        - debug_dict.txt 9 words, all 4 characters long
        - easy_dict.txt 75 words, 3 or 4 characters
        - hard_dict.txt 200 words, 3-5 characters
# Requirements
- Complete the TODO statements in the code + highlighted in the Contents section.
- Provide appropriate documentation in the form of docstrings for the function that you implement in WordGuesserHuman and WordMakerHuman.
- Use good programming style: appropriate + descriptive variable names, code comments for significant sections or operations, etc.
- Upload the four .py files and the words folder in one zipped folder: ‘project01-lastname.zip’
