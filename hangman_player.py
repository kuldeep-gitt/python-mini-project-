import hangman_creator

hangman = hangman_creator.Hangman('d://wordlist.txt')
hangman.choose_the_word()
hangman.fill_the_word_status()


while True:
    hangman.get_word_status()
    hangman.guess_the_letter()

    if hangman.attempts_remaining == 0:
        print("out of attempts.the word was{}.game over!".format(hangman.chosen_word))

        break

    elif hangman.chosen_word == ''.join(hangman.word_status):
        print("Hurray!You won the game!")
        break