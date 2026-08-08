import pgzrun
import random

TITLE= "Alien Clicker"
WIDTH= 500
HEIGHT= 500


# single actor that can switch between multiple sprites
alien_images = ["bob", "rc", "bc", "gc"]
alien_index = 0
message = ""
alien = Actor(alien_images[alien_index])


def draw():
    global message
    screen.clear()
    screen.fill("black")
    alien.draw()
    screen.draw.text(message, (50,50), fontsize= 30, color= "white")
    #place_alien()

def place_alien():
    global alien_index
    alien.image = alien_images[alien_index]
    alien_index = (alien_index + 1) % len(alien_images)
    alien.x = random.randint(50,WIDTH-50)
    alien.y = random.randint(50,HEIGHT-50)


def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good shot!"
        place_alien()
    else:
        message = "Try again"


place_alien()
pgzrun.go()
