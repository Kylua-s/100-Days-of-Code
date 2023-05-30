# Project 22 - U.S. States Game
# U.S. states guessing game

import turtle
import pandas


# Screen settings
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Turtle to write the states
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# Reads the data
data = pandas.read_csv("50_states.csv")
state_list = data['state'].to_list()


correct_guesses = []
while len(correct_guesses) <= 50:
    guess = screen.textinput(f"{len(correct_guesses)}/50 States Correct", "What's another state's name?")
    guess = guess.title()

    if guess in state_list:
        # Write the state on the map
        correct_guesses.append(guess)
        x_cor = int(data[data.state == guess].x)
        y_cor = int(data[data.state == guess].y)
        pen.goto(x_cor, y_cor)
        pen.write(guess)

    elif guess == 'Exit':
        # Creates a csv file with all the states that were not guessed
        missed_states = []
        for state in state_list:
            if state not in correct_guesses:
                missed_states.append(state)
        learing_data = pandas.DataFrame(missed_states)
        learing_data.to_csv("Missed_States.csv")
        break

# End screen message
pen.goto(0, 0)
if len(correct_guesses) <= 50:
    pen.write(f"A csv file was created with all \nthe {50-len(correct_guesses)} states that were not guessed.",
              align="center",
              font=("Courier", 24, "normal"))
else:
    pen.write("You GOAT", align="center", font=("Courier", 24, "normal"))


screen.exitonclick()
