import random
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Screen Set-Up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game with Python!")
screen.tracer(0)

#Create scoreboard
scoreboard = Scoreboard()

#Create the snake with our Snake class
snake = Snake()

#Create the food
initial_amount_of_food = random.randint(4, 6)
food_list = []
for _ in range(initial_amount_of_food):
    new_food = Food()
    food_list.append(new_food)

#Listen to input and turn the snake accordingly
screen.listen()
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Up", fun=snake.up)

#Game update the game each loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Detect collision with food
    for food in food_list:
        if food.distance(snake.snake_head) < 20:
            snake.add_segment()
            food.reset()
            scoreboard.increase_score()

    #Detect collision with wall
    if snake.snake_head.xcor() > 300 or snake.snake_head.xcor() < -300 or snake.snake_head.ycor() > 300 or snake.snake_head.ycor() < -300:
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail
    for segment in snake.segments:
        if segment != snake.snake_head:
            if segment.distance(snake.snake_head) < 5:
                scoreboard.game_over()
                game_is_on = False

screen.exitonclick()
