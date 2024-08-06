#Song Game Program, Pseudocode
#imports the random library
import random
#import the sleep function from the time library
from time import sleep
#import my custom encryption class and library
import Encryption as Class
#sets a key for encryption
#set key as int
key = 1028

#set songFile as file
#opens the song list file
songFile = open("songList.txt", "r")
#set songFileReas as list
#reads the lines from the songFile
songFileRead = songFile.readlines()
#closes the songFile
songFile.close()

#define the procedure main()
def main():
  #global the varibale users
  global users
  #set userFile as file
  #opens the user list file
  userFile = open("users.txt", "r")
  #set userFileRead as list
  #reads the lines from the userFile
  userFileRead = userFile.readlines()
  #closes the userFile
  userFile.close()
  #set users as list
  #creates a blank list
  users = []
  #starts a for loop
  for i in userFileRead:
    #print(i)
    #strips each line of "\n"
    usersFileTemp = i.strip("\n")
    #splits each line of "--"
    usersFileTemp = usersFileTemp.split("--")
    #print(usersFileTemp[0])
    #adds the line to the users list
    users += usersFileTemp
    #print(users)  
  #global the variables points, login and user
  global points
  global login
  global user
  #set user as str
  #asks the user to input their name
  user = str(input("What is your name: "))
  #if user is alphanumerical
  if user.isalpha():
    #output "Name authorised"
    print("Name authorised")
    #wait for 0.2 seconds 
    sleep(0.2)
    #set points as int
    #sets points to equal 0
    points = 0
  #if user is not alphanumerical
  else: 
    #output "Error, Name not authorised"
    print("Error, Name not authorised")
    #wait for 0.2 seconds 
    sleep(0.2)
    #call the procedure main()
    main()
  #set choose as str
  #ask the user if they would like to login
  choose = str(input("Would you like to login? (Yes or No) "))
  #if choose is alphanumerical 
  if choose.isalpha():
    #if choose.lower() is equal to "yes" then
    if choose.lower() == "yes":
      #set login as boolean Value
      #sets login to True
      login = True
      #calls the procedure findUser()
      findUser()
    #if choose.lower() is equal to "no" then
    elif choose.lower() == "no":
      #set login as boolean Value
      #sets login as False
      login = False
      #calls the proceudre song()
      song()
    #if choose.lower() is not equal to "yes" or "no" then
    else: 
      #output "Error, Selection Not Found"
      print("Error, Selection Not Found")
      #wait for 0.2 seconds 
      sleep(0.2)
      #calls the proceudre main
      main()
  #if choose is not alphanumerical then
  else:
    #output "Error, enter a valid input"
    print("Error, enter a valid input")
    #calls the procedure main
    main()

#define the procedure findUser()
def findUser():
  #global the variables userCurrentRank, userNames, users, userFileRead, encryptedPass, login
  global userCurrentRank
  global userNames
  global users
  global userFileRead
  global encryptedPass
  global login
  #creates a for loop
  for i in range(0, len(users), 3):
    #if users[i].lower() is equal to the user.lower() then
    if users[i].lower() == user.lower():
      #output "User Found"
      print("User Found")
      #wait for 0.2 seconds 
      sleep(0.2)
      #set password as str
      #asks the user for their password 
      password = str(input("Please enter your password: "))
      #encypts this password
      passToEncrypt = Class.encryption(password, key)
      encryptedPass = passToEncrypt.encrypt()
      #if password. is equal to users[i+2] then
      if encryptedPass == users[i+2]:
        #output password accepted
        print("Password accepted")
        #output "User's Previous Score:", users[i+1]
        print("User’s Previous Score:", users[i+1])
        #print(users[i])
        #set userCurrentRank as int
        #sets userCurrentRank as i 
        userCurrentRank = i
        #calls the procedure song()
        song()      
      #if password is not equal to users[i+2] then
      else:
        #output password denied
        print("password denied")
        #calls the findUser() procedure
        findUser()
  #if users[i].lower() is not equal to the user.lower() then
  #output user not found
  print("User not found")
  #sets login to false becuase the user couldnt be found 
  login = False

  #calls the procedure song()
  song()

#defines the procedure song()
def song():
  #globals the variables songArtist and songTitle
  global songArtist
  global songTitle
  #set songArtist as str
  #creates a blank string
  songArtist = ""
  #set songTitla as list
  #creates a blank list
  songTitle = []
  #if the length of songFileRead is less than or equal to 1 then
  if len(songFileRead) <= 1:
    #if login is True then
    if login == True:
      #call the procedure writeUserFile()
      writeUserFile()
    #if login is not True then
    else: 
      #call the procedure writeFile()
      writeFile()
  ##print(len(songFileRead))
  #set randNo as int
  #creates a random number between 0 and the length of songFileRead -1
  randNo = random.randint(0, len(songFileRead)-1)
  ##print(randNo)
  #set songFileTemp as list
  #strips songFileRead[randNo] of "\n"
  songFileTemp = songFileRead[randNo].strip("\n")
  #splits songFileTemp at "--"
  songFileTemp = songFileTemp.split("--")
  #sets the songArtist as the first element in songFileTemp
  songArtist = songFileTemp[0]
  #sets songTitleTemp as the second element in songFileTemp
  songTitleTemp = songFileTemp[1]
  #adds to songTitle the songTitleTemp split at " "
  songTitle += songTitleTemp.split(" ")
  #output "Song Chosen"
  print("Song Chosen") 
  #takes the song out of songFileRead so the song doesn't get chosen again 
  songFileRead.pop(randNo)
  #calls the proceudre userGuess()
  userGuess()

#defines the procedure userGuess()
def userGuess():
  #globals the variable points
  global points
  #set guessNo as int
  #sets guessNo as 0
  guessNo = 0 
  #while guessNo is less than 2 then
  while guessNo < 2:
    ##print(guessNo)
    #set rightWords as int
    #sets rightWords as 0
    rightWords = 0
    #outputs the Song Artist's name
    print("Song Artist:", songArtist)
    #outputs "Song Name"
    print("Song Name:")
    #creates a for loop
    for i in songTitle:
      #output the first letter in each element of songTitle
      print(i[0])
      #wait for 0.1 seconds 
      sleep(0.1)
    #set guess as str
    #asks the user to guess the song
    guess = str(input("Please Enter Your Guess: "))
    #set splitGuess as list
    #splits the guess up into seperate words
    splitGuess = guess.split(" ")
    #if the length of songTitle is not less than the length of splitGuess then
    if  len(songTitle) == len(splitGuess):
      #creates a for loop
      for i in range(len(splitGuess)):
        #if splitGuess[i].lower() is equal to songTitle[i].lower() then
        if splitGuess[i].lower() == songTitle[i].lower(): 
          #add 1 to rightWords 
          rightWords += 1
    #if the length of songTitle is less than the length of splitGuess then
    else:
      #adds 0 to rightWords
      rightWords += 0
    #if rightWords is equal to the length of songTitle then
    if rightWords == len(songTitle):
      #output "Well Done, you got the song Correct"
      print("Well Done, you got the song Correct")
      #wait for 0.2 seconds 
      sleep(0.2)
      #if guessNo is eqaul to 0 then
      if guessNo == 0:
        #add 3 to points
        points += 3
        #call the procedure song
        song()
      #if guessNo is not equal to 0 then
      else:  
        #add 1 to points
        points += 1
        #call the procedure song
        song()
    #if rightWords is not euqal to the length of songTitle then
    else: 
      #output "Not quite, Try again"
      print("Not quite, Try again")
      #wait for 0.2 seconds 
      sleep(0.2)
      #add 1 to guessNo
      guessNo += 1
  #if guessNo is equal to 2 
  if guessNo == 2:
    #output "That is all your attmepts"
    print("That is all your attempts")
    #wait for 0.2 seconds 
    sleep(0.2)
    #output the user's score
    print("You scored: ", points, "points")
    ##print(user)
    #if login is equal to True then
    if login == True:
      #calls the procedure writeUserFile()
      writeUserFile()
    #if login is not equal to True then
    else: 
      #calls the procedure writeFile()
      writeFile()


#defines the procedure writeFile()
def writeFile():
  #set userWrote as boolean Value
  #set userWrote to False
  userWrote = False
  #set userLength as int
  #sets userLength the the length of users
  userLength = len(users)
  #sets userFile as File
  #opens the file "users.txt" in the mode write
  userFile = open("users.txt", "w")
  #creates a for loop
  #set password as str
  #asks the user to set a password
  password = str(input("What is you password going to be? "))
  #set confirmPW as str
  #confirms the users password
  confirmPW = str(input("Confirm your password: "))
  #if password is equal to confermPW then
  if password == confirmPW:
    #output password confirmemed
    print("password confirmed")
    #encrypts the password
    passToEncrypt = Class.encryption(password, key)
    encryptedPassword = passToEncrypt.encrypt()
    #creates a for loop
    for i in range(0, userLength, 3):
      #print(i)
      # if i % 2 != 0:
      #   i -= 1
      #if int(users[i+1]) is less than points and userWrote is False then
      if int(users[i+1]) < points and userWrote == False:
        #set userWrote to True
        userWrote = True
        #write to userFile the user's name and points and password
        userFile.write(user + "--" + str(points) + "--" + encryptedPassword + "\n")
        #minus 1 from userLength
        userLength -= 1
        #write to userFile users[i] and users[i+1] and users[i+2]
        userFile.write(users[i] + "--" + users[i+1] + "--" + users[i+2] + "\n")
      #if int(users[i+1]) is not less than points or userWrote is not False then
      else: 
        #write to the userFile users[i] and users[i+1] and users[i+2]
        userFile.write(users[i] + "--" + users[i+1] + "--" + users[i+2] + "\n")
  #if password is not equal to confirmPW then
  else:
    #output passwords do not mach
    print("passwords do not match")
    #call the writeFile() procedure
    writeFile()
  #if userWrote is False then
  if userWrote == False:
    #write to the user file the user's name and points and password
    userFile.write(user + "--" + str(points) + "--" + encryptedPassword + "\n")
  #output "File Updated"
  print("File Updated")
  #close the userFile
  userFile.close()
  #calls the proceudre topScores()
  topScores()


#defines the proceudre writeUserFile()
def writeUserFile():
  #set userWrote as boolean value
  #sets userWrote as False
  userWrote = False
  #set userFile as file
  #opens the file "users.txt" in the mode write 
  userFile = open("users.txt", "w")
  #set userLength as int
  #sets userLength as the length of users
  userLength = len(users)
  #creates a for loop
  for i in range(0, userLength, 3):
    #if users[i].lower() is equal to user.lower() and userWrote is False then 
    if users[i].lower() == user.lower() and userWrote == False and users[i+2] == encryptedPass:
      ## userLength -= 1
      #if int(users[i+1]) is less than points then
      if int(users[i+1]) < points:
        #sets userWrote as True
        userWrote = True
        #writes to userFile the user's name and points
        userFile.write(user + "--" + str(points) + "--" + encryptedPass + "\n")
        #output "New Hight Score!!"
        print("New High Score!!!")
        #wait for 0.5 seconds
        sleep(0.5)
      #if int(user[i+1]) is not less than points then
      else:
        #sets userWrote as True
        userWrote = True
        #writes to the userFile the user's name and old score
        userFile.write(users[i] + "--" + users[i+1] + "--" + users[i+2] + "\n")
    #if users[i].lower() is not equal to user.lower() or userWrote is not False then
    else: 
      #writes to the userFile users[i] and users[i+1]
      userFile.write(users[i] + "--" + users[i+1] + "--" + users[i+2] + "\n")
  #if userWrote is False thne
  if userWrote == False:
    #write to the userFile the user's name and points
    userFile.write(user + "--" + str(points) + "--" + encryptedPass + "\n")  
    #output "User not found"
    print("User not found")
    #wait for 0.2 seconds
    sleep(0.2)
  #output "File Updated"
  print("File Updated")
  for x in range (1, 75):
    print("\n")
  #closes the userFile
  userFile.close()
  #calls the procedure topScores()
  topScores()


#defines the procedure topScores()
def topScores():
  #if the length of users is greater than 10 then
  if len(users) > 15:
    #create a for loop
    for i in range(0,10,3):
      #output i, users[i] and users[i+1]
      print((i//3), ".", users[i], "       ", users[i+1])
      #wait for 0.7 seconds
      sleep(0.7)
  #calls the proceudre main()
  main()
	
#calls the procudre main()
main()


# **FEEDBACK

# WOW 