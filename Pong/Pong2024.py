#--import section
import turtle as t
import random as r

#global var of objects or game config
COURT_HEIGHT=600
COURT_WIDTH=1000
PADDLE_WIDTH=50
leftScore = 0
rightScore = 0
fontSettings = "Arial", 20

wn = t.Screen()
#made the screen a little bigger as the lines would be on the edge of the window and it looked weird
wn.setup(width=COURT_WIDTH,height=COURT_HEIGHT)

#left player 
leftPlayer = t.Turtle("square")
leftPlayer.color("blue")
leftPlayer.penup()
leftPlayer.speed(0)
leftPlayer.turtlesize(4,1)          #turtlesize will stretch the turtle
leftPlayer.setx(-COURT_WIDTH/2+10)

#right player
rightPlayer = t.Turtle("square")
rightPlayer.color("red")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.turtlesize(4,1)          #turtlesize will stretch the turtle
rightPlayer.setx(COURT_WIDTH/2-15)

ball = t.Turtle("circle")
ball.color("red")
ball.penup()
ball.speed(0)

lScore = t.Turtle(visible=False)
lScore.speed(0)
lScore.penup()
lScore.setposition(-COURT_WIDTH/4,COURT_HEIGHT/4)
lScore.write(leftScore,font=fontSettings)

rScore = t.Turtle(visible=False)
rScore.speed(0)
rScore.penup()
rScore.setposition(COURT_WIDTH/4,COURT_HEIGHT/4)
rScore.write(rightScore,font=fontSettings)


#functions
def drawCourt():
    border=t.Turtle(visible=False)
    border.speed(0)
    #top border
    border.teleport(-500,300)
    border.fd(1000)
    
    #bottom border
    border.teleport(500,-300)
    border.bk(1000)
    
    #middle lines
    border.teleport(0,-300)
    border.lt(90)
    for i in range(12):
        border.fd(26)
        border.penup()
        border.fd(26)
        border.pendown()
        
def leftPlayerUp():
    if leftPlayer.ycor()<(COURT_HEIGHT/2-PADDLE_WIDTH):
        leftPlayer.sety(leftPlayer.ycor()+20)
def leftPlayerDown():
    if leftPlayer.ycor()>(-COURT_HEIGHT/2+PADDLE_WIDTH):
        leftPlayer.sety(leftPlayer.ycor()-20)
def rightPlayerUp():
    if rightPlayer.ycor()<(COURT_HEIGHT/2-PADDLE_WIDTH):
        rightPlayer.sety(rightPlayer.ycor()+20)
def rightPlayerDown():
    if rightPlayer.ycor()>(-COURT_HEIGHT/2+PADDLE_WIDTH):
        rightPlayer.sety(rightPlayer.ycor()-20)
def collideWithPaddle(paddle,ball):
    #check did we collide with it
    if paddle.distance(ball) < 20:
        ball.setheading(180-ball.heading())         #flip the heading it was going
        #which paddle did we collide with
        if ball.xcor()>0:
            ball.setx(ball.xcor()-5)
        else:
            ball.setx(ball.xcor()+5)
        ball.fd(10)
        #the ball should react accordingly
    
    
def updateScore():
    global leftScore
    global rightScore
    if ball.xcor()<0:
        rightScore+=1
        rScore.clear()
        rScore.write(rightScore,font=fontSettings)
    elif ball.xcor()>0:
        leftScore+=1
        lScore.clear()
        lScore.write(leftScore,font=fontSettings)
        
    
        
def resetBall():
    ball.setposition(0,0)
    #randomizer for who serves first
    if r.randint(0,1)==0: #left first
        ball.setheading(r.randint(150,210))
    else:
        ball.setheading(r.randint(-30,30))
        
def moveTheBall():
    ball.fd(20)
    x,y = ball.position()
    
    #top and bottom wall bounce
    if y>(COURT_HEIGHT/2) or y<(-COURT_HEIGHT/2):
        ball.setheading(-ball.heading())
    
    #left wall or right wall should reset
    elif x<(-COURT_WIDTH/2) or x>(COURT_WIDTH/2):
        updateScore()
        resetBall()
    else:
        collideWithPaddle(leftPlayer,ball)
        collideWithPaddle(rightPlayer,ball)
    
    wn.ontimer(moveTheBall,20)
    
        
#---events
wn.onkeypress(leftPlayerUp,"w")
wn.onkeypress(leftPlayerDown,"s")
wn.onkeypress(rightPlayerUp,"Up")
wn.onkeypress(rightPlayerDown,"Down")
wn.onkeypress(resetBall,"r")
wn.listen()
    
    
drawCourt()
moveTheBall()    
wn.mainloop()