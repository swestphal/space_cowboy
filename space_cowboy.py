

# Import the module
import simplegui

# Define global variables (program state)
positionX = 150
positionY = 100
speed = 10
vehicle_width=20
vehicle_height=20
screen_width=400
screen_height=200

# Define "helper" functions


# Define event handler functions
def right():
    global positionX
    positionX = (positionX+speed)%screen_width

def left():
    global positionX
    positionX = (positionX-speed)%screen_width
    

def forward():
    global positionY
    global speed
    positionY = (positionY-speed)%screen_height
    
 
    
def back():
    global positionY
    global speed
    positionY = (positionY+speed)%screen_height


def draw(canvas):
     canvas.draw_polygon([(positionX, positionY), (positionX+vehicle_width, positionY), (positionX+(vehicle_width/2), positionY-vehicle_height)], 12, 'Green')


def key_handler(key):
    if key == 38:
        forward()
    if key == 40:
        back()
    if key == 39:
        right()
    if key == 37:
        left()
    

# Create a frame

frame = simplegui.create_frame('space cowboy', screen_width, screen_height)

# Register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)


# Start frame and timers
frame.start()