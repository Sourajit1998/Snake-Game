import turtle
import time
import random

delay=0.1
score=0
high_score=0

#Screen
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

#Snakes body
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score:0", align="center",font=("Courier",24,"normal"))

#Body parts
segments=[]

#Food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

def move_up():
    if head.direction!="down":
        head.direction="up"
def move_down():
    if head.direction != "up":
        head.direction="down"
def move_left():
    if head.direction != "right":
        head.direction="left"
def move_right():
    if head.direction != "left":
        head.direction="right"


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

def reset():
    pen.clear()
    pen.write("Score: {} High Score:{}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

wn.listen()
wn.onkeypress(move_up,"w")
wn.onkeypress(move_down,"s")
wn.onkeypress(move_left,"a")
wn.onkeypress(move_right,"d")

while True:
    wn.update()

    #border collison
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()         #reset the segments

        delay=0.1  #Reset the game speed
        score=0    #Reset the score
        reset()


    #if snake collides with the food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)                   #move the food to a random spot

        score+=10          #score increase

        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {} High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))

        #add new segment to the snake's body
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Speed increases with level up
        delay-=0.001

    for index in range(len(segments)-1,0,-1):               #last segment added to the previous segment
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments)>0:                                    #for the head segment
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    time.sleep(delay)
    move()

    #collison with itself
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

        #Hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score=0
            delay=0.1              #Reset the game speed
            reset()                #Reset the score


wn.mainloop()