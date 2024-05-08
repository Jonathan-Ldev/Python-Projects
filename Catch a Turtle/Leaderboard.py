#This file contains functions to manage the leaderboard
FILENAME="db.txt"   #Constant variable

#to get the names from the db
def getNames(FILENAME):
    #open the db
    file1 = open(FILENAME,"r")
    
    #loop through each line of the file
    names=[]
    for eachLine in file1:
        #get the name from each line
        index=0
        name=""
        while(eachLine[index])!=",":
            eachLetter=eachLine[index]
            name+=eachLetter
            index+=1
        names.append(name)
        
    #return the names
    return names
#to get the scores from the db
def getScores(FILENAME):
    #open the db
    file1=open(FILENAME,"r")
    
    
    #loop through each line of the file
    scores=[]
    for eachLine in file1:
        #get the scores from each line
        data=eachLine.split(",")    #data is a list
        #data -> ["name","number\n"]
        number=data[1].rstrip()
        scores.append(number)
        
    #return the scores
    return scores




#to update the leaderboard
def updateLeaderboard(FILENAME,leaderNames,leaderScores,playerName,currentScore):
    #check if currentScore is in the leaderScores range
    wheretoInsertTheNewData=len(leaderScores)
    for i in range (len(leaderScores)):
        if currentScore>=int(leaderScores[i]):
            wheretoInsertTheNewData=i
            break
    
    #insert player info
    leaderNames.insert(wheretoInsertTheNewData,playerName)
    leaderScores.insert(wheretoInsertTheNewData,currentScore)
    
    #ensure only 5 players
    if(len(leaderNames)>5):
        leaderNames.pop()   #pop() removes last item in the list
        leaderScores.pop()
    
    #save the data back to the database
    file1 = open(FILENAME,"w")
    #loop through the lists and save each list to the file
    for i in range(len(leaderNames)):
        file1.write(f"{leaderNames[i]},{leaderScores[i]}\n")
    file1.close()
    
    

#to draw the leaderboard
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  #high_scorer is a boolean to tell if the current user is a high_scorer
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()
  
  index = 0
  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  while (index < len(leader_scores)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
    index = index + 1
  
  # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.pendown()
  
  #TODO Display message about player making the leaderboard
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  #TODO Display gold/silver/bronze
  
  hsNames=getNames(FILENAME)
  hsScores=getScores(FILENAME)
  #updateLeaderboard(FILENAME,hsNames,hsScores,"bekah",56)
  