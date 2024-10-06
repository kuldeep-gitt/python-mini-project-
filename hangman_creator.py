import random
import re


class Hangman:

    def __init__(self, wordlist):

        self.wordlist = wordlist
        self.attempts_remaining = 6
        self.current_letter = ''
        self.chosen_word = ''
        self.guessed_letters = []

    def choose_the_word(self):
        file = open(self.wordlist)
        word = file.read().split('\n')
        word_count = len(word)
        self.chosen_word = word[random.randrange(0, word_count)]
        self.word_status = ['_' for i in range(len(self.chosen_word))]

    def fill_the_word_status(self):
        nos = random.randrange(1, 3)
        for i in range(nos):
            position = random.randrange(0, len(self.chosen_word))
            self.word_status[position] = self.chosen_word[position]

    def guess_the_letter(self):
        letter = input("Guess the letter:")
        if (letter in self.guessed_letters):
            print("you have already guessed that letter. your guesses:{}".format(','.join(self.guessed_letters)))
            return
        self.guessed_letters.append(letter)
        occurrences = []
        occurence = re.finditer(letter, self.chosen_word)

        for m in occurence:
            occurrences.append(m.start())

            if (len(occurrences) == 0):
                self.attempts_remaining -= 1
                print("oops ! Your guess was wrong.Attempts remaining is{}".format(self.attempts_remaining))

            else:
                for position in occurrences:
                    self.word_status[position] = self.chosen_word[position]
                    print("correct word!")

    def get_word_status(self):
        print("current.status:{}\n".format(','.join(self.word_status)))
