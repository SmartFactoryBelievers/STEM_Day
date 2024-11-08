import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Robot Race!")
screen.setup(width=600, height=400)

colors = ["red", "blue", "green", "yellow", "purple"]
shapes = ["turtle", "circle", "triangle", "square", "classic"]
speeds = [1, 3, 5, 7, 10]
robots = []

# Set starting positions for each robot
start_y = -100

for i in range(len(colors)):
    robot = turtle.Turtle(shape=shapes[i])  # Change shape for each robot
    robot.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Make the "robot" look bigger
    robot.color(colors[i])
    robot.penup()
    robot.goto(x=-250, y=start_y)
    robot.speed(speeds[i])  # Set speed for each robot

    # Draw "antenna" to make it look like a robot
    robot.pendown()
    robot.setheading(90)  # Point up
    robot.forward(10)  # "Antenna"
    robot.penup()
    robot.setheading(0)  # Point right again

    robots.append(robot)
    start_y += 50  # Space each robot out

# Race logic
race_in_progress = True

while race_in_progress:
    for robot in robots:
        # Move each robot a random distance forward
        robot.forward(random.randint(1, 10))

        # Check if a robot has reached the finish line
        if robot.xcor() >= 250:
            race_in_progress = False
            winning_color = robot.pencolor()
            print(f"The {winning_color} robot wins!")
            break

# Keep the window open until closed by the user
turtle.done()
