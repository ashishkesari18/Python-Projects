#rockpaper scissors
import random
rock = "✊"
paper = "🖐"
scissors = "✌️"
game_images = [rock,paper,scissors]
user_input = int(input("please enter your choice either 0 for rock and 1 for paper and 2 for Scissors\n"))
if user_input >=3 and user_input<0:
  print("You have entered an invalid option and you lose...!")
else:
  print("You chose:")
  print(game_images[user_input])
computer_input = random.randint(0,2)
print("computer choose:")
print(game_images[computer_input])
if user_input ==0 and computer_input == 2:
    print("You win")
elif computer_input ==0 and user_input == 2:
    print("you lose")
elif computer_input > user_input :
    print("You lose")
elif user_input > computer_input:
    print("you win")
elif user_input == computer_input:
    print("It's draw")
