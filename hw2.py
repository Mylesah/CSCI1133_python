
import turtle, platform, math

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

# cents
#==========================================
# Purpose: To compute the toal ammount of cents
#   
# Input Parameter(s):
# quarters = 25
# dimes = 10
# nickels = 5
# pennies = 1
#
# Return Value: The sum of all inputs in cents
#   
#==========================================

def cents(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters*25
    total += dimes*10
    total += nickels*5
    total += pennies
    return total

# draw_M
#==========================================
# Purpose: To draw the University of Minnesota "M"
#   
# Input Parameter(s): None, no user inputs needed to run the program
#   
# Return Value: Maroon colored "M" on yellow drawn with the turtle graphics
#   
#==========================================

def draw_M():
    turtle.delay(0)
    turtle.bgcolor("gold")
    turtle.hideturtle()
    turtle.color("maroon")
    turtle.penup()
    turtle.setpos(-200,-100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(14)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(128)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(14)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(28)
    turtle.right(60)
    turtle.forward(140)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(140)
    turtle.right(60)
    turtle.forward(28)
    turtle.left(90)
    turtle.forward(64)
    turtle.end_fill()

# Part B: star8
#==========================================
# Purpose: Draw an 8-point star in turtle graphics
#   
# Input Parameter(s): None, no user inputs needed to run the program
#   
# Return Value: An 8-point star in turtle graphics
#   
#==========================================

def star8():
    turtle.forward(300)
    turtle.left(135)
    turtle.forward(300)
    turtle.left(135)
    turtle.forward(300)
    turtle.left(135)
    turtle.forward(300)
    turtle.left(135)
    turtle.forward(300)
    turtle.left(135)
    turtle.forward(300)
    turtle.left(135)
    turtle.forward(300)
    turtle.left(135)
    turtle.forward(300)


# Part C: trajectory
#==========================================
# Purpose: To compute the horizantal speed, vertical speed, flight time, and total horizantal distance traveled
#   
# Input Parameter(s):
# height: distance from the ground in meters before the ball is thrown
# speed: intial velocity of the ball in meters per seconds when it is thrown 
# angle: the angle that the ball is thrown at
#
# Return Value: It returns the total horizantal distance traveled by the ball
#   
#==========================================

def trajectory(height, speed, angle):
    angle = angle * (math.pi/180)
    speed_x = math.cos(angle) * speed
    speed_y = math.sin(angle) * speed
    flight_time = (speed_y + math.sqrt((speed_y**2 + 19.6*height)))/9.8
    travel = round(flight_time * speed_x, 3)
    speed_x = round(speed_x, 3)
    speed_y = round(speed_y, 3)
    flight_time = round(flight_time, 3)
    print('Horizontal Speed:', speed_x, 'm/s')
    print('Vertical Speed:', speed_y, 'm/s')
    print('Flight Time:', flight_time, 's')
    return travel
