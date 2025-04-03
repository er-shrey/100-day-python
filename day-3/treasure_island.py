print("""
                                   ___
                                   T T
                                   ===
                                   |.|
                                  .'.`.
                                .'.' `.`.
                  %%          .'.' ___ `.`.
                 %%%%       .'.'  |_|_|  `.`.
                %%%%%%    .'.'    |_|_|    `.`.
                %%%%%__.--`'| []  |_|_|  [] |`'---.
__              %%%%|------||               |||||||
 /\     =========%%%|    _&||      ___      ||===='
/  \   ///////////H/| j |  ||     |_|_|     ||    |
||||  ////////////H%|   |- ||     |_|_|     ||____|
|||| /////////////H/|   |  ||     |_|_|     ||  TT|       .   &
|||| @@@@@@@@@@@@@H@|======||               ||====|  "==='   (f
|\//|\/|/\//\||//|\|||/\//|//\||\//||//|\||\||\/|/\//\||////|//\/||
""")

print("Welcome to treasure island.\nYour mission is to find the treasure")

check_1 = input("left or right\n").lower()

if check_1 == "left":
    check_2 = input("swim or wait\n").lower()
    if check_2 == "wait":
        door = input("Which door? red, blue, yellow\n").lower()
        if door == "blue":
            print("Eaten by beasts. \n\n Game over")
        elif door == "red":
            print("Burned by fire. \n\n Game over")
        elif door == "yellow":
            print("You win!")
        else:
            print("Game over")
    else:
        print("Attacked by trout. \n\n Game over")
else:
    print("Fall into a holde. \n\n Game over")
