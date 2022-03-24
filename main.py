from art import logo
import random
from replit import clear

numbers = []
for n in range(1, 101):
  numbers.append(n)
  
def choose_number():
  return random.choice(numbers)

hidden_number = choose_number()

def difficulty():
  ask_dif = input("Type 'easy' or 'hard' as gamemode: ")
  if ask_dif == 'easy':
    return 10
  elif ask_dif == 'hard':
    return 5

def guess_check(guess):
  if guess == hidden_number:
    print("You won!")
    print(f"The number was: {hidden_number}")
    return 0
  elif guess > hidden_number:
    print("Too high!")
    return 1
  elif guess < hidden_number:
    print("Too low!")
    return 1

def play_game():
  lives = difficulty()

  while lives > 0 :
    
    guess = int(input("guess for a number between 1 and 100:\n"))

    if guess > 100 or guess < 0:
      print("Can't proccess number higher than 100 and lower than 0.")
    else:
      result = guess_check(guess)
      if result == 0:
        lives = 0
      elif result == 1:
        lives -= 1
      print(f"You have {lives} lives left...")


def start_game():
  print(logo)
  if input("Welcome to the Number Guessing Game! Type 'y' to play:\n") == 'y':
    clear()
    play_game()
  else:
    clear()
    start_game()
start_game()