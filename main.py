#jordan overton
#10/27/2022
#purpose: to make a program with a method variable color change and if statements 

from random import choice

ROCK = 1
PAPER = 2
SCISSORS=3
red = "\u001b[31m"
print("lets play rock paper scissors!")

cpu = choice((ROCK, PAPER, SCISSORS))
player_one = input('-> ROCK, PAPER, or SCISSORS?')
#i made this all upper case to make the code run easier also im gonna loop it to make so you have an option to either play again or leave 

if (player_one).upper()== 'ROCK':
  player_one=1
elif (player_one).upper()== 'PAPER':
  player_one=2
elif (player_one).upper()== 'SCISSORS':
  player_one=3
else:
  print('What the heck did you pick!? Pick a valid option!')
  
if(cpu==ROCK)and(player_one==ROCK):
  print(red + 'You Tied')
elif(cpu==ROCK)and(player_one==PAPER):
  print(red +'gosh darnet i lost ')
elif(cpu==ROCK)and(player_one==SCISSORS):
  print(red +'You Lose better kuck next time ')
elif(cpu==PAPER)and(player_one==ROCK):
  print(red +'almost got me ')
elif(cpu==PAPER)and(player_one==PAPER):
  print(red +'You Tied')
elif(cpu==PAPER)and(player_one==SCISSORS):
  print(red +'winner winner chicken dinner')
elif(cpu==SCISSORS)and(player_one==ROCK):
  print(red +' ahh shucks you win')
elif(cpu==SCISSORS)and(player_one==PAPER):
  print(red +'finally i win and you loose')
elif(cpu==SCISSORS)and(player_one==SCISSORS):
  print(red +'You Tied')

print("thank you for playing have a good day!!")

#also i did have a couple problems with the strings i messed up my strings and had to go back and fix them 
# ran into a problem with turning the text a diffrent collor because i forgot to define the color as a variable 
  
