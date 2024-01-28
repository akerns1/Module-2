import random

#Generating secret and guess values
secret = random.randint(1,10)
guess = random.randint(1,10)

#printing secret and guess values
print("Guess value is = ", guess)
print("Secret value is = ", secret)

#creating too low
if guess < secret:
    print("too low!")

#creating too hight
elif guess > secret:
    print("too high!")
    
#print command for getting the answer correct
else:
    print("just right!")