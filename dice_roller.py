import random

def main():
    dice_rolls = 2
    dice_sum = 0
    for i in range(0,dice_rolls):
        roll = random.randint(1,6)
        #or, dice_sum += roll
        dice_sum = dice_sum + roll
        print(f'you rolled a {roll}')
    print(f'You rolled a total of {dice_sum}')

if __name__== "__main__":
  main()