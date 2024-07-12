from turtle import Turtle

# Constants and Initialization
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Create a Snake Body


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    """
    len(segments) represents the index of the last segment in the segments list.
    0: This is the stopping point of the range (exclusive). The loop will continue 
    until it reaches but does not include this value.
    -1: This is the step. It indicates that the loop should move 
    backwards through the range.
    
    This loop iterates over the indices of the segments list in reverse order, 
    starting from the second-to-last segment and moving to the first segment.
    """
    def movement(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start, stop, step
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # stop to go up then back which violate the game rules
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
