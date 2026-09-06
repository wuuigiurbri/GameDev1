import pgzrun
import random
import time

WIDTH= 693
HEIGHT= 409

number_of_satelites= 8
next_satelite= 0
start_time= 0
end_time= 0
total_time= 0
satelites= []
lines= []

def create_satelite():
    global start_time
    for i in range(number_of_satelites):
        sat= Actor("satekite")
        sat.pos = random.randint (40,WIDTH-40), random.randint(40,HEIGHT-40)
        satelites.append(sat)
    start_time= time.time()


 



def draw():
    screen.blit("background",(0,0))
    number= 1
    for i in satelites:
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+20))
        i.draw()
        number += 1
    for i in lines:
        screen.draw.line(i[0],i[1], ("red"))  

def update():
    pass

def on_mouse_down(pos):
    global lines
    global next_satelite
    if next_satelite > number_of_satelites:
        if satelites[next_satelite].collidepoint(pos):
            if next_satelite:
                lines.append((satelites[next_satelite-1].pos, satelites[next_satelite].pos))
            next_satelite += 1
        else:
            lines= []
            next_satelite = 0


create_satelite()
pgzrun.go()