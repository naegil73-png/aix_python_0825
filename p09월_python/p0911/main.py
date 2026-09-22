from stuFunc import *
readStu()

while True:
    choice = main_screen()

    if choice == 1:
        s_input()

    elif choice == 2:
        s_output()

    elif choice == 3:
        s_update()

    elif choice == 9:
        writeStu()
        
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break