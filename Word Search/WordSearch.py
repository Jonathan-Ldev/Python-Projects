FILENAME = "board.txt"
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

board = []
finalBoard = []
line = []
column = 0
victory = "f"
loop = "t"
rowN = 0
colN = 0
direction = ""
#board = [["P", "L", "A", "I", "T", "R", "Q", "L", "F", "D", "L"],
#         ["O", "C", "L", "Z", "A", "P", "E", "Q", "U", "S", "B"],
#         ["P", "M", "O", "E", "N", "S", "Y", "C", "Q", "U", "I"],
#         ["T", "B", "H", "M", "H", "L", "K", "S", "U", "D", "N"],
#         ["A", "W", "C", "Y", "P", "S", "N", "N", "B", "Z", "A"],
#         ["R", "E", "B", "S", "Z", "U", "R", "Q", "Q", "Y", "R"],
#         ["T", "H", "C", "R", "I", "K", "T", "E", "H", "R", "Y"],
#         ["S", "S", "E", "T", "V", "G", "E", "E", "W", "D", "I"],
#         ["V", "P", "B", "B", "A", "N", "D", "E", "R", "O", "L"],
#         ["W", "P", "O", "B", "O", "G", "A", "B", "T", "K", "P"],
#         ["L", "A", "M", "I", "C", "E", "D", "A", "X", "E", "H"],]
word = ""
wordCheck = []
def importWords():
     global word
     word = list(input("What word do you want to find (MUST BE IN ALL CAPS) "))
     return word

def importBoard():
     # credit to alex for providing the entirety of the code to import the board
     global board
     global line
     global column
     file1 = open(FILENAME,"r") #opens the file and has all the cahracters needed
     
     letters=[]
     for eachLine in file1:  #looks through all the .txt file (utilized and modified from Leaderboard CAT notes)
          index=0
          letter=""
          try:      #prevents python from crashing when it hits the end of one of the lines of the file.
               while(eachLine[index]!="\t"):
                    eachLetter=eachLine[index]
                    letter+=eachLetter
                    index+=2            #skips the \t's in the file and takes all the characters inbetween
                    letters.append(letter)        #takes the found letter and puts it into a list representing the row it's in
                    letter=""     #clears the letter for the next letter in the line
          except:        #sends out data despite the error from reaching the end of the line
               board.append(letters)    #appends the list with a line of letters to another list then clears it for the next line
               # add one the variable when switching to next line to indicate amount of columns
               column += 1
               letters=[]
               
     letters=[]

     index=0
     letter=""
     try:      #prevents python from crashing when it hits the end of one of the lines of the file.
          #find one row to use as the variable for amount in a row
          while(eachLine[index]!="\t"):
               eachLetter=eachLine[index]
               letter+=eachLetter
               index+=2            #skips the \t's in the file and takes all the characters inbetween
               line.append(letter)        #takes the found letter and puts it into a list representing the row it's in
               letter=""     #clears the letter for the next letter in the line
     except:        #sends out data despite the error from reaching the end of the line
          letters=[]
     
     return board, line, column

def printBoard(board):
     print(board)

def searchHorizontally(word,board):
     global wordCheck
     global victory
     global rowN
     global colN
     global direction
     #run the word check through every letter in a row for every column
     for row in range(len(line)):
          for col in range(column):
               #check if the initial letter is the same as the words initial letter
               if word[0] == board[row][col]:
                    #check every letter from the start to the right of the inital letter for the words length
                    for i in range(len(word)):
                         #stop the loop if it starts checking out of range of the board
                         if col + i >= len(line):
                             break
                        #if the letter is the same then appened to a list unless the list is already the same as the word
                         if word[i] == board[row][col+i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck.append(word[i])
                                   if len(wordCheck) == len(word):
                                        rowN = row +1
                                        colN = col +1
                                        direction = "right"
                         #if the letter is not the same then clear the list unless the list is already the same as the word
                         elif word[i] != board[row][col+i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck = []
     if wordCheck == word:
          print(f"Word Found! {wordCheck}")
          victory = "t"
          printBoard(board)
          print(f"Starting letter location is at row{rowN} col{colN} going {direction}")
def searchHorizontallyReverse(word,board):
     global wordCheck
     global victory
     global rowN
     global colN
     global direction
     #run the word check through every letter in a row for every column
     for row in range(len(line)):
          for col in range(column):
               #check if the initial letter is the same as the words initial letter
               if word[0] == board[row][col]:
                    #check every letter from the start to the right of the inital letter for the words length
                    for i in range(len(word)):
                         #don't need the limiter for reverse??? seems to break it
                        
                        #if the letter is the same then appened to a list unless the list is already the same as the word
                         if word[i] == board[row][col-i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck.append(word[i])
                                   if len(wordCheck) == len(word):
                                        rowN = row +1
                                        colN = col +1
                                        direction = "left"
                         #if the letter is not the same then clear the list unless the list is already the same as the word
                         elif word[i] != board[row][col-i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck = []
     if wordCheck == word:
          if victory == "f":
               print(f"Word Found! {wordCheck}")
               victory = "t"
               printBoard(board)
               print(f"Starting letter location is at row{rowN} col{colN} going {direction}")
          else:
               pass
               

def searchVerically(word,board):
     global wordCheck
     global victory
     global rowN
     global colN
     global direction
     #run the word check through every letter in a row for every column
     for row in range(len(line)):
          for col in range(column):
               #check if the initial letter is the same as the words initial letter
               if word[0] == board[row][col]:
                    #check every letter from the start to the right of the inital letter for the words length
                    for i in range(len(word)):
                         #stop the loop if it starts checking out of range of the board
                         if row + i > column-1:
                             break
                        #if the letter is the same then appened to a list unless the list is already the same as the word
                         if word[i] == board[row+i][col]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck.append(word[i])
                                   if len(wordCheck) == len(word):
                                        rowN = row +1
                                        colN = col +1
                                        direction = "down"
                         #if the letter is not the same then clear the list unless the list is already the same as the word
                         elif word[i] != board[row+i][col]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck = []
     if wordCheck == word:
          if victory == "f":
               print(f"Word Found! {wordCheck}")
               victory = "t"
               printBoard(board)
               print(f"Starting letter location is at row{rowN} col{colN} going {direction}")
          else:
               pass
          
def searchVerticalReverse(word,board):
     global wordCheck
     global victory
     global rowN
     global colN
     global direction
     #run the word check through every letter in a row for every column
     for row in range(len(line)):
          for col in range(column):
               #check if the initial letter is the same as the words initial letter
               if word[0] == board[row][col]:
                    #check every letter from the start to the right of the inital letter for the words length
                    for i in range(len(word)):
                        #if the letter is the same then appened to a list unless the list is already the same as the word
                         if word[i] == board[row-i][col]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck.append(word[i])
                                   if len(wordCheck) == len(word):
                                        rowN = row +1
                                        colN = col +1
                                        direction = "up"
                         #if the letter is not the same then clear the list unless the list is already the same as the word
                         elif word[i] != board[row-i][col]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck = []
     if wordCheck == word:
          if victory == "f":
               print(f"Word Found! {wordCheck}")
               victory = "t"
               printBoard(board)
               print(f"Starting letter location is at row{rowN} col{colN} going {direction}")
          else:
               pass
def searchUpRightDiagonal(word,board):
     global wordCheck
     global victory
     global rowN
     global colN
     global direction
     #run the word check through every letter in a row for every column
     for row in range(len(line)):
          for col in range(column):
               #check if the initial letter is the same as the words initial letter
               if word[0] == board[row][col]:
                    #check every letter from the start to the right of the inital letter for the words length
                    for i in range(len(word)):
                         #stop the loop if it starts checking out of range of the board
                         #COMPUTER caused a lot of problems, had to put a lot more limiters, dont know why
                         if row + i > column:
                             break
                         if col + i > len(line)-1:
                              break
                        #if the letter is the same then appened to a list unless the list is already the same as the word
                         if word[i] == board[row-i][col+i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck.append(word[i])
                                   if len(wordCheck) == len(word):
                                        rowN = row +1
                                        colN = col +1
                                        direction = "up right"
                         #if the letter is not the same then clear the list unless the list is already the same as the word
                         elif word[i] != board[row-i][col+i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck = []
     if wordCheck == word:
          if victory == "f":
               print(f"Word Found! {wordCheck}")
               victory = "t"
               printBoard(board)
               print(f"Starting letter location is at row{rowN} col{colN} going {direction}")
          else:
               pass    

def searchDownRightDiagonal(word,board):
     global wordCheck
     global victory
     global rowN
     global colN
     global direction
     #run the word check through every letter in a row for every column
     for row in range(len(line)):
          for col in range(column):
               #check if the initial letter is the same as the words initial letter
               if word[0] == board[row][col]:
                    #check every letter from the start to the right of the inital letter for the words length
                    for i in range(len(word)):
                         if col + i > len(line)-1:
                              break
                         if row + i > column-1:
                              break
                        #if the letter is the same then appened to a list unless the list is already the same as the word
                         if word[i] == board[row+i][col+i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck.append(word[i])
                                   if len(wordCheck) == len(word):
                                        rowN = row +1
                                        colN = col +1
                                        direction = "down right"
                         #if the letter is not the same then clear the list unless the list is already the same as the word
                         elif word[i] != board[row+i][col+i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck = []
     if wordCheck == word:
          if victory == "f":
               print(f"Word Found! {wordCheck}")
               victory = "t"
               printBoard(board)
               print(f"Starting letter location is at row{rowN} col{colN} going {direction}")
          else:
               pass

def searchUpLeftDiagonal(word,board):
     global wordCheck
     global victory
     global rowN
     global colN
     global direction
     #run the word check through every letter in a row for every column
     for row in range(len(line)):
          for col in range(column):
               #check if the initial letter is the same as the words initial letter
               if word[0] == board[row][col]:
                    #check every letter from the start to the right of the inital letter for the words length
                    for i in range(len(word)):
                         #no limter for left, I really don't know why
                        #if the letter is the same then appened to a list unless the list is already the same as the word
                         if word[i] == board[row-i][col-i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:     
                                   wordCheck.append(word[i])
                                   if len(wordCheck) == len(word):
                                        rowN = row +1
                                        colN = col +1
                                        direction = "up left"
                         #if the letter is not the same then clear the list unless the list is already the same as the word
                         elif word[i] != board[row-i][col-i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck = []
     if wordCheck == word:
          if victory == "f":
               print(f"Word Found! {wordCheck}")
               victory = "t"
               printBoard(board)
               print(f"Starting letter location is at row{rowN} col{colN} going {direction}")
          else:
               pass
          
def searchDownLeftDiagonal(word,board):
     global wordCheck
     global victory
     global rowN
     global colN
     global direction
     #run the word check through every letter in a row for every column
     for row in range(len(line)):
          for col in range(column):
               #check if the initial letter is the same as the words initial letter
               if word[0] == board[row][col]:
                    #check every letter from the start to the right of the inital letter for the words length
                    for i in range(len(word)):
                         #needs a limiter for down left, seriously why
                         if row + i > column-1:
                              break
                        #if the letter is the same then appened to a list unless the list is already the same as the word
                         if word[i] == board[row+i][col-i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:     
                                   wordCheck.append(word[i])
                                   if len(wordCheck) == len(word):
                                        rowN = row +1
                                        colN = col +1
                                        direction = "down left"
                         #if the letter is not the same then clear the list unless the list is already the same as the word
                         elif word[i] != board[row+i][col-i]:
                              if len(wordCheck) == len(word):
                                   pass
                              else:
                                   wordCheck = []
     if wordCheck == word:
          if victory == "f":
               print(f"Word Found! {wordCheck}")
               victory = "t"
               printBoard(board)
          else:
               pass
          
#printing and coloring the board code by alex
def printBoard(board):
     for i in range(len(board)):
          print(" ".join(board[i]))


importBoard()
importWords()
searchHorizontally(word,board)
searchHorizontallyReverse(word,board)
searchVerically(word,board)
searchVerticalReverse(word,board)
searchUpRightDiagonal(word,board)
searchDownRightDiagonal(word,board)
searchUpLeftDiagonal(word,board)
searchDownLeftDiagonal(word,board)



