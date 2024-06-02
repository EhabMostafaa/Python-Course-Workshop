import random

def guessing_game():
    random_number=random.randint(1,20)
    
    while True:
        guessed_number=int(input("guess number"))
        if guessed_number == random_number:
            print(f"guessed pass number is {guessed_number}")
            break
        elif guessed_number < random_number:
            print(f"guessed failed number, it is too low")
        elif guessed_number > random_number:
            print(f"guessed failed number, it is too high")
            
guessing_game()