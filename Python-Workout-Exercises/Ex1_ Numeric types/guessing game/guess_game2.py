import random

def guessing_game():
    random_number=random.randint(1,50)
    count=3
    while count>0:
        guessed_number=int(input("guess number "))
        count-=1
        if guessed_number == random_number:
            print("guessed pass number is {0}".format(guessed_number))
            break
        elif (guessed_number - random_number) < 10:
            print(f"guessed failed number, it is too near , make it little smaller")
        elif (guessed_number - random_number) < 20:
            print(f"guessed failed number, it is far , make it more smaller")
        elif (guessed_number - random_number) < 30:
            print(f"guessed failed number, it is too far , make it most smaller")
        elif (random_number - guessed_number) < 10:
            print(f"guessed failed number, it is too near , make it little bigger")
        elif (random_number - guessed_number) < 20:
            print(f"guessed failed number, it is far , make it more bigger")
        elif (random_number - guessed_number) < 30:
            print(f"guessed failed number, it is too far , make it most bigger")
        
    if count == 0:
        print(f"enta 3beat fe Dmagk")
 
guessing_game()