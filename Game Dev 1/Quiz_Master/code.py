import pgzrun

HEIGHT= 800
WIDTH= 1000
TITLE= "Quiz Master"

marquee_box= Rect(0,0,700,80)
question_box= Rect(0,0,650,150)
timer_box= Rect(0,0,150,150)
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

score= 0
time_left= 10
question_index=0
question_count=0
marquee_message= ""
questions_file = "questions.txt"

def read_question_file():
    global question_count, questions
    q_file= open(questions_file,"r")
    for i in q_file:
        questions.append(i)
        question_count+=1
    q_file.close()

def read_next_question():
    global question_index, questions
    question_index+= 1
    return questions.pop(0).split(",")

def correct_answer():
    global score, questions,time_left
    score+ 1
    if questions:
        x= read_next_question()
        time_left= 10
    else:
        game_over()


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
    
    marquee_message= marquee_message + f" Q: {question_index} of {question_count}"

    screen.draw.textbox(marquee_message, marquee_box,color="white")
    screen.draw.textbox(str(time_left),timer_box, color="white", shadow= (0.5,0.5), scolor= "dimgray")
    screen.draw.textbox("skip",skip_box,color="white", angle=-90)

def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left= WIDTH

def update():
    move_marquee()

def on_mouse_down():
    global answer_boxes, x, skip_box
    index = 1
    for i in answer_boxes:
        if i.collidepoint(pos): 
            if index in int(x[5]):
                correct_answer()
            else:
                game_over()
        index= index+1
        if skip_box.collidepoint(pos):
            skip_question()


read_question_file()
x= read_next_question()
print(x)
pgzrun.go()
