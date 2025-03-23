# Question banks
geography = {
    "q1": 'a', "q2": 'b', "q3": 'b'
}

physics = {
    "q1": 'c', "q2": 'a', "q3": 'b'
}

math = {
    "q1": 'b', "q2": 'c', "q3": 'a'
}

marks = 0

subject = input("Select the subject (geo, phy, math): ").lower()

if subject == "geo":
    a1 = input("What is the capital of India?\n"
               "a) New Delhi\n"
               "b) Mumbai\n"
               "c) Kolkata\n")
    if a1 == geography["q1"]:
        print("Correct answer!")
        marks += 1
    else:
        print("Wrong Answer!")

    a2 = input("What is the capital of the USA?\n"
               "a) Texas\n"
               "b) Washington DC\n"
               "c) Alaska\n")
    if a2 == geography["q2"]:
        print("Correct answer!")
        marks += 1
    else:
        print("Wrong Answer!")

    a3 = input("What is the capital of France?\n"
               "a) Lyon\n"
               "b) Paris\n"
               "c) Bordeaux\n")
    if a3 == geography["q3"]:
        print("Correct answer!")
        marks += 1
    else:
        print("Wrong Answer!")

elif subject == "phy":
    a1 = input("What is the SI unit of force?\n"
               "a) Joule\n"
               "b) Watt\n"
               "c) Newton\n")
    if a1 == physics["q1"]:
        print("Correct answer!")
        marks += 1
    else:
        print("Wrong Answer!")

    a2 = input("Which of the following is a scalar quantity?\n"
               "a) Speed\n"
               "b) Force\n"
               "c) Momentum\n")
    if a2 == physics["q2"]:
        print("Correct answer!")
        marks += 1
    else:
        print("Wrong Answer!")

    a3 = input("Which law states that 'Every action has an equal and opposite reaction'?\n"
               "a) Newton's First Law\n"
               "b) Newton's Third Law\n"
               "c) Newton's Second Law\n")
    if a3 == physics["q3"]:
        print("Correct answer!")
        marks += 1
    else:
        print("Wrong Answer!")

elif subject == "math":
    a1 = input("What is the value of (2+3) * 4?\n"
               "a) 10\n"
               "b) 20\n"
               "c) 25\n")
    if a1 == math["q1"]:
        print("Correct answer!")
        marks += 1
    else:
        print("Wrong Answer!")

    a2 = input("What is the square root of 81?\n"
               "a) 6\n"
               "b) 8\n"
               "c) 9\n")
    if a2 == math["q2"]:
        print("Correct answer!")
        marks += 1
    else:
        print("Wrong Answer!")

    a3 = input("What is 10 divided by 2?\n"
               "a) 5\n"
               "b) 4\n"
               "c) 6\n")
    if a3 == math["q3"]:
        print("Correct answer!")
        marks += 1
    else:
        print("Wrong Answer!")

else:
    print("Invalid input. Please enter geo, phy, or math.")

print("Your total marks:", marks)
