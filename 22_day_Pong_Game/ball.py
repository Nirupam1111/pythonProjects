from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed("fastest")
        self.goto(0,0)
        self.move_x=15
        self.move_y=15
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *=-1

    def bounce_x(self):
        self.move_x *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
