import random

songsPlayed ={}
currentSong = 0

#this function will randomly shuffle the songs
def shuffleSongs(songsList):

    #Everytime a unique list of songs will be generated
    for i in range(0,len(songsList)):
        randomNumber = random.randint(0,len(songsList)-1)

        #swapping the songs in the list  
        songsList[i] , songsList[randomNumber] = songsList[randomNumber], songsList[i]
    pass

#this function will play the next song
def nextSong(songList):
    global songsPlayed,currentSong
    if(currentSong+1 == len(songList)):
        currentSong=0
    else:
        currentSong=currentSong+1
    if(songList[currentSong] not in songsPlayed.keys() ):
        songsPlayed[songList[currentSong]]=1
    
    return songList[currentSong]

#this function will play the previous song
def previousSong(songList):
    global songsPlayed,currentSong
    if(currentSong==0):
        currentSong=len(songsList)-1
    else:
        currentSong = currentSong-1
    if( songList[currentSong] not in songsPlayed.keys() ):
        songsPlayed[songList[currentSong]]=1
    return songList[currentSong]

#this function will play the first song or show the current playing song 
def playCurrentSong(songList):
    global currentSong
    if( songList[currentSong] not in songsPlayed.keys() ):
        songsPlayed[songList[currentSong]]=1
    return songList[currentSong]

#main function starts from here
#with automatically closes the file when its scope ends
try:
    with open("songsFile.txt","r") as songsFile:
        songsList=[]
        for line in songsFile:
            line=line.strip()
            songsList.append(line.strip('\n'))
except:
    print("File Not Found:songsFile.txt")
    exit()
shuffleSongs(songsList)
#print("Shuffled Song List:",songsList)
print("Select from below options:")
print("1.Play Song")
print("2.Play Previous Song")
print("3.Play next Song")
print("4.Exit")
choice = None
while True:
    try:
        choice=int(input("Enter your choice:"))
        if(choice==0):
            print("Wrong Choice!")
            continue
        break
    except ValueError:
        print("input must be a number")
while(choice):
    if(choice==1):
        if(len(songsList)!=len(songsPlayed)):
            print("Current Song is:"+playCurrentSong(songsList))
        else:
            print("All Songs in the list are already played")
            break
    elif(choice==2):
        if(len(songsList)!=len(songsPlayed)):
            print("Playing Next Song:"+previousSong(songsList))
        else:
            print("All Songs in the list are already played")
            break
    elif(choice==3):
        if(len(songsList)!=len(songsPlayed)):
            print("Playing Next Song:"+nextSong(songsList))
        else:
            print("All Songs in the list are already played")
            break
    elif(choice==4):
        break
    else:
        print("Wrong Choice!")
    while True:
        try:
            choice=int(input("Enter your choice:"))
            if(choice==0):
                print("Wrong Choice!")
                continue
            break
        except ValueError:
            print("input must be a number")
        
