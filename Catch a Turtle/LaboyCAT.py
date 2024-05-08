#---import statements---
import turtle as t
import random as r
import Leaderboard as lb

#---global variables and objects---
#---game configuration--
wn=t.Screen()
wn.addshape("assets/gold.gif")
wn.addshape("assets/silver.gif")
wn.addshape("assets/bronze.gif")
wn.addshape("assets/turtle.gif")
wn.bgpic("assets/turtle.gif")
score=0
click = 0
miss = 0
overall = 0
size = 4
start = "false"
#    tuple("font style",fontSize,"font type - bold, italic, normal")
fontSetup=("Times New Roman",30,"normal")
timer = 10
interval = 1000
FILENAME="db.txt"
leaderboard=[]

trent = t.Turtle()
trent.penup()
trent.shape("turtle")
trent.shapesize(2)
trent.fillcolor("purple")
trent.speed(0)
trent.shapesize(4)

scoreKeeper = t.Turtle()
scoreKeeper.penup()
scoreKeeper.teleport(100,200)
scoreKeeper.pendown()
scoreKeeper.speed(0)
scoreKeeper.hideturtle()   #still writes, but can't see the turtle

timeKeeper = t.Turtle()
timeKeeper.penup()
timeKeeper.teleport(-100,200)
timeKeeper.pendown()
timeKeeper.speed(0)
timeKeeper.hideturtle()   #still writes, but can't see the turtle

medal = t.Turtle()
medal.speed(0)
medal.hideturtle()
medal.teleport(200,0)

#---functions---
def trentClicked(x,y):
     global click
     global size
     print("trent was clicked")
     click += 1
     # print(x,y)
     trent.color("red")
     trent.stamp()
     trent.color("purple")
     if size > 1:
          size = size/2
          trent.shapesize(size)
          
     else:
          trent.shapesize(4)
          size = 4
     moveTrent()
     updateScore()
     if wn.bgcolor() == "white":
          wn.bgcolor("red")
     else:
          wn.bgcolor("white")
     

def moveTrent():
     # width,height=t.screensize()
     # print(width,height)
     # make sure it isn't within a distance of 10 of the timekeepr and score keeper
     newX=r.randint(-300,300)
     newY=r.randint(-300,300)
     if trent.distance(scoreKeeper)  <=50:
          newX=r.randint(-300,300)
          newY=r.randint(-300,300)
     if trent.distance(timeKeeper)  <=50:
          newX=r.randint(-300,300)
          newY=r.randint(-300,300)
     trent.goto(newX,newY)

def updateScore():
     global score
     score+=1
     #write the score to the screen
     scoreKeeper.clear()
     scoreKeeper.write(f"Score: {score}",font=fontSetup)  #drawing the score


def screenClicked(x,y):
     #if the game hasn't ended, then update misses
     global miss  
     global timer 
     if timer <= 0:
          pass
     else:
          miss+=1
     
     # wn.bgcolor("red")  #this runs anytime the screen or turt is clicked
     
#game over function.............
def manageLeaderboard():
     global score
     global miss
     global click
     global overall
     namesList=lb.getNames("db.txt")
     scoresList=lb.getScores("db.txt")
     #if the current score is in the leaderboard
     #determine if the leaderboard score is a gold, silver, bronze, or none
     #since clicking anywhere on the screen even the turtle is a "miss" then subtract clicks from misses to get actual misses
     if score >= int(scoresList[0]):
          medal.shape("assets/gold.gif")
          medal.showturtle()
          playerName=input("congrats!, you made a gold medal!!\n\tName Please:")
          lb.updateLeaderboard("db.txt",namesList,scoresList,playerName,score) 
     elif score >= int(scoresList[1]):
          if score < int(scoresList[0]):
               medal.shape("assets/silver.gif")
               medal.showturtle()
               playerName=input("congrats, you made a silver medal!\n\tName Please:")
               lb.updateLeaderboard("db.txt",namesList,scoresList,playerName,score) 
     elif score >= int(scoresList[2]):
          if score < int(scoresList[1]):
               medal.shape("assets/bronze.gif")
               medal.showturtle()
               playerName=input("congrats, you made a bronze medal!\n\tName Please:")
               lb.updateLeaderboard("db.txt",namesList,scoresList,playerName,score) 
     if score >= int(scoresList[-1]):        #[-1] grabs last item in list
          if score < int(scoresList[2]):
               playerName=input("congrats, you made the leader board!\n\tName Please:")
               lb.updateLeaderboard("db.txt",namesList,scoresList,playerName,score) 
     #    update the leaderboard
     #draw the leaderboard
     lb.draw_leaderboard(False,namesList,scoresList,scoreKeeper,10)
     overall = click/miss
     overall = round(overall * 100)
     miss = miss - click
     print(f"{click} clicks,{miss} misses,{overall}% accuracy")
     
def updateTimer():
    global timer
    global start
    #subtract one from the time
    timer -= 1
    #draw the time to the screen
    timeKeeper.clear()
    
    #iterate our loop
    #turtleObject, get the screen you're on, and get the timer and run this command after this interval
    if timer<=0:
        timeKeeper.write("Time's Up!",font=fontSetup)
        trent.hideturtle()
        manageLeaderboard()
    else:
        timeKeeper.write(f"Time: {timer}",font=fontSetup)
        timeKeeper.getscreen().ontimer(updateTimer,interval)          #example of recursion
        
def w():
     global start
     start = "true"
        
def startGame():
     #entire purpose of this input is to stall the timer so that it doesn't start before hitting enter
     global start
     timeKeeper.write("Click enter in powershell to start the game")
     start = input("Click enter to start the game")
          
     
     
     
     
    

#---events---   Gold Block from MIT Event Handlers
#object.method(command)
startGame()
trent.onclick(trentClicked)    
wn.onkeypress(w,"s")
wn.onclick(screenClicked)     #in turtle, all objects are clickable 
wn.ontimer(updateTimer,interval)


#--main loop---
wn.mainloop()

'''
     Features List:
     1. Click a turtle
     2. Move turtle randomly
     3. Score
     4. Timer
     5. High Score
'''