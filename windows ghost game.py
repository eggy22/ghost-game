import os
import time

print("Full screen is recommended for better experience")
level = (0)
time.sleep(1)
print("....")

time.sleep(1)
print("...")

time.sleep(1)
print("..")

time.sleep(1)
print(".")

time.sleep(1)
os.system('cls')
while True:

    x = input("""Hello this is just a small text based game 
The rules are simple ex: like left or right
Would you like to start the game y/n
                       \nyou:""").lower()

    if x == 'n':
        print("See you later..")
        time.sleep(1)
        exit()

    elif x == 'y':
        os.system('cls')       
        print("Alright then lets start the game..")
        time.sleep(2)
        os.system('cls')
        
    else:
            print("type a valid ans ")
            time.sleep(1)
            os.system('cls')
            continue

    q = input("""You are stuck in a house 
and you see a door and a window to hall way 
which way u go? (door,window)\nyou: """).lower()
    
    if q == 'window':
        os.system('cls')
        level += 1
        print("Level " + str(level))
        o = input("""

  o=(=(=(=(=(=(=)=)=)=)=o
     !-'-'-'-/_\-'-'-'-! 
     ! !  , /___\`  ! !!
     !!! , /  |  \`  ! !
     !!  ,|___|___`  !!!
     !_,| |_______|` `_!
     !-`| |       | |,-!
     !!!! |       | ! !!
     !!!! |       | !!!!
     !!!!_|_______|_!!!!
     !!!!___________!!!! 
     !!!!           !!!!   
     !!!!           !!!!   
     !!!!           !!!!   
     !!!!           !!!!   


You opened the window jumped
but you fell and DIED... 
do you want to play agin? (y,n)\nyou: """).lower()
        if o =='y':
            os.system('cls')
            continue
            break
        os.system('cls')
        
        
    elif q == 'door':
        os.system('cls')
        level += 1
        print("Level " + str(level))
        print("""
     ______________
    |\ ___________ /|
    | |  /|,| |   | |
    | | |,x,| |   | |
    | | |,x,' |   | |
    | | |,x   ,   | |
    | | |/    |   | |
    | |    /] ,   | |
    | |   [/ ()   | |
    | |       |   | |
    | |       |   | |
    | |       |   | |
    | |      ,'   | |
    | |   ,'      | |
    |_|,'_________|_|  
    """)

    else:
         print("type a valid ans ")
         time.sleep(1)
         os.system('cls')
         continue
        

    print("You opened the door and walk to the hall way")
    time.sleep(2)
    print("and its very dark u cant see anything")
    time.sleep(3)
    os.system('cls')
    print("Level 2")
    print("""  
    /
   /
  /____________________
  |________  __________
  /_____  /||   |
 |".___."| ||   |
 |_______|/ |   |
  || .___."||  /
  ||_______|| /
  |_________|/
and you found a Drawer                                               """)
    o = input("do u want to search the drawer or no (search,dont search)\nyou: ")
    if o == 'dont search':
        exit("you died by falling down without light")
        time.sleep(2)
        

    elif o == 'search':
        os.system('cls')
        level += 2
        print("Level " + str(level))

        o = input("""
        _________
        |_______|
        |       |
        |       |
        |       |
        |_______|
You found a lighter do u want to light the lighter (light,dont light)\nyou: """).lower()
    else:
        print("type a valid ans")
        os.system('cls')
        time.sleep(2)
        continue   
    os.system('cls')
    
    if o == 'dont light':
        exit("You died by hitting your head on the wall")
        time.sleep(2)
    elif o == 'light':
        level += 1
        print("Level " + str(level))

        input("""
     ___    A
     | |   {*}
     | |  __V__
     |_|o_|%%%|0_
        |       |
        |       |
        |       | 
        |       |
        |_______|
    
    
    You light the lighter and you found a paper on the floor  \n clike enter to read the paper: """)

    os.system('cls')
    level += 1
    print("Level " + str(level))

    print("""
    
     $$$$$$\   $$$$$$\  $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
    $$$ __$$\ $$$ __$$\ \____$$  |$$  ____| $$  __$$\ $$  __$$\ $$  __$$\ 
    $$$$\ $$ |$$$$\ $$ |    $$  / $$ |      $$ /  \__|$$ /  $$ |\__/  $$ |
    $$\$$\$$ |$$\$$\$$ |   $$  /  $$$$$$$\  $$$$$$$\  \$$$$$$$ | $$$$$$  |
    $$ \$$$$ |$$ \$$$$ |  $$  /   \_____$$\ $$  __$$\  \____$$ |$$  ____/ 
    $$ |\$$$ |$$ |\$$$ | $$  /    $$\   $$ |$$ /  $$ |$$\   $$ |$$ |      
    \$$$$$$  /\$$$$$$  /$$  /     \$$$$$$  | $$$$$$  |\$$$$$$  |$$$$$$$$\ 
     \______/  \______/ \__/       \______/  \______/  \______/ \________|
    
    
    
      you found a code on the paper u walking around to the house 
      and you found a lock that need a code to unlock (rembering this code might help) 
                """)
    input("click enter to unlock the lock ")
    os.system('cls')
    level += 1
    print("Level " + str(level))
    y = input("""
         .--------.
        / .------. '
       / /        \ '
       | |        | |
      _| |________| |_
    .' |_|        |_| '.
    '._____ ____ _____.'
    |     .'____'.     |
    '.__.'.'    '.'.__.'
    '.__  |     |  __.'
    |   '.'.____.'.'   |
    '.____'.____.'____.'
    '.________________.'
    
        you found a lock that need a code to unlock what is the code u saw on the paper 
        that might unlock  \nyou: """)

    if y == '0075692':
        os.system('cls')
        print("""
         .-------
        / .------
       / /        
       | |        
      _| |________    _
    .' |_|            '.
    '._____ ____ _____.'
    |     .'____'.     |
    '.__.'.'    '.'.__.'
    '.__  | YALE |  __.'
    |   '.'.____.'.'   |
    '.____'.____.'____.'
    '.________________.'
    
       congratulations you unlocked the lock to a door """ )  

    else:
        i = input("sorry the code was wrong you died there was a ghost hunting you...(do you want to play agin? y/n)")
        if i == 'n':
            exit('alr see you have a good day..')
            time.sleep(3)
        elif i == 'y':
            os.system('clear')
            continue
       
    l = input( """and you see a big ocean and you see a working boat what will you do 
       get in the boat or ignore (get in the boat,ignore)\n you: """)
    
    if l == 'ignore':
        p = input("""oops u died from a ghost..
        do you want to play agin ? y/n""")
        if p == 'y':
            os.system('cls')
            continue
        else:
            exit("sorry didint get that.. restarting game in 5 sec")
            time.sleep(5)
            os.system('cls')
            continue
            
    elif l == 'get in the boat':
        os.system('cls')
        print("""
                    |
                    |
           |        |
         |-|-|      |
           |        |
           | {O}    |
           '--|     |
             .|]_   |
       _.-=.' |     |
      |    |  |]_   |
      |_.-='  |   __|__
       _.-='  |\   /|\
      |    |  |-'-'-'-'-.
      |_.-='  '========='
           `   |     |
            `. |    / \
              ||   /   \____.--=''''==--.._
              ||_.'--=='    |__  __  __  _.'
              ||  |    |    |\ ||  ||  || |                        ___
 ____         ||__|____|____| \||__||__||_/    __________________/|   |
|    |______  |===.---. .---.========''''=-._ |     |     |     / |   |
|    ||     |\| |||   | |   |      '===' ||  \|_____|_____|____/__|___|
|-.._||_____|_\___'---' '---'______....---===''======//=//////========|
|--------------\------------------/-----------------//-//////---------/
|               \                /                 // //////         /
|                \______________/                 // //////         /
|                                        _____===//=//////=========/
|==============================================================LGB/
'----------------------------------------------------------------`

    
you get in the boat and drive away and you escaped
""")
    break

input(""" made by eggy 
discord id = eggy#2646
thanks for playing this game...have a good day :D(clike enter to close)""") 