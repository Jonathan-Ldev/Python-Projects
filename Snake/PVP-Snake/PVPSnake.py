#---import section
import turtle as t

import random as r
import time

#---global var of objects or game config
delay=0.05
bodyParts=[]        #bodyParts is plural so list
bodyParts2=[]
colors=["green","blue","yellow","dark violet","deep pink","orange","red","black","midnight blue","cyan","aquamarine","silver","spring green","dark red","slate blue","deep sky blue","chartreuse","cadet blue"]
colorN = r.randint(0,17)
colorN2=r.randint(0,17)

wn=t.Screen()
wn.setup(width=600,height=600)      #each time the game turns on, sets the w,h
wn.bgcolor("gray")

head = t.Turtle(shape="square")
head.color(colors[colorN])
head.speed(0)
head.penup()
head.teleport(-200,0)
head.direction="right"

#basically copied all snake 1 code to make snake 2
head2 = t.Turtle(shape="square")
head2.color(colors[colorN2])
head2.speed(0)
head2.penup()
head2.teleport(200,0)
head2.direction="right"

bodyPart = t.Turtle()
bodyPart.teleport(1000,1000)

bodyPart2 = t.Turtle()
bodyPart2.teleport(1000,1000)

food = t.Turtle(shape="circle")
food.speed(0)
food.penup()
food.teleport(100,100)
food.color("red")

#---functions
#move up
def up():
    if head.direction != "down":
        head.direction="up"
#move down
def right():
    if head.direction != "left":
        head.direction="right"
#move left
def left():
    if head.direction != "right":
        head.direction="left"
#move right
def down():
    if head.direction != "up":
        head.direction="down"
        
def up2():
    if head2.direction != "down":
        head2.direction="up"
#move down
def right2():
    if head2.direction != "left":
        head2.direction="right"
#move left
def left2():
    if head2.direction != "right":
        head2.direction="left"
#move right
def down2():
    if head2.direction != "up":
        head2.direction="down"
    
def move():
    if head.direction =="up":
            head.sety(head.ycor()+20)
    elif head.direction =="right":
            head.setx(head.xcor()+20)
    elif head.direction =="left":
            head.setx(head.xcor()-20)
    elif head.direction =="down":
            head.sety(head.ycor()-20)
def move2():
    if head2.direction =="up":
            head2.sety(head2.ycor()+20)
    elif head2.direction =="right":
            head2.setx(head2.xcor()+20)
    elif head2.direction =="left":
            head2.setx(head2.xcor()-20)
    elif head2.direction =="down":
            head2.sety(head2.ycor()-20)            
def hideTheBodyParts():
    global bodyParts
    head.teleport(0,0)
    for eachBodyPart in bodyParts:
        eachBodyPart.goto(1000,1000)
        bodyParts=[]
def hideTheBodyParts2():
    global bodyParts2
    head2.teleport(0,0)
    for eachBodyPart in bodyParts2:
        eachBodyPart.goto(1000,1000)
        bodyParts2=[]


#---events
#window.onkeypress(command,"keyboard character")
wn.onkeypress(up,"w")       #keyboard bindings from the window object
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")
wn.onkeypress(down,"s")
wn.onkeypress(up2,"i")       #keyboard bindings from the window object
wn.onkeypress(right2,"l")
wn.onkeypress(left2,"j")
wn.onkeypress(down2,"k")
wn.listen()


#---main loop
while True:         #runs the code over and over
    wn.update()     #update or refresh the screen
    #TODO: Check for wall collision
            #top               #right               #left                 #bottom
    if head.ycor()>290 or head.xcor()>290 or head.xcor()<-290 or head.ycor()<-290:
        hideTheBodyParts()
        
    if head2.ycor()>290 or head2.xcor()>290 or head2.xcor()<-290 or head2.ycor()<-290:
        hideTheBodyParts2()
    
    if head.distance(bodyPart2)<10:
        hideTheBodyParts()
    
    if head2.distance(bodyPart)<10:
        hideTheBodyParts2()
        
    if head2.distance(head)<10:
        check = r.randint(1,2)
        if check ==1:
            hideTheBodyParts
        else:
            hideTheBodyParts2
        
    #if head.xcor()>290:
        #head.teleport(-290,0)
        
    #TODO: Check for food collision
    #distance btwn head and food
    if head.distance(food) < 20:
        food.teleport(r.randint(-290,290),r.randint(-290,290))
        bodyPart = t.Turtle(shape="square")
        bodyPart.color(colors[colorN])
        bodyPart.speed(0)
        bodyPart.penup()
        bodyParts.append(bodyPart)
    if head2.distance(food) < 20:
        food.teleport(r.randint(-290,290),r.randint(-290,290))
        bodyPart2 = t.Turtle(shape="square")
        bodyPart2.color(colors[colorN2])
        bodyPart2.speed(0)
        bodyPart2.penup()
        bodyParts2.append(bodyPart2)
   
    
    #TODO: Move the body parts
    #Move the tail to the head
    for i in range(len(bodyParts)-1,0,-1):
        newX=bodyParts[i-1].xcor()
        newY=bodyParts[i-1].ycor()
        bodyParts[i].goto(newX,newY)
    for i in range(len(bodyParts2)-1,0,-1):
        newX=bodyParts2[i-1].xcor()
        newY=bodyParts2[i-1].ycor()
        bodyParts2[i].goto(newX,newY)
        
    #Move the neck to the head
    if len(bodyParts)>0:
        newX=head.xcor()
        newY=head.ycor()
        bodyParts[0].goto(newX,newY)
    if len(bodyParts2)>0:
        newX=head2.xcor()
        newY=head2.ycor()
        bodyParts2[0].goto(newX,newY)
        
    #TODO: Move the head forward
    move()
    move2()
    
    #TODO: Check for body collision
    #if the head is within some value of another bodyPart
    for eachBodyPart in bodyParts:
        if head.distance(eachBodyPart)<10:
            hideTheBodyParts()
    for eachBodyPart in bodyParts:
        if head2.distance(eachBodyPart)<10:
            hideTheBodyParts2()
    
    
    
    time.sleep(delay)       #time module tells the program to sleep by some delay value