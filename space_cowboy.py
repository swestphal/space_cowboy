# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
positionX = 150
positionY = 100
speed = 0
vehicle_width=20
vehicle_height=20
screen_width=400
screen_height=200
max_speed=10
speed_up=1
slow_down=0
stop=0
# Define "helper" functions


# Define event handler functions
def right():
    global positionX
    positionX = (positionX+speed)%screen_width

def left():
    global positionX
    positionX = (positionX-speed)%screen_width
    

def accelerate():
    global positionY
    global speed
    global speed_up
    global slow_down
    positionY = (positionY-speed)%screen_height
    if speed<=max_speed:
        speed+=.4  
    speed_up=1
    print "acc"
    slow_down=0
 
    
def decelerate():
    global positionY
    global speed
    global speed_up
    global slow_down
    speed-=1

    if speed <=0: 
        speed=0
        slow_down=0

def move_forward():
    global positionY
    if (slow_down==1 ):
        print "back", speed
        decelerate()
    if (speed_up==1):
        accelerate()
        print "forward", speed


def draw(canvas):
    canvas.draw_polygon([(positionX, positionY), (positionX+vehicle_width, positionY), (positionX+(vehicle_width/2), positionY-vehicle_height)], 12, 'Green')


def key_handler(key):
    global stop
   
    if key == 38:
        accelerate()
    if key == 40:
        decelerate()
    if key == 39:
        right()
    if key == 37:
        left()
    if key == 88:
        stop=1
    move_forward
        
#Create a frame

frame = simplegui.create_frame('space cowboy', screen_width, screen_height)

# Register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)
move = simplegui.create_timer(100,move_forward)

# Start frame and timers
frame.start()
move.start()