#guess me and number values
guess_me = 7
number = 1

#while loop to guess number
while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    
#increment number by 1
    number += 1