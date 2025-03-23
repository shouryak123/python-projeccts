import json

# Load questions from JSON file
with open(r"C:\Users\shour\OneDrive\Desktop\python proj\end2endproj\quiz.json", "r") as file:

    quiz_data = json.load(file)

marks = 0

# Ask user to select a subject
subject = input("Select the subject (geo, phy, math): ").lower()

# Check if the subject exists in JSON data
if subject in quiz_data:
    for key, value in quiz_data[subject].items(): #.items enables us to go through the values in key and value
        print("\n" + value["question"])
        for option in value["options"]:
            print(option)

        # Get user input
        user_answer = input("Enter your answer (a, b, c): ").lower()

        # Check if answer is correct
        if user_answer == value["answer"]:
            print("Correct answer!")
            marks += 1
        else:
            print("Wrong answer! The correct answer was:", value["answer"])

else:
    print("Invalid input. Please enter geo, phy, or math.")

print("\nYour total marks:", marks)
