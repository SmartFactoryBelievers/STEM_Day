
import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Robot Race!")
screen.setup(width=600, height=400)

colors = ["red", "blue", "green", "yellow", "purple"]
robots = []
multiplier = [0.1, 0.1, 0.1, 0.1, 0.7]

# Set starting positions for each robot
start_y = -100

for color in colors:
    robot = turtle.Turtle(shape="square")  # Use square shape for a more "robotic" look
    robot.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Make the "robot" look bigger
    robot.color(color)
    robot.penup()
    robot.goto(x=-250, y=start_y)
    
    ## Draw "antenna" to make it look like a robot
    #robot.pendown()
    #robot.setheading(90)  # Point up
    #robot.forward(10)  # "Antenna"
    #robot.penup()
    #robot.setheading(0)  # Point right again

    robots.append(robot)
    start_y += 50  # Space each robot out

# Race logic
race_in_progress = True

while race_in_progress:
    for i in range(0,5):
        # Move each robot a random distance forward
        robots[i].forward(random.randint(1, 10)*multiplier[i])
        
        # Check if a robot has reached the finish line
        if robots[i].xcor() >= 250:
            race_in_progress = False
            winning_color = robots[i].pencolor()
            print(f"The {winning_color} robot wins!")
            break

# Keep the window open until closed by the user
turtle.done()



