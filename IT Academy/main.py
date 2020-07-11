import os
import sys
import pickle


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

    def full_stack_php(self):
        print("""

                ##########  Full Stack(PHP)  ##########

                This course will give you the following Skills:

                Front End Web Development:
                    HTML.
                    CSS.
                    JAVASCRIPT.
                    BOOTSTRAP.
                
                Back End Web Development:
                    PHP.
                    MYSQL.
                    WORDPRESS.
                    PHP OOP.
                
                BASICS:
                    WEB BASICS.
                    INTRODUCTION TO XML.
                    COMPLETE UNDERSTANDING OF JSON.
                    INTRODUCTION TO REST AND API.                
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
            os.system('cls')
            Courses.full_stack_php(self)
        elif courseChoice == 4:
            os.system("cls")
            return
        else:
            print("\t\t\tWrong choice !!!\n\t\t\tEnter only 1/2/3/4")


class Student:
    def register_student(self):
        list = []
        print("""
        #################### Register Student ####################
        
        Enter the details as per the headings...
        """)

        regNo = int(input("Registration Number: "))

        while regNo < 1:
            print("\t\n\nInvalid Registration Number !!! ")
            print('\tRegistration Number should be greater than "0" !!!')
            print("\tTry Again !!!")
            print("\n\n")
            regNo = int(input("Registration Number: "))

        try:
            file = open("student.dat", "rb")
            regNoList = pickle.load(file)
            file.close()
        except FileNotFoundError:
            name = input("Name: ")
            print("""
                    Courses:
                        1. MERN Stack
                        2. Full Stack with Django(Python)
                        3. Full Stack with HTML5 CSS3 PHP & MYSQL 
                    """)
            choice = int(input("Enter Course no. : "))
            while choice != 1 and choice != 2 and choice != 3:
                print("Invalid Course Number !!! Try Again")
                choice = int(input("Enter Course no. : "))

            if choice == 1:
                course = 'MERN Stack'
            elif choice == 2:
                course = 'MERN Stack'
            elif choice == 3:
                course = 'MERN Stack'

            print("""
                Payment Type:
                    1. Full Payment
                    2. Pay in two installments
                
                Note: Rs 2000 should be paid as deposit which is refundable !!!
                """)
            choice = int(input("Enter Payment Type no. : "))
            while choice != 1 and choice != 2:
                print("Invalid Payment Type !!! Try Again")
                choice = int(input("Enter Payment Type no. : "))

            if choice == 1:
                Totalpayment = 22000
            elif choice == 2:
                Totalpayment = 12000

            student = {"regNo": regNo, "name": name, "course": course, "payment": Totalpayment}
            list.append(student)
            file = open("student.dat", "ab+")
            pickle.dump(list, file)
            file.close()
            print("\n\n\t\tRecord Added Successfully !!!")
            print("\n\n\t\t\tPress any key to exit ...\n\n\n\n\n")
            back = input()
            if back:
                return
            os.system('cls')
        else:
            # check if register number already exists
            for x in regNoList:
                if regNo == x['regNo']:
                    found = True
                else:
                    found = False

            while found == True:
                print(f"Registration Number {regNo} already exists ...")
                print("Try again with different number !!!")
                regNo = int(input("Registration Number: "))

                while regNo < 1:
                    print("\t\n\nInvalid Registration Number !!! ")
                    print('\tRegistration Number should be greater than "0" !!!')
                    print("\tTry Again !!!")
                    print("\n\n")
                    regNo = int(input("Registration Number: "))

                    for x in regNoList:
                        if regNo == x['regNo']:
                            found = True
                        else:
                            found = False

            name = input("Name: ")
            print("""
            Courses:
                1. MERN Stack
                2. Full Stack with Django(Python)
                3. Full Stack with HTML5 CSS3 PHP & MYSQL 
            """)
            choice = int(input("Enter Course no. : "))
            while choice == 1 and choice == 2 and choice == 3:
                print("Invalid Course Number !!! Try Again")
                choice = int(input("Enter Course no. : "))

            if choice == 1:
                course = 'MERN Stack'
            elif choice == 2:
                course = 'MERN Stack'
            elif choice == 3:
                course = 'MERN Stack'

            print("""
                Payment Type:
                    1. Full Payment
                    2. Pay in two installments

                Note: Rs 2000 should be paid as deposit which is refundable !!!
                """)
            choice = int(input("Enter Payment Type no. : "))
            while choice != 1 and choice != 2:
                print("Invalid Payment Type !!! Try Again")
                choice = int(input("Enter Payment Type no. : "))

            if choice == 1:
                Totalpayment = 22000
            elif choice == 2:
                Totalpayment = 12000

            student = {"regNo": regNo, "name": name, "course": course, "payment": Totalpayment}
            list.append(student)
            file = open("student.dat", "ab+")
            pickle.dump(list, file)
            file.close()
            print("\n\n\t\tRecord Added Successfully !!!")
            print("\n\n\t\t\tPress any key to exit ...\n\n\n\n\n")
            back = input()
            if back:
                return
            os.system('cls')

    def update(self):
        regNo = input('Enter Registration Number to update :')

        file = open("student.dat", "rb+")
        list = pickle.load(file)

        found = 0
        lst = []
        for x in list:
            if regNo == x['regNo']:
                found = 1
                x['name'] = input('Enter new name ')
                print("""
                            Courses:
                                1. MERN Stack
                                2. Full Stack with Django(Python)
                                3. Full Stack with HTML5 CSS3 PHP & MYSQL 
                            """)
                choice = int(input("Enter Course no. : "))
                while choice == 1 and choice == 2 and choice == 3:
                    print("Invalid Course Number !!! Try Again")
                    choice = int(input("Enter Course no. : "))

                if choice == 1:
                    x['course'] = 'MERN Stack'
                elif choice == 2:
                    x['course'] = 'MERN Stack'
                elif choice == 3:
                    x['course'] = 'MERN Stack'

                print("""
                                Payment Type:
                                    1. Full Payment
                                    2. Pay in two installments

                                Note: Rs 2000 should be paid as deposit which is refundable !!!
                                """)
                choice = int(input("Enter Payment Type no. : "))
                while choice != 1 and choice != 2:
                    print("Invalid Payment Type !!! Try Again")
                    choice = int(input("Enter Payment Type no. : "))

                if choice == 1:
                    x['payment'] = 22000
                elif choice == 2:
                    x['payment'] = 12000
            lst.append(x)

        if found == 1:
            file.seek(0)
            pickle.dump(lst, file)
            print("Record Updated")
        else:
            print('No Record Found !!!')

    def delete(self):
        regNo = input('Enter Registration Number to DELETE : ')

        file = open("student.dat", "rb+")
        list = pickle.load(file)

        found = 0
        lst = []
        for x in list:
            if regNo != x['name']:
                lst.append(x)
            else:
                found = 1

        if found == 1:
            file.seek(0)
            pickle.dump(lst, file)
            print("Record Deleted ")
        else:
            print('Record not found !!!')

    def display(self):
        try:
            file = open("student.dat", "rb")
            regNoList = pickle.load(file)
            file.close()
        except FileNotFoundError:
            print("No Records Found !!!")
        else:
            # for x in regNoList:
            #     print(f"Registration Number: {regNoList[x][0]}")
            #     print(f"Name               : {regNoList[x][1]}")
            #     print(f"Payment            : {regNoList[x][2]}")

            for i in regNoList:
                print(regNoList[i])


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
                os.system('cls')
                Student.register_student(self)
            elif choice == 3:
                Student.display(self)
            elif choice == 4:
                Student.update(self)
            elif choice == 5:
                Student.delete(self)
            elif choice == 6:
                sys.exit()
            else:
                print("\t\t\tWrong choice !!!\n\t\t\tEnter only 1/2/3/4/5/6")


m = Menu()
m.menu_panel()
