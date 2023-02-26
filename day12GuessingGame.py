# from random import randint
#
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")
#
# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS
#
# def game():
#
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#
#
#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")
#
#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))
#
#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")
#
#
# game()
import random

number = random.randint(1, 100)

print("Welcome to the number guessing")
print("I'm thinking of a number between 1 and 100 ")
level = input("choose a difficulty .Type 'easy' or 'hard' : ")
if level == "easy":
  attempts = 10
elif level == "hard":
  attempts = 5

print(f"You have {attempts} remaining to guess the number ")
t = True
while t:
  guess = int(input("Make a guess : "))


  def guess_fun(a, b):
    if a == b:
      return 0
    elif a < b:
      return 1
    elif a > b:
      return 2


  result = guess_fun(guess, number)
  if result == 1 or result == 2:
    attempts = attempts - 1


  def result_fun(result):
    if attempts == 0:
      print("You run out of attempts. You lose !")

    elif result == 0:
      print(f"You have guess it right !. The number was {number}")


    elif result == 1:
      print("Too low")
      print("Guess again ")
      print(f"You have {attempts} remaining to guess the number ")

    elif result == 2:
      print("Too high")
      print("Guess again ")
      print(f"You have {attempts} remaining to guess the number ")


  result_fun(result)
  if result == 0 or attempts == 0:
    t = False

