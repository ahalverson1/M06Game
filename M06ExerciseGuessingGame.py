#define variables
word = 'puppy'
letters = len(word)

print(f'There are ' + str(letters) + ' letters in this word')

num_guesses = 7
guesses = []
win_game = False

while win_game == False and num_guesses > 0:
    user_input = input('Enter a letter: ')
    guess = str(user_input.lower())
    guess_word_result = ''
    guesses = ''
    if type(user_input) is int:
        guess_word_result = 'Please input a letter or word guess.'
    if guess == word:
        guess_word_result = 'Correct word! You win!'
        win_game = True
    elif user_input is not int and guess in guesses:
        guess_word_result = 'You have already guessed this letter. Pick again.'
    elif user_input is not int and guess in word:
        guess_word_result = 'Good guess!'
        print(num_guesses)
    elif user_input is not int and guess not in word:
        num_guesses -= 1
        guess_word_result = 'Wrong guess.'
        print(f'You have ' + str(num_guesses) + ' guesses left.')
    else:
        guess_word_result = ''

    print(guess_word_result)

if win_game == False and num_guesses == 0:
    print('Game over.')
        
