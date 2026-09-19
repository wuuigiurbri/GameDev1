import pgzrun

HEIGHT= 800
WIDTH= 1000
TITLE= "Quiz Master"

marquee_box= Rect(0,0,700,80)
question_box= Rect(0,0,650,150)
timer_box= Rect(0,0,100,100)
answer_box1= Rect(0,0,300,150)
answer_box2= Rect(0,0,300,150)
answer_box3= Rect(0,0,300,150)
answer_box4= Rect(0,0,300,150)
skip_box= Rect(0,0,200,380)

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box, "blue")

pgzrun.go()