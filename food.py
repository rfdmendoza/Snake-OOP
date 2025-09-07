from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.spawn_food()

    def spawn_food(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        pos = (pos_x,pos_y)
        self.teleport(pos_x, pos_y)
        return pos