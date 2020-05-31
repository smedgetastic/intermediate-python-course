import random

def main():
    #previous variable: dice_rolls = 2
    dice_rolls = int(input('How many dice would you like to roll?'))
    dice_size = int(input('How many sides are the dice?'))
    dice_sum = 0
    for i in range(0,dice_rolls):
        roll = random.randint(1,6)
        #or, dice_sum += roll
        dice_sum = dice_sum + roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == 6:
            print(f'You rolled a {roll}! Critical Success!')
        else:
            print(f'you rolled a {roll}')
    print(f'You rolled a total of {dice_sum}')

if __name__== "__main__":
  main()