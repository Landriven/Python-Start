import random

def get_choices():
  player_choice = input("enter a choice (rock, paper, scissors):")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "You both suck"
  elif player == "rock":
    if computer == "scissors":
      return "Rock violates scissors! You win"
    else: 
      return "paper smothers rock to death! You lose."
  elif player == "paper":
    if computer == "rock":
      return "paper smothers rock to death! You win"
    else: 
      return "Rock violates scissors! You lose."
  elif player == "scissors":
    if computer == "paper":
      return "scissors shreds paper! You win"
    else: 
      return "Rock violates scissors! You lose."

choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)