import pgzrun
import random
import time

WIDTH= 1024
HEIGHT= 600

next_planet= 0
start_time= 0
end_time= 0
total_time= 0
planets= []
lines= []
images= ["earth.png", "jupiter.png", "mars.png", "moon.png", "moon.png", "mars.png", "jupiter.png","earth.png" ]
number_of_planets= len(images)

def create_planet():
    global start_time
    for i in range(number_of_planets):
        sat= Actor(images[0])
        sat.pos = random.randint (40,WIDTH-40), random.randint(40,HEIGHT-40)
        images.remove(images[0])
        planets.append(sat)
    start_time= time.time()


 



def draw():
    global total_time
    screen.blit("background",(0,0))
    number= 1
    for i in planets:
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+20))
        i.draw()
        number += 1
    for i in lines:
        screen.draw.line(i[0],i[1], ("red"))  
    if next_planet < number_of_planets:
        total_time= time.time() - start_time
        screen.draw.text(str(round(total_time,1)),(10,10), fontsize= 30,)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10), fontsize= 30,)

def update():
    pass

def on_mouse_down(pos):
    global lines
    global next_planet
    if next_planet < number_of_planets:
        if planets[next_planet].collidepoint(pos):
            if next_planet:
                lines.append((planets[next_planet-1].pos, planets[next_planet].pos))
            next_planet += 1
        else:
            lines= []
            next_planet = 0



create_planet()
pgzrun.go()