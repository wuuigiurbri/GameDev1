import pgzrun
import random

WIDTH= 500
HEIGHT= 350
score= 0
game_over= False

ss = Actor("spaceship")
ss.pos = (230, 220)

star_images = ["gold_star", "green_star"]
star = Actor(star_images[0])


def place_stars():
    star.image = random.choice(star_images)
    star.x = random.randint(50, WIDTH - 50)
    star.y = random.randint(50, HEIGHT - 50)

star.pos= (130,320)

def draw():
    screen.clear()
    screen.blit("background", (0,0))
    ss.draw()
    star.draw()
    screen.draw.text("SCORE= {}".format(score),(0,0),color="red")
    if game_over:
        screen.fill("black")
        screen.draw.text("Times Up! Your final score: {}".format(score),(200,150),color="blue")
        
def time_up():
    global game_over
    game_over= True

def update():
    global score
    if keyboard.left:
        ss.x -= 2
    if keyboard.right:
        ss.x +=2
    if keyboard.up:
        ss.y -=2
    if keyboard.down:
        ss.y += 2

    coll= ss.colliderect(star)

    if coll:
        score+=10
        place_stars()


clock.schedule(time_up,60.0)
    


pgzrun.go()