import random as r

cw = 0  # Computer wins
pw = 0  # Player wins
number_of_wins = int(input("Number of wins required to win the tournament? "))
ROCK='r' #so if we want to change what rock paper or scissors are we dont have to change it everywhere in the code but only here
PAPER ='p'
SCISSOR='s'
choices ={ROCK:'Rock',PAPER:'paper',SCISSOR:'scissors'}
options = tuple(choices.keys())


while cw < number_of_wins and pw < number_of_wins:
    cc = r.choice(options)  # Computer choice

    # Get valid user input
    pc = input("Choose one (r/p/s): ").lower()
    while pc not in options:
        print("Please input a valid choice (r, p, or s).")
        pc = input("Choose one (r/p/s): ").lower()

    print(f"Computer chose:{choices[cc]} ")
    print(f"Player chose: {choices[pc]}")

    # Determine the winner
    if pc == cc:
        print("It's a draw!")
    elif ((pc == ROCK and cc ==SCISSOR) or 
          (pc == PAPER and cc == ROCK) or 
          (pc == SCISSOR and cc == PAPER)):
        pw += 1
        print("🎉 Player wins this round!")
    else:
        cw += 1
        print("💻 Computer wins this round!")

    print(f"Total wins - Player: {pw}, Computer: {cw}\n")

# Announce the winner
if pw == number_of_wins:
    print("🏆 Player wins the tournament!")
else:
    print("🤖 Computer wins the tournament!")
