#variable set to 5
guess_me = 5

#loop to guess in range(10) til it correctly guesses number
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break