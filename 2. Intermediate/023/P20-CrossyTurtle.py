import time
import turtle
import player
import car_manager
import score

# Screen settings
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create everything else
player = player.Player()
car_manager = car_manager.CarManager()
score = score.Score()

# Player movment
screen.listen()
screen.onkey(player.go_up, "Up")

game = True
while game:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game = False
            score.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()
