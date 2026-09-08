# this is a simple conditionalguessing game where the user has to guess a number between 1 and 10
print("Hello user, kindly answer the following questions candidly. Note that minors are exempted from this process.")
name = input("What is your First name: ")
name1 = input("What is your middle name: ")
name2 = input("What is your last name: ")
print(f"Hello, {name}")
age = int(input("How old are you: "))

if age < 0:
    print("Invalid age entered")
elif 0 <= age < 18:
    print("Sorry you are a minor and cannot proceed.")
elif age >= 18:
    print("Time to play a guessing game. If u win, you get $10, if you lose, You lose $10. You have three trials. Ready? ")
    special_number = 6
    tries = 3

    for i in range(tries):
        guess = int(input("Make a guess from 1- 10: "))
        if guess < special_number:
            print("Too low! Try again")
        elif guess > special_number:
            print("Too high! Try again")
        else:
            print("Congratulations, you guessed right! You have now earned $10")
            break
    else:
        print(f"Game over! You owe us $10. The special number was {special_number}")
