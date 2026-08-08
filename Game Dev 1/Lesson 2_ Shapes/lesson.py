import pgzrun

HEIGHT= 800
WIDTH= 800

def draw():
    screen.clear()
    screen.draw.text("My name is Teniola", (100,100), color= 'yellow')
    screen.draw.circle((250,150), 25, (255,0,0))
    screen.draw.filled_circle((200,200), 50, (255,0,0))
    rect= Rect((300,100), (50,20))
    screen.draw.rect(rect, (0,255,0))
    screen.draw.filled_rect(Rect((400,100), (50,20)), (0,255,0))
    screen.draw.rect(Rect((500,100), (50,50)), (0,0,255))
    screen.draw.filled_rect(Rect((600,100), (50,50)), (0,0,255))
    screen.draw.line((100,300), (200,400), (255,0,0))

pgzrun.go()