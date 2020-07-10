import os
import sys


class Courses:

    def mern_stack(self):
        print("""
        
        ##########  MERN Stack  ##########
        
        MERN Stack is a Javascript Stack that is used for easier and faster deployment of full-stack web 
        applications. MERN Stack comprises of 4 technologies namely: MongoDB, Express, React and Node.js. It is 
        designed to make the development process smoother and easier. 

        Each of these 4 powerful technologies provides an end-to-end framework for the developers to work in and each 
        of these technologies play a big part in the development of web applications. 
        """)

        print("\n\n\t\t\tPress any key to exit ...\n\n\n\n\n")
        back = input()
        if back:
            return
        os.system('cls')

    def full_stack_django(self):
        print("""

                ##########  Django(Python) Stack  ##########

                Django is a widely-used Python web application framework with a "batteries-included" philosophy. The 
                principle behind batteries-included is that the common functionality for building web applications 
                should come with the framework instead of as separate libraries
              """)

        print("\n\n\t\t\tPress any key to exit ...\n\n\n\n\n")
        back = input()
        if back:
            return
        os.system('cls')


    def available_courses(self):
        print("""
        
        
        ##########  Available Courses  ##########
        
        -> Every courses on IT Academy costs rs. 20,000
        -> Student can involve on any course either by full payment on beginning or payment with two installments of rs. 10,000 each.
        -> Total cost would be 22,000 including 2,000 deposit which is refundable and is returned after the course completion.
        
        -> All available courses:
        
        1. MERN Stack
        2. Full Stack with Django(Python)
        3. Full Stack with HTML5 CSS3 PHP & MYSQL
        
        4. Exit...
        
        --------------------------------------------------------
        Press 4 to exit ...
        Press the respective menu number for course description ...
        """)
        courseChoice = int(input("\t\t\tEnter Course Number: "))
        if courseChoice == 1:
            os.system('cls')
            Courses.mern_stack(self)
        elif courseChoice == 2:
            os.system('cls')
            Courses.full_stack_django(self)
        elif courseChoice == 3:
            print("Display Records")
        elif courseChoice == 4:
            return
        else:
            print("\t\t\tWrong choice !!!\n\t\t\tEnter only 1/2/3/4")


class Menu:
    def menu_panel(self):
        choice = 0
        while choice != 6:
            print("""
            ##################################
            ########    IT ACADEMY    ########
            ##################################            
    
                ----  Main Menu  ----
    
            1. Available Courses.
            2. Register Student.
            3. Display Student Records.
            4. Update Records.
            5. Delete Records.
            6. Exit.
    
            --------------------------------------------------------
            Press the respective menu number for respective operation ...
            """)
            choice = int(input("\t\t\tEnter Your Choice: "))

            if choice == 1:
                os.system('cls')
                Courses.available_courses(self)
            elif choice == 2:
                print("Register Students")
            elif choice == 3:
                print("Display Records")
            elif choice == 4:
                print("Update Records")
            elif choice == 5:
                print("Delete Records")
            elif choice == 6:
                sys.exit()
            else:
                print("\t\t\tWrong choice !!!\n\t\t\tEnter only 1/2/3/4/5/6")


m = Menu()
m.menu_panel()
