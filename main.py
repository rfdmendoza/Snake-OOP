from snake  import Snake
from food import Food
from turtle import Screen
from score import Score
import time

is_game_going = True
canvas = Screen()
canvas.setup(width=600,height=600)
canvas.bgcolor("black")
canvas.title("Snake Game")
canvas.tracer(0)

snake = Snake()
food = Food()
score = Score()

canvas.listen()
canvas.onkey(fun = snake.up,key= "Up")
canvas.onkey(fun= snake.down,key= "Down")
canvas.onkey(fun = snake.left,key= "Left")
canvas.onkey(fun = snake.right,key= "Right")


def game():
    global is_game_going
    while is_game_going :
        canvas.update()
        time.sleep(0.1)
        snake.move()
        if snake.check_if_collided():
            snake.reset_snake()
            score.reset_score()
        if snake.head.distance(food) < 15:
            while food.spawn_food() in snake.snake_positions:
               food.spawn_food()
            snake.increase_length()
            score.add_score()
game()

canvas.exitonclick()