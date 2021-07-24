#DICE Simulation
from random import randint
def Dice():
    dice = randint(1,6)
    print(dice)

if __name__ == '__main__':
    game_on = False
    print("Are you ready to roll the dices ?")
    inp = 'NO'
    while inp not in ['yes','no']:
        inp = input('Type "yes" or "no": ')
    if inp == 'yes':
        game_on = True
    else:
        game_on = False
        exit()
    while game_on:
        Dice()
        print("\n")
        print("Would you like to roll again ?")
        ini = "X"
        while ini not in ['yes','no']:
            ini = input('Type "yes" or "no": ')
        if ini == 'yes':
            print("\n"*100)
            continue
        else:
            print("Thank you")
            break
         