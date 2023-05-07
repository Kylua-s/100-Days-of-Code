# Project 15 - Quiz
from question_model import Question
from data import question_data

# To store the Question objects
question_bank = []
for question in question_data:
    # Extract the text and answer values from the dictionary
    q_text = question['text']
    q_answer = question['answer']
    # Create a new Question object
    question = Question(q_text, q_answer)
    # Add the new Question object to the question_bank list
    question_bank.append(question)

# User score
correct_answers = 0
for question in question_bank:
    # Prompt the user to answer the current question with a True or False input
    answer = input(f"Q.{question.q_number}: {question.text} (True/False): ")
    # If the user's answer matches the correct answer, increment correct_answers
    if answer == question.answer:
        correct_answers += 1
        print("You got it right!")
    else:
        print("That's wrong.")
    # Show the user's current score out of the total number of questions
    print(f"The correct answer was: {question.answer}.")
    print(f"Your current score is: {correct_answers}/{question.q_number}")
    print()

# Once all questions have been answered, show the final score and end the program
print("You completed the quiz!")
print(f"Your final score is: {correct_answers}/{len(question_bank)}")
