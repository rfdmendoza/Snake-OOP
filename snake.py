from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN= 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_positions = []
        self.initialize_snake()
        self.head = self.snake_body[0]

    def get_position(self, snake_part):
        position = tuple(snake_part.pos())
        self.snake_positions.append(position)

    def generate_segment(self):
        character = Turtle(shape="square")
        character.color("white")
        character.penup()
        self.snake_body.append(character)
        return self.snake_body[len(self.snake_body)-1]

    def initialize_snake(self):
        x_pos = 0
        for index in range(3):
            character = self.generate_segment()
            character.setpos(x=x_pos, y=0)
            self.get_position(character)
            x_pos -= 20

    def increase_length(self):
        pos = self.snake_positions[len(self.snake_positions)-1]
        character = self.generate_segment()
        character.setpos(pos[0],pos[1])
        self.get_position(character)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        self.head.forward(MOVE_DISTANCE)
        self.get_position(self.snake_body[0])
        for index in range(1, len(self.snake_body)):
            self.snake_body[index].goto(self.snake_positions[0])
            self.get_position(self.snake_body[index])
            self.snake_positions.pop(0)
            if index == len(self.snake_body) - 1:
                self.snake_positions.pop(0)

    def check_if_collided(self):
        for segment in self.snake_body[1:]:
            if self.head.distance(segment) < 19:
                return True
        if  (self.head.xcor() >=285 or self.head.xcor() <= -285
               or self.head.ycor() >=285 or self.head.ycor() <= -285):
            return True
        else:
            return False
    def reset_snake(self):
        for segment in self.snake_body:
            segment.hideturtle()
        self.snake_body.clear()
        self.snake_positions.clear()
        self.initialize_snake()
        self.head = self.snake_body[0]


