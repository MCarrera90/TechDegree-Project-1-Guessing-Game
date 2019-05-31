import random

number = random.randint(1, 11)

print("Welcome to the number guessing game!")

def start_game():
    guess = int(input("Pick a number between 1 and 10: "))
    attempt_count = 1
    while guess != number:
        if guess > number:
            print("It's lower")
            guess = int(input("Pick a number between 1 and 10: "))
        elif guess < number:
            print("It's higher")
            guess = int(input("Pick a number between 1 and 10: "))
        attempt_count += 1    
    else:
        print("Great job! you guessed correctly, it took {} tries.\nThanks for playing the game is over.".format(attempt_count))
        
    
   

if __name__ == '__main__':
    start_game()
