import pgzrun
import random

TITLE= "Alien Shooter"
WIDTH= 500
HEIGHT= 500

message= ""

alien= Actor("bob")

def draw():
    global message
    screen.clear()
    screen.fill("yellow")
    alien.draw()
    screen.draw.text(message, (50,50), fontsize= 30, color= "black")
    #place_alien()

def place_alien():
    alien.x = random.randint(50,WIDTH-50)
    alien.y= random.randint(50,HEIGHT-50)

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        message= "Good shot!"
        place_alien()
    else:
        message= "Try again"
    

place_alien()
pgzrun.go()