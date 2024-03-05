from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)

    # How the move function works
    '''
    This for loop works by using the range function to go backwards. using a start of len(segments) -1
    (We have to use len(segments) - 1 since it gives us one higher than the correct index), stop of 0, and step of -1

    Also something to note is that when using the range function. Since range excludes the stop, since we go to zero,
    it will never include our furthest most block at the front.

    This in turn allows for us to go through each segment backwards to get a more seamless movement for the snake
    as well as prepare for any future turns the snake will make.

    Using segments[seg_num - 1] we are able to grab the snake 'block' before it and grab the positions.
    Then we can hand them to the current furthest block and move it forward.
    '''

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
