from turtle import Turtle

UP = 90
DOWN = 270
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()

        self.color('white')
        self.shape('square')
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def play(self):
        midline = Turtle()
        midline.hideturtle()
        midline.speed('fastest')
        midline.color('white')
        midline.penup()
        midline.goto(0, 300)
        midline.setheading(270)
        for _ in range(30):

            midline.forward(10)
            midline.penup()
            midline.forward(10)
            midline.pendown()

    def goup(self):
        new_y= self.ycor() + 20
        self.goto(self.xcor(),new_y)
    def godown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
