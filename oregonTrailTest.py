import time
import sys
import datetime
import random

STARTDATE = datetime.datetime(1848, 3, 1)
currentDate = STARTDATE
print(STARTDATE)
health = 100
oxHealth = 100
totalMiles = 2000
milesTraveled = 0
food = 1000
rations = "full"
healthCondition = "good"
weather = "cold"
pace = "normal"
ox = 5
members = 3


def turn(health, weather, rations, healthCondition, food, currentDate, ox, members):
    weather = random.choice(["hot", "good", "fair", "poor", "windy", "rain", "blizzard"])

    # Sets Health Condition based on amount of Health
    if health >= 80:
        healthCondition = "good"
    elif health < 80 and health >= 50:
        healthCondition = "fair"
    else:
        healthCondition = "poor"

    # Sets ration modifier based on what ration setting you are on.
    if rations == "full":
        rationsModifier = 2
    elif rations == "half":
        rationsModifier = 1
    else:
        rationsModifier = 0.5

    problem = random.choice(
        ["lost", "snake bite", "sick", "ox died", "none", "none", "none", "none", "none", "none", "none", "none",
         "none", "none"])

    if problem == "lost":
        lost = random.randint(1, 7)
        print("One of your members got lost for", lost, "days")
        currentDate += datetime.timedelta(days=lost)
        food -= members * rationsModifier * lost
    elif problem == "snake bite":
        health -= 50
    elif problem == "sick":
        health -= 20
    elif problem == "ox died":
        ox -= 1
        food += 50
    else:
        pass

    print(str.format("""
   .....                                        ..'..                              ..',,,'..
..',;;;,,'...  ...                       ..'''',,;;;;,..                       ..',;;;;;;;;,,,'..
,;;,;;;;;,;;;,,,;,,...               ..',;;;;;,,;;;;;;;;,'..     ..''....',,'',,;;;;;;;;;;,;;;;;,'..
;;;;;;;;;;;;;;;;;;;;;,,....'..   ..',;;;;;;;;;;;;;;;;;;;;;;,'..',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,',,;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
''''''''''''''',,,''''.........'''''',,,''''''''''''',,;;;;;,,,,,,,,,,,,;;;;;;;;;;;;,,,''...'',,,;;;
                                                      ........        ...............            ...
 +-----------------------------+
 |Date:{:_>24}|
 |Weather:{:_>21}|           ..'''''''''''..                         ..''''''.
 |Health:{:_>22}|          ,:ccccllllllllc::::,...  ......  ..,::::::clclllcc,.
 |Miles Traveled:{:_>15}|         .cc'.;cccclccccccccclc'.;cllllc;.'ccccccccccccclcl;.
 |Miles To Go:{:_>17}|          .;c, .,:clcclclcclcclc'.clcccclc.'cccccccccccclll:.
 |Food:{:_>24}|           .cc.  .';cccclcclcclc'.clcccclc.'cccccccccccccc:.
 +-----------------------------+            ,:;.   'ccccccclcclc'.clcccclc.'cccccccccccccc'
                 ..                         .;c;.   ,ccclccccllc'.clcccllc.'cccccclccllcc,
          .,,. .'::.  ....                   .:c.   .clcccccclcc'.cccccclc.'cccccccccccc'
           .,:::cl,..',';c;:;;;;:;;;'.        ',.   .:cccccccccc..:cccccc:.'ccccccccccc:.
         .';clcccl,';;::ccccccccccccc:.       ....  ......,,,,'.  .............',,,,..','.
          ...';:;,,;cccllcclcclccccccc........'.''.',...',.,;',,. .,','',,,  .,'';,','.''.
                .;:clcclcccclllccccc:,.      ...',... .,'. ', .';. ..,',,.. .;. .,. .,,.
                 .'clcccc::;'.,:lclc.         ..''    ';...;;...;'   ''''   ,;..';,..';.
                  .cc,:c;..  .,cc,:c.                 .,'. ', .',.          .;. .,. .,,.
                .':c,..;l'   .';:;:c.                  .',',;','.            .,,';,',.
'..''.''''.'''.',:c:,'';:,''''',::::,'''''...'''''''''''',;;;;,''''''''''..'''';;;;;,'''.''''''''''.
;;;;;;;;;;;;;;,;;:::;;;::;,,;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;,;::::;;;:;;;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;,;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
;;;;;;;;;;;;;;;;;:::;;;::;;;;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;""",
                     currentDate.strftime("%A %b, %d, %Y"), weather, health, milesTraveled, totalMiles, food))
    input()


turn(health, weather, rations, healthCondition, food, currentDate, ox, members)

options = ["Continue on Trail",
           "Check Supplies",
           "Change Pace",
           "Change Rations",
           "Stop to Rest",
           "Attempt to Trade",
           "Hunt for Food"]
