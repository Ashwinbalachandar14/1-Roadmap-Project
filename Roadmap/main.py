import random
NUMBER=random.randint(1,101)
EASY_ATTEMPTS=10
HARD_ATTEMPTS=5
def easy():
    global EASY_ATTEMPTS
    while EASY_ATTEMPTS>0:
        print(f"You have {EASY_ATTEMPTS} attempts to get the number:")
        guess=int(input("Make a guess:"))
        if guess>NUMBER:
            print("Too High")
            EASY_ATTEMPTS-=1
            if EASY_ATTEMPTS==0:
                print(f"You Lose and the Number is :{NUMBER} ")
            easy()
        elif guess==NUMBER:
            print(f"You Got it! The Number is {guess}")
            EASY_ATTEMPTS=0
        else :
            print("Too Low")
            EASY_ATTEMPTS-=1
            if EASY_ATTEMPTS==0:
                print(f"You Lose and the Number is :{NUMBER} ")
            easy()


def hard():
    global HARD_ATTEMPTS
    while HARD_ATTEMPTS>0:
        print(f"You have {HARD_ATTEMPTS} attempts to get the number:")
        guess=int(input("Make a guess:"))
        if guess>NUMBER:
            print("Too High")
            HARD_ATTEMPTS-=1
            if HARD_ATTEMPTS==0:
                print(f"You Lose and the Number is :{NUMBER} ")
            hard()
        elif guess==NUMBER:
            print(f"You Got it! The Number is {guess}")
            HARD_ATTEMPTS=0
        else :
            print("Too Low")
            HARD_ATTEMPTS-=1
            if HARD_ATTEMPTS==0:
                print(f"You Lose and the Number is :{NUMBER} ")
            hard()
print("Welcome to the number guessing game!")
print("I'm thinking to guess the number between 1 to 100")
user_input=input("Choose your Difficulty level: Type 'easy' or 'hard':").lower()
if user_input=="easy":
    easy()
else:
    hard()