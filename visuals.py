import turtle
dash_positions = []
# Setup turtle screen and pen
screen = turtle.Screen()
screen.setup(600,600)
#screen.title("Interactive Stickman Drawer (Terminal Input)")
t1 = turtle.Turtle()
pen = turtle.Turtle()
t2 = turtle.Turtle()
pen.speed(2)
pen.pensize(3)
pen.hideturtle()
t1.hideturtle()
t2.hideturtle()

def guessinger(bol):
  t2.clear()
  if bol == 1:
    t2.penup()
    t2.goto(140, 130)
    t2.write("Right", font=("Arial", 15, "normal"))
  else:
    t2.penup()
    t2.goto(140, 130)
    t2.write("Wrong", font=("Arial", 15, "normal"))    

def dasher(rangers):
    t1.penup()
    t1.goto(-120, 160)
    t1.write("[", font=("Arial", 15, "normal"))  
    pen.penup()
    pen.goto(-120, 160)
    pen.penup()
    x = -100
    for _ in range(rangers):
        pen.goto(x, 160)
        dash_positions.append(x)  # Store this dash position
        pen.write("_", font=("Arial", 15, "normal"))
        x += 30  # move right for next dash/letter

    pen.goto(x, 160)
    pen.write("]", font=("Arial", 15, "normal"))

def update_letter(index, letter):
    if 0 <= index < len(dash_positions):
        pen.penup()
        pen.goto(dash_positions[index], 163)
        pen.write(letter, font=("Arial", 15, "normal"))
  
def results(lives):
  t2.clear()
  if lives < 2:
     pen.penup()
     pen.goto(140, 130)
     pen.write("Loser", font=("Arial", 20, "normal"))
  else:
    pen.penup()
    pen.goto(120, 120)
    pen.write("Winner", font=("Arial", 15, "normal"))
     
def visualize(live):
    commands[str(live)]()
    
    
    
    

def draw_hanger():
    pen.penup()
    pen.goto(-80,-130)
    pen.pendown()
    pen.goto(-120,-130)
    pen.goto(-120,-160)
    pen.goto(160,-160)
    pen.goto(160,-130)
    pen.goto(-80,-130)
    
    
    pen.penup()
    pen.goto(-80,-130)
    pen.pendown()
    pen.goto(-80, 130)
    pen.pendown()
    pen.goto(20,130)
    pen.penup()
    pen.goto(0,130)
    pen.pendown()
    pen.goto(0,90)
# Drawing functions
def draw_head():
    pen.penup()
    pen.goto(0, 50)
    pen.pendown()
    pen.circle(20)

def draw_body():
    pen.penup()
    pen.goto(0, 50)
    pen.pendown()
    pen.goto(0, -30)

def draw_arm_right():
    pen.penup()
    pen.goto(0, 20)
    pen.pendown()
    pen.goto(-30, 0)

def drw_arm_left():
    pen.penup()
    pen.goto(0, 20)
    pen.pendown()
    pen.goto(30, 0)

def draw_leg_right():
    pen.penup()
    pen.goto(0, -30)
    pen.pendown()
    pen.goto(-20, -60)

def draw_leg_left():
    pen.penup()
    pen.goto(0, -30)
    pen.pendown()
    pen.goto(20, -60)

# Dictionary for easy mapping
commands = {
    '6': draw_head,
    '5': draw_body,
    '4': draw_arm_right,
    '3': drw_arm_left,
    '2': draw_leg_right,
    '1': draw_leg_left
}


draw_hanger()

#for future use 
"""
# Run loop
while True:
    part = input("Enter part to draw: ").strip().lower()
    if part == 'q':
        break
    if part in commands:
        commands[part]()
    else:
        print("Invalid input. Try h, b, a, l, or q.")

# Keep turtle window open after exit

"""