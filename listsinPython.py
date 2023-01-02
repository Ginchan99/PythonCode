#first we import all the packages

import numpy as np

#1 Create a list
listofNos = list(range(10))
print("listofNos=", listofNos)

#create list with alternative nos
#listofNos = list(range(startno,lastno,gap))
listofNos = list(range(1,10,2))
print("listofNos=", listofNos)

#create list of even nos below 10 in reverse
listofNos = list(range(10,1,-2))
print("listofNos=", listofNos)

#can we iterate through the list and print the nos if its a multiple of 3?
listofNos = list(range(1,100,1))
#adding the list at the end of original
listofmulof3 = []
for num in listofNos:
    if num % 3 == 0:
        listofmulof3.append(num)

print("listofmulof3=",listofmulof3)

#get multiples of 3 and 5
listofmulof3 = list(range(3,100,3))
listofmulof5 = list(range(5,100,5))
print("listofmulof3=",listofmulof3,"listofmulof5=",listofmulof5)
listofmulof3and5 = []
for num in listofmulof3:
    if num in listofmulof5:
        listofmulof3and5.append(num)
print("listofmulof3and5=",listofmulof3and5)

#get multiples of 3 or 5, merging them
listofmulof3or5 = listofmulof3+listofmulof5
print("listofmulof3or5=",listofmulof3+listofmulof5)
sortedlistofmulof3or5 = sorted(listofmulof3or5)
print("sortedlistofmulof3or5=",sortedlistofmulof3or5)

#remove duplicates from the list
deduplicatedlist = []
for numIndex in range(1,len(sortedlistofmulof3or5),1):
    num = sortedlistofmulof3or5[numIndex-1]
    next_num = sortedlistofmulof3or5[numIndex]
    if num!= next_num:
        deduplicatedlist.append(num)

print("deduplicatedlist=",deduplicatedlist)
#faster method to remove duplicates
print("fastduplicatedlist=",list(set(sortedlistofmulof3or5)))


listofwords = ["rahul","prateek","tushti","rohit"]
print("meenakshi" in listofwords)
print("prateek" in listofwords)

#take user inputs and print them in order
#rock paper scissors
name = input("What is your name ")
print("Hi %s, Welcome to our game! = "%name) #%s is a string

#noError = False

#while not (noError):
 #   try:
  #      numGames =input("How many games do you want to play ")
   #     numGames = int(numGames)
    #    if(numGames>1 and numGames<100)
     #       noError = True
      #  else:
       #     print("You have made an error, please retry!")
        #noError = True
    #except:
     #   noError = False
#print("Thanks %s, we will play %d games!"%(name,numGames))


hasError = True

while hasError:
    try:
        numGames =input("How many games do you want to play ")
        numGames = int(numGames)
        if(numGames>1 and numGames<100):
            hasError = False
        else:
            print("Err1 You have made an error, please retry!")
    except:
        print("Err 2 You have made an error, please retry!")
        hasError = True
print("Thanks %s, we will play %d games!"%(name,numGames))
ListofChoices = ["Rock","Paper","Scissors"]

def playGame(ListofChoices):
    #get computer choices
    computerchoiceno = np.random.randint(0,2)
    computerchoice = ListofChoices[computerchoiceno]
    print("computerchoice=",computerchoice)
    #get human choices
    hasError = True
    while hasError:
        try:
            yourchoice = input("What is your choice? Please choose between rock, paper and scissors: ")
            if(yourchoice in ListofChoices):
                hasError = False
            else:
                print("ERR 3 You have made an error, please retry!")
        except:
            print("ERR 4 You have made an error, please retry!")
            hasError = True
    print("humanchoice=",yourchoice)
    if(yourchoice=="Rock" and computerchoice=="Rock") or (yourchoice=="Paper" and computerchoice=="Paper") or (yourchoice=="Scissors" and computerchoice=="Scissors"):
        return 0
    if (yourchoice=="Rock" and computerchoice =="Scissors") or (yourchoice=="Paper" and computerchoice=="Rock") or (yourchoice=="Scissors" and computerchoice=="Paper"):
        return 1
    if (yourchoice=="Rock" and computerchoice=="Paper") or (yourchoice=="Paper" and computerchoice=="Scissors") or (yourchoice=="Scissors" and computerchoice=="Rock"):
        return -1

numGamesWon = 0
for gameNo in range(numGames):
    numGamesWon += playGame(ListofChoices)

if(numGamesWon>0):
    print("You won!")
elif(numGamesWon<0):
    print("You lost!")
else:
    print("Game Over")


for gameNo in range(numGames):
    playGame(ListofChoices)