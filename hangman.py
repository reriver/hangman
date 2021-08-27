import random


def copy_chars(word, user_letter, word_to_print):
    for i in range(0, len(word)):
        if user_letter == word[i]:
            word_to_print[i] = user_letter[0]


def play_hangman():
    attempt = 8
    words = ['python', 'java', 'kotlin', 'javascript']
    random.seed(a=None, version=2)
    word = list(random.choice(words))

    word_to_print = list('-' * len(word))
    user_input_set = set()

    while attempt > 0:
        print()
        print(''.join(word_to_print))

        user_letter = input('Input a letter: ')

        if len(user_letter) != 1:
            print('You should input a single letter')
            continue

        if user_letter in user_input_set:
            print('You\'ve already guessed this letter')
            continue
        user_input_set.add(user_letter)

        if not user_letter.islower():
            print('Please enter a lowercase English letter')
            continue

        if user_letter in word:
            for i in range(0, len(word)):
                if user_letter == word[i]:
                    word_to_print[i] = user_letter[0]
            if word_to_print == word:
                break
        else:
            print("That letter doesn't appear in the word")
            attempt -= 1

    if word_to_print != word:
        print('You lost!')
    else:
        print('You guessed the word!')
        print('You survived!')


answer = ""
print("H A N G M A N")
while answer != 'exit':
    answer = input('Type "play" to play the game, "exit" to quit: ')
    if answer == 'play':
        play_hangman()
