import random as r

number_rolled_dice=0
def rolling_dice():
    global number_rolled_dice  #defined it as a global variable
    answer =input("do you wanna roll the the dice? (y/n): ").lower() #.lower() converts the input to lower case
   
    if answer=="y":
        number =input("how many dice do you want to roll?")
        i=0
        for i in range(int(number)):
            print("your roll is:",r.randint(1,6))
            number_rolled_dice+=1
            
        rolling_dice()
    elif answer=="n": 
        print("you rolled",number_rolled_dice,"dices")
        print("thank you for playing the game")
    else:
        print("invalid input")
        rolling_dice() 

rolling_dice()
