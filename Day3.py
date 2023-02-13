from time import sleep

print("Tresure Island Maze!\n")

dir = input("You are at an adjacent island! Select left or right (L/R)").lower()
if dir == 'l' or dir == 'r' or dir == 'left' or dir == 'right':
    if dir== 'l' or dir == 'left':
        print("You are at a lake!")
        choice = input("Would you wait for a boat or swim across the lake? (wait/swim)").lower()
        if choice== 'wait' or choice == 'w':
            print("Hop on the boat")
            sleep(2)
            col = input("You have arrived at the treasure island!\n Pick a color between red, yellow and blue (r/y/b)").lower()
            if col == 'r' or col == 'red':
                print("Ah!!! You perished in Fire!!\n Game Over")
            elif col == 'b' or col == 'blue':
                print("CONGRATULATIONS! The treasure is all yours!")
            elif col == 'y' or col== 'yellow':
                print("Oh no!! You fell into a Hole! \n Game Over")
            else:
                print("You made an invalid Choice, you are bear's breakfast Now! \n Game Over")
        elif choice == 'swim' or choice== 's':
            print("You start swimming and..")
            sleep(1)
            print("Oh no! Crocodiles in the Water! \n Game Over")
        else:
            print("Invalid Input, A bolder falls on you! \n Game Over")
    elif dir == 'right' or dir == 'r':
        print("You fell in a ditch!\n Lesson of the Day: \n Not all right choices are Right xD")
else:
    print("Invalid input! \n Game Over!")



