import random
secret_number = random.randint(1,100)



print('Lets play guessing game! Guess a number between 1 and 100. You have 5 attempts.')

num_guesses = 5


while True:
    guess = int(input('Enter your guess: '))
   
    num_guesses -= 1
    
    if guess == secret_number:
        print('You won!')
        break
    elif num_guesses == 0:
        print('Better luck next time!')
        break
    elif guess > secret_number:
        print ("Wrong guess!Guess lower!")
    elif guess < secret_number:
        print ("Wrong guess!Guess higher!")    
    
    print('Number of guesses remaining = ' + str(num_guesses))

print('Secret number = ' + str(secret_number))
