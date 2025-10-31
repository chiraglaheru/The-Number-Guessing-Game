[''' 
  ________ ____ ______________ _________ _________ .______________   ___ ___    _____ __________________   
 /  _____/|    |   \_   _____//   _____//   _____/ |   \__    ___/  /   |   \  /  _  \\______   \______ \  
/   \  ___|    |   /|    __)_ \_____  \ \_____  \  |   | |    |    /    ~    \/  /_\  \|       _/|    |  \ 
\    \_\  \    |  / |        \/        \/        \ |   | |    |    \    Y    /    |    \    |   \|    `   \
 \______  /______/ /_______  /_______  /_______  / |___| |____|     \___|_  /\____|__  /____|_  /_______  /
        \/                 \/        \/        \/                         \/         \/       \/        \/ 
''']

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

secret_number = random.randint(1, 100)

if level == 'easy':
    max_tries = 10
else:
    max_tries = 5  
tries_used = 0

while tries_used < max_tries:
    print(f"You have {max_tries - tries_used} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))  
    
    if guess == secret_number:
        print("Congratulations! You guessed it!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    tries_used += 1

if tries_used == max_tries and guess != secret_number:
    print(f"Game over! The number was {secret_number}")
