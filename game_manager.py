from word_maker import WordMakerAI, WordMakerHuman
from word_guesser import WordGuesserHuman

class GameManager():
    def __init__(self, ai, words_file, guesses, debug):
        self.starting = guesses
        self.words_file = words_file
        if ai:
            self.word_maker = WordMakerAI(words_file, debug)
        else:
            self.word_maker = WordMakerHuman(words_file, debug)
        self.word_guesser = WordGuesserHuman(guesses, words_file, debug)
        self.ai = ai
        self.debug = debug

    def control_loop(self):
        if self.ai:
            word_lengths = list(self.word_maker.words.keys())
        else:
            word_lengths = [len(word) for word in self.word_maker.words]

        MIN_WORD_LEN = min(word_lengths)
        MAX_WORD_LEN = max(word_lengths)

        while True:
            print("Let's play hangman!")

            while True:
                numS = input(f"How many characters should my word be? ({MIN_WORD_LEN}-{MAX_WORD_LEN}): ")
                try:
                    num = int(numS)
                    if num >= MIN_WORD_LEN and num <= MAX_WORD_LEN: break
                except:
                    pass
            self.run_game(num)
            ans = input("Would you like to play again? (y/n):")
            while ans not in ["y", "n"]:
                ans = input("Would you like to play again? (y/n):")
            if ans == "n": break

    def run_game(self, word_length):
        self.word_maker.reset(word_length)
        self.word_guesser.reset(word_length)

        while True:
            if self.word_guesser.state.num_guesses == 0:
                print(f"You lose! The word was {self.word_maker.getValidWord()}.")
                break
            self.word_guesser.state.print_state(self.word_maker.getAmountOfValidWords())
            inp = self.word_guesser.getGuess()
            letter_positions = self.word_maker.guess(inp)
            letter_count = len(letter_positions)
            if letter_count != 1:
                s = "s"
            else:
                s = ""
            print(f"Found {letter_count} '{inp}'{s}")

            self.word_guesser.state.num_guesses -= 1 if letter_count == 0 else 0
            self.word_guesser.state.guessed.append(inp)
            for i in letter_positions:
                self.word_guesser.state.word[i] = inp

            self.word_guesser.state.completed_letters += letter_count
            if self.word_guesser.state.completed_letters == word_length:
                left = self.starting - self.word_guesser.state.num_guesses
                es = "es" if left != 1 else ""
                print(f"You win in {left} incorrect guess{es}!")
                print("The word was {}".format("".join(self.word_guesser.state.word)))
                break