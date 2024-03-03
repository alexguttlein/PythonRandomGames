import art
import gameData
import random
from time import sleep
from os import system

def printLogo():
    print(art.logo)

def selectRandomCharacter():
    posSelect = random.randint(0, len(gameData.data)-1)
    return gameData.data[posSelect]

def printCompare(select1, select2):
    print("Compare A: " + select1["name"] + ", a", select1["description"] + ", from " + select1["country"])
    print(art.vs)
    print("Compare B: " + select2.get("name") + ", a", select2.get("description") + ", from " + select2.get("country"))

def makeSelection():
    sel = ''
    while(sel != 'A' and sel != 'B'):
        sel = input("Who has more IG followers? Type 'A' or 'B': ")
        sel = sel.upper()
    return sel

def defineWinner(select1, select2):
    #print("A follows: " + str(select1.get("follower_count")))
    #print("B follows: " + str(select2.get("follower_count")))
    
    if(select1.get("follower_count") > select2.get("follower_count")):
        return 'A'
    return 'B'

def printWaitingAnswer():
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)


'''Inicia el programa'''
contadorAciertos = 0
#select1 = selectRandomCharacter()
select1 = random.choice(gameData.data)
seguirJugando = True

while seguirJugando == True:
    printLogo()
    select2 = selectRandomCharacter()

    while(select1.get("name") == select2.get("name")):
        select2 = selectRandomCharacter()

    winner = defineWinner(select1, select2)

    printCompare(select1, select2)

    selection = makeSelection()
    printWaitingAnswer()

    system('cls')

    if(selection == winner):
        print("CORRECTO")
        contadorAciertos += 1
    else:
        print("INCORRECTO")
        print("")
        seguirJugando = False

    select1 = select2

#print("Tuviste " + str(contadorAciertos) + " aciertos")
print(f"Tuviste {contadorAciertos} aciertos")
