import random

#file
filepath = "words_alpha.txt"
f = open(filepath, 'r')
#create word list
wordList = f.readlines()
# close file
f.close()

#define variables
word = random.choice(wordList).strip()
letters = (len(word))
print(word)

print(f'There are ' + str(letters) + ' letters in this word')

num_guesses = 7
lettersGuessed = ''
win_game = False

while win_game == False and num_guesses > 0:
    user_input = input('Enter a letter: ')
    guess = str(user_input.lower())
    guess_word_result = ''
    if user_input.isalpha() is False or len(guess) > 1:
        print('Please input a letter.')
    else:
        if guess == word:
            guess_word_result = 'Correct word! You win!'
            win_game = True
        elif user_input is not int and guess in lettersGuessed:
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
    print("")

    if wrongLetterCount == 0:
        print(f"Congrats! The word was {word}.")
if win_game == False and num_guesses == 0:
    print('Game over.')
        
