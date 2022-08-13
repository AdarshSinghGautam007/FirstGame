print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. Magnetic field always lies to north!")
Character=input('Choose any character as of your\'s personality:\n"Tokyo" , "Professor" , "Berlin" .\n').lower()

if Character == "tokyo":
  choice1=input('\nWelcome Tokyo. \nYour are at the river bank. Would you follow the "River" or "Compass" .\n').lower()
  if choice1== "compass":
    choice2=input('\nGreat choice! You have to cross the river.What would you like to choose? "Swim" or "Boat".\n').lower()
    if choice2 == "boat":
      choice3=input('\nSaved from 3,700 pounds bite force of Crocodile.\n Dig in front of tree that give oxygen in night."Orchids" or "Hyperion".\n').lower()
      if choice3 =="orchids":
        choice4=input('\nKnowledge of science is important in life and Game too.\n You have three boxes but you can open only one. Good Luck!\n Which Box you wish to open?\n "Red Box" or "Blue Box" or "Green Box".\n').lower()
        if choice4== "blue box":
          print('''
                                    | |      
  ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
 / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
| (_| (_) | | | | (_| | | | (_| | |_\__ \
 \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                  __/ |                  
                 |___/                   
         ''')
          print(''' \n You Are Winner.....!''')
      elif choice4== "red box":
        print("\nScorpions are silent creature untill they are not triggred .Better Luck Next time!")
      elif choice4== "green box":
        print("\nViper have to put healthy person in a second . Better Luck next Time!")
      else:
        print("\nWrong input. Try again!")
        print("\nOops! \n Update your Knowledge.  Game Over! ")
    else:
      print("\nCrocodile will have greate lunch today. Game Over!")
  else:
    print("\nOops! you are in wrong way.Game Over!")

#Professor:
if Character == "professor":
  choice1=input('\nWelcome Professor. \nYour are at the river bank. Would you follow the "River" or "Compass" .\n').lower()
  if choice1== "compass":
    choice2=input('\nGreat choice! You have to cross the river.What would you like to choose? "Swim" or "Boat".\n').lower()
    if choice2 == "boat":
      choice3=input('\nSaved from 3,700 pounds bite force of Crocodile.\n Dig in front of tree that give oxygen in night."Orchids" or "Hyperion".\n').lower()
      if choice3 =="orchids":
        choice4=input('\nKnowledge of science is important in life and Game too.\n You have three boxes but you can open only one. Good Luck!\n Which Box you wish to open?\n "Red Box" or "Blue Box" or "Green Box".\n').lower()
        if choice4== "blue box":
          print('''
                                    | |      
  ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
 / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
| (_| (_) | | | | (_| | | | (_| | |_\__ \
 \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                  __/ |                  
                 |___/                   
         ''')
          print(''' \n You Are Winner.....!''')
      elif choice4 == "red box":
        print("\nScorpions are silent creature untill they are not triggred .Better Luck Next time!")
      elif choice4 == "green box":
        print("\nViper have to put healthy person in a second . Better Luck next Time!")
      else:
        print("\nWrong input. Try again!")
        print("\nOops! \n Update your Knowledge.  Game Over! ")
    else:
      print("\nCrocodile will have greate lunch today. Game Over!")
  else:
    print("\nOops! you are in wrong way.Game Over!")

#Berlin:

if Character == "berlin":
  choice1=input('\nWelcome Berlin. \nYour are at the river bank. Would you follow the "River" or "Compass" .\n').lower()
  if choice1== "compass":
    choice2=input('\nGreat choice! You have to cross the river.What would you like to choose? "Swim" or "Boat".\n').lower()
    if choice2 == "boat":
      choice3=input('\nSaved from 3,700 pounds bite force of Crocodile.\n Dig in front of tree that give oxygen in night."Orchids" or "Hyperion".\n').lower()
      if choice3 =="orchids":
        choice4=input('\nKnowledge of science is important in life and Game too.\n You have three boxes but you can open only one. Good Luck!\n Which Box you wish to open?\n "Red Box" or "Blue Box" or "Green Box".\n').lower()
        if choice4== "blue box":
          print('''
                                    | |      
  ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
 / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
| (_| (_) | | | | (_| | | | (_| | |_\__ \
 \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                  __/ |                  
                 |___/                   
         ''')
          print(''' \n You Are Winner.....!''')
      elif choice4 == "red box":
        print("\nScorpions are silent creature untill they are not triggred .Better Luck Next time!")
      elif choice4 == "green box":
        print("\nViper have to put healthy person in a second . Better Luck next Time!")
      else:
        print("\nWrong input. Try again!")
        print("\nOops! \n Update your Knowledge.  Game Over! ")
    else:
      print("\nCrocodile will have greate lunch today. Game Over!")
  else:
    print("\nOops! you are in wrong way.Game Over!")
