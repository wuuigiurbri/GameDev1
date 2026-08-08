import pgzrun
import random

WIDTH= 600
HEIGHT= 500
score= 0
game_over= False

bee= Actor("bee")
bee.pos= 130,220

flower= Actor("flower")
flower.pos= 230,320

def draw():
    screen.clear()
    screen.blit("background", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("SCORE= {}".format(score),(0,0),color="black")
    if game_over:
        screen.fill("pink")
        screen.draw.text("Times Up! Your final score: {}".format(score),(300,250),color="red")
        
def time_up():
    global game_over
    game_over= True


def place_flower(): 
    flower.x= random.randint(50,WIDTH-50)
    flower.y= random.randint(50,HEIGHT-50)

def update():
    global score
    if keyboard.left:
        bee.x -= 2
    if keyboard.right:
        bee.x +=2
    if keyboard.up:
        bee.y -=2
    if keyboard.down:
        bee.y += 2

    coll= bee.colliderect(flower)

    if coll:
        score+=10
        place_flower()


clock.schedule(time_up,60.0)
    


pgzrun.go()