import random
target = random.randint(1, 100)
guess = int(input("Guess the number between [1, 100]: "))
while True:
    if(guess == target):
        print("Congratulations you guessed the number!")
        break
    if(guess < target):
        guess = int(input("increase your guess: "))
    if(guess > target):
        guess = int(input("decrease your guess: "))