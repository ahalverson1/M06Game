import random

#file
filepath = "words_alpha.txt"
f = open(filepath, 'r')
#create word list
wordList = f.readlines()
# close file
f.close()

winCount = 0
loseCount = 0

#function definition
def getWord():
    word = random.choice(wordList).strip()
    letters = len(word)
    print(f'There are ' + str(letters) + ' letters in this word. You will start with 7 guesses.')
    return word

#game framework
def playGame():
    num_guesses = 7
    winCount = 0
    loseCount = 0
    word = getWord()
    win_game = False
    lettersGuessed = ''
    while win_game == False and num_guesses > 0:
        user_input = input('  Enter a letter: ')
        guess = str(user_input.lower())
        guess_word_result = ''
        if user_input.isalpha() is False or len(guess) > 1:
            print('Please input a letter.')
        else:
            if user_input is not int and guess in lettersGuessed:
                guess_word_result = 'You have already guessed this letter. Pick again. You have ' + str(num_guesses) + ' guesses left.'
            elif user_input is not int and guess in word:
                guess_word_result = 'Good guess! You have ' + str(num_guesses) + ' guesses left.'
            elif user_input is not int and guess not in word:
                num_guesses = num_guesses - 1
                guess_word_result = 'Wrong guess. You have ' + str(num_guesses) + ' guesses left.'
            else:
                guess_word_result = ''

        print(guess_word_result)

        lettersGuessed = lettersGuessed + guess
        wrongLetterCount = 0

        for letter in word:
            if letter in lettersGuessed:
                print(f'{letter}', end="")
            else:
                print("_", end="")
                wrongLetterCount += 1
    else:
        if num_guesses == 0:
            print('  Game over. The word was ' + word)
            loseCount += 1
            print('Wins: ' + str(winCount))
            print("")
            print('Losses: ' + str(loseCount))
            playAgain = input('Would you like to play again? Yes/No  ')
            if 'y' in playAgain:
                playGame()
            else:
                print('Goodbye!')
        if win_game == True or wrongLetterCount == 0:
            print('Congrats! The word was ' + word)
            winCount += 1
            print('Wins: ' + str(winCount))
            print('Losses: ' + str(loseCount))
            playAgain = input('Would you like to play again? Yes/No')
            if 'y' in playAgain:
                playGame()
            else:
                print('Goodbye!')

playGame()