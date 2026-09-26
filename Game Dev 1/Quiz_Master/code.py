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

answer_boxes= [answer_box1, answer_box2, answer_box3, answer_box4]
questions= []

time_left= 10
question_index=0
question_count=0
marquee_message= ""

def draw():
    global marquee_message
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.filled_rect(timer_box, "navyblue")
    screen.draw.filled_rect(skip_box, "green")

    for i in answer_boxes:
        screen.draw.filled_rect(i, "darkorange")
        

    marquee_message= "Welcome to the Quiz Master"
    
    marquee_message= marquee_message + f"Q: {question_index} of {question_count}"

    screen.draw.textbox(marquee_message, marquee_box,color="white")
    screen.draw.textbox(str(time_left),timer_box, color="white", shadow= (0.5,0.5), scolor= "dimgray")
    screen.draw.textbox("skip",skip_box,color="white", angle=-90)


    


def update():
    pass

pgzrun.go()
