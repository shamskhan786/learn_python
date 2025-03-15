import random

# # Number Guessing Game
# print("Welcome to the game, this is a number guessing game! \n you got 5 attemts to guess the number between 50 and 100, lets start game: ")

# number_guessing = random.randrange(50,100)
# # Chances
# chances = 5
# guess_counter = 0

# while guess_counter < chances:
#     guess_counter += 1
#     my_number = int(input("Enter your guess:"))

#     if my_number == number_guessing:
#         print(f"The number is {number_guessing} you found is right!! in the  {guess_counter} attempt"
          
#     )
#         break

#     elif guess_counter >= chances and my_number != number_guessing:
#         print(f"Oops sorry,the number is {number_guessing}better luck next time!  ")

#     elif my_number > number_guessing:
#         print("Your guess very High! Try again")

#     elif my_number < number_guessing:
#         print("Your guess very Low! Try again")  
      




print("Welcome to the game, this is a number guessing game! \n you got 5 attemts to guess the number between 50 and 100, lets start game: ")

number_to_guessing = random.randrange(50,100)

chances = 5
guess_count = 0

while guess_count < chances:
    guess_count += 1
    user_input = int(input("Please enter your guess:"))

    if user_input == number_to_guessing:
        print(f"The number is {number_to_guessing} you found itb right! in the {guess_count} attempt")
        break
    elif guess_count >= chances and user_input != number_to_guessing:
        print(f"Oops sorry, the number is {number_to_guessing} better luck next time")

    elif user_input > number_to_guessing:
        print("Your guess very high, try again")

    elif user_input < number_to_guessing:
        print("Your guess very low, try again")        