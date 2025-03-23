import random as r

min=int(input("enter minimum numberfor the range:"))
max =int(input("Enter maximum number for the range:"))
number_of_tries=int(input("Enter maximmum number of tries allowed"))
while min>max:
    print("keep minimum value less than max value.")
    min=int(input("enter minimum numberfor the range:"))
    max =int(input("Enter maximum number for the range:"))

    
number = r.randint(int(min),int(max))
tries =0

def guess():
    guessed=input("What is your guess?")
    guessed =int(guessed)
    return guessed

guesser =guess()
while(guesser !=number):
    if(guesser>number):
        print("Your guess is too high")
        tries+=1
        if tries>=int(number_of_tries):
            print("Max tries reached, the correct number was",number)
            break
        guesser=guess()
    else:
        print("Your guess is too low")
        tries+=1
        if tries>=int(number_of_tries):
            print("Max tries reached, the correct number was",number)
            break
        guesser=guess()
if(guesser==number):
    print("you got the answer in",tries+1,"tries")