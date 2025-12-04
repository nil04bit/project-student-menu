
from random import randint
from os import system
from datetime import time
from time import sleep

students = [
    [1, "ali", "rezayi", "22", "Male", "0021547485", "2154621", "B", 75, 85, 55, "Deactive"],
    [2, "sara", "marami", "30", "Female", "0021854765", "1524102", "A", 75, 95, 65.5, "Active"],
    [3, "milad", "amiri", "28", "Male", "0021858787", "1844102", "A", 40, 62, 80, "Active"],
    [4, "mina", "baqeri", "25", "Female", "0021800765", "4104102", "B", 33, 56, 100, "Active"]
            ]

# region start game
while True:
    # region show menu
    system("cls")
    menu = input("\nMenu:\n1.[A]dd\n2.[S]how\n3.[R]emove\n4.[E]dit\n5.[Se]arch\n6.[Re]port\n7.[Q]uit\nplease choose an option: ")
    system("cls")
    if menu == "":
        print("no entry. please try again.")
    elif menu not in ("A", "S", "R", "E", "Re", "Q", "1", "2", "3", "4", "5", "6", "7"):
        print("wrong entry. please try again.")
    else:
        # region add item
        match menu:
            case "1" | "A":
                system("cls")
                while True:
                    if input("do you want to add a student?\t[yes]\t[no]\t") != "yes":
                        break
                    else:
                        system("cls")
                        # region get first name
                        while True:
                            first_name = input("please enter your first name: ")
                            system("cls")
                            if first_name == "":
                                print("no entry. please try again.")
                            else:
                                # region get last name
                                while True:
                                    last_name = input("please enter your last name: ")
                                    system("cls")
                                    if last_name == "":
                                        print("no entry. please try again.")
                                    else:
                                        code = randint(0, len(students)+ 1)
                                        for student in students:
                                            if student[0] == code:
                                                code = randint(0, len(students) + 1)
                                    break
                                break
                                # endregion
                        # endregion 
                        
                        # region get age
                        while True:
                            age = input("please enter your age: ")
                            system("cls")
                            if age == "":
                                print("no entry please try again.")
                            elif 0 < int(age) < 18:
                                print("not old enough. please try again.")
                            elif int(age) < 0:
                                print("invalid number. please try again.")
                            else:
                                break
                        # endregion
                        
                        # region get gender    
                        while True:
                            gender = input("please choose your gender:\n[F]emale\t[M]ale\t")
                            system("cls")
                            match gender:
                                case "":
                                    print("no entry. please try again.")
                                case "F":
                                    gender = "Female"
                                    break
                                case "M":
                                    gender = "Male"
                                    break
                                case _:
                                    print("invalid input. please try again.")
                        # endregion
                        
                        # region get national code
                        while True:
                            national_code = input("please enter your national code: ")
                            system("cls")
                            for student in students:
                                for i in student:
                                    if student[5] == national_code:
                                        print("national code duplicated. please try again.")
                                break
                            if national_code == "":
                                print("no entry. please try again.")
                            elif len(national_code) != 10:
                                print("wrong entry. please try again.")
                            else:
                                break

                            
                        # endregion
                        
                        # region get student code
                        while True:
                            student_code = input("please enter your student number: ")
                            system("cls")
                            for student in students:
                                for i in student:
                                    if student[6] == student_code:
                                        print("student code duplicated. please try again.")
                                break
                            
                            if student_code == "":
                                print("no entry. please try again.")
                            elif len(student_code) < 7:
                                print("wrong entry. please try again.")
                            else:
                                break

                            
                        # endregion

                        # region get class
                        while True:
                            class_number = input("please choose your class:\n[A]\t[B]\t[C]\t")
                            system("cls")
                            if class_number == "":
                                print("no entry. please try again.")
                            elif class_number not in ("A", "B", "C"):
                                print("wrong entry. please try again.")
                            else:
                                break
                        # endregion
                        
                        # region get php score
                        while True:
                            php_score = input("please enter your php score: ")
                            system("cls")
                            if php_score == "":
                                print("no entry. please try again")
                            elif float(php_score) > 100 or float(php_score) < 0:
                                print("wrong entry. please try again.")
                            else:
                                php_score = float(php_score)
                                break
                        # endregion

                        # region get python score
                        while True:
                            python_score = input("please enter your python score: ")
                            system("cls")
                            if python_score == "":
                                print("no entry. please try again")
                            elif float(python_score) > 100 or float(python_score) < 0:
                                print("wrong entry. please try again.")
                            else:
                                python_score = float(python_score)
                                break
                        # endregion
                        
                        # region get js score
                        while True:
                            js_score = input("please enter your js score: ")
                            system("cls")
                            if js_score == "":
                                print("no entry. please try again")
                            elif float(js_score) > 100 or float(js_score) < 0:
                                print("wrong entry. please try again.")
                            else:
                                js_score = float(js_score)
                                break
                        # end region
                        
                        # region get status
                        while True:
                            status = input("please choose your status:\n[A]ctive\t[D]eactive\t")
                            system("cls")
                            match status:
                                case "":
                                    print("no entry. please try again.")
                                case "A":
                                    status = "Active"
                                    break
                                case "D":
                                    status = "Deactive"
                                    break
                                case _:
                                    print("wrong entry. please try again.")
                        # endregion

                        student = [code, first_name, last_name, age, gender, national_code, student_code,
                                class_number, php_score, python_score, js_score, status]
                        students.append(student)
                        system("cls")
                        print("student added.")
        # endregion   
    # endregion

            # region show items
            case "2" | "S":
                flag = True
                show_correct = True
                while flag:
                    if len(students) == 0:
                        system("cls")
                        print("student list is empty.")
                        break
                    else:
                        system("cls")
                        # region ask to show
                        while show_correct:
                            column_names = None
                            column_indexes = None
                            show_options = input("please choose an option:\n1.[S]how all\n2.[Se]arch one\n3.[Q]uit: ")
                            match show_options:
                                case "3" | "Q":
                                    flag = False
                                    show_correct = False
                                    break
                                
                                # region show all
                                case "1" | "S":
                                    column_names = ["Code", "Name", "Family", "Age", "Gender", "National code", "Student code", "Class", "Php sc", "Python sc", "Js sc", "Status"]
                                    column_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                                # endregion
                                
                                # region choose item to show   
                                case "2" | "Se":
                                    system("cls")
                                    column_names = []
                                    column_indexes = [0]
                                    # region show selected items
                                    while True:
                                        selected_columns = input("please choose an item:\n1.[N]ame\n2.[F]amily\n3.[A]ge\n4.[G]ender\n5.[Na]tional code\n6.[St]udent code\n7.[C]lass\n8.[P]hp score\n9.[Py]thon score\n10.[J]ava score\n11.[S]tatus\n12.[E]nd\t")
                                        system("cls")
                                        if selected_columns == "":
                                            print("no entry. please try again.")
                                        elif selected_columns in ["12", "E"]:
                                            break
                                        elif selected_columns in ["1", "N"] and "Name" not in column_names:
                                            column_names.append("Name")
                                            column_indexes.append(1)
                                            
                                        elif selected_columns in ["2", "F"] and "Family" not in column_names:
                                            column_names.append("Family")
                                            column_indexes.append(2)
                                            
                                        elif selected_columns in ["3", "A"] and "Age" not in column_names:
                                            column_names.append("Age")
                                            column_indexes.append(3)
                                            
                                        elif selected_columns in ["4", "G"] and "Gender" not in column_names:
                                            column_names.append("Gender")
                                            column_indexes.append(4)

                                        elif selected_columns in ["5", "Na"] and "National code" not in column_names:
                                            column_names.append("National code")
                                            column_indexes.append(5)

                                        elif selected_columns in ["6", "St"] and "Student code" not in column_names:
                                            column_names.append("Student code")
                                            column_indexes.append(6)

                                        elif selected_columns in ["7", "C"] and "Class" not in column_names:
                                            column_names.append("Class")
                                            column_indexes.append(7)

                                        elif selected_columns in ["8", "Php"] and "Php sc" not in column_names:
                                            column_names.append("Php sc")
                                            column_indexes.append(8)

                                        elif selected_columns in ["9", "Py"] and "Python sc" not in column_names:
                                            column_names.append("Python sc")
                                            column_indexes.append(9)

                                        elif selected_columns in ["10", "J"] and "Js sc" not in column_names:
                                            column_names.append("Js sc")
                                            column_indexes.append(10)

                                        elif selected_columns in ["11", "S"] and "Status" not in column_names:
                                            column_names.append("Status")
                                            column_indexes.append(11)

                                        else:
                                            print("invalid option. please Try again.\n")

                                        if column_names:
                                            print("selected items:", *column_names)
                                    # endregion
                                # endregion
                                case _:
                                    print("wrong entry. please try again.")
                                    break
                                
                            print("Row", "Code", *column_names, sep="\t")
                            print(
                                "----------------------------------------------------------------------------------------------------------------------------------------------------------")
                            for row, student in enumerate(students):
                                print(row + 1, end="\t")
                                for item in column_indexes:
                                    print(student[item], end="\t")
                                print()
                            print(
                                "----------------------------------------------------------------------------------------------------------------------------------------------------------")
                            sleep(3)
                                
                        # endregion
                # endregion
            
            # region remove item
            case "3" | "R":
                system("cls")
                option = None
                if len(students) == 0:
                    print("student list is empty.")
                else:
                    # region ask to remove
                    while True:
                        if input("do you want to remove a student?[yes]\t[no]\t") != "yes":
                            break
                        else:
                            system("cls")
                            # region get search item to remove
                            while True:
                                options = input("please choose the option you want to search with:\n1.[C]ode\n2.[N]ational code\n3.[S]tudent code\n4.[Q]uit: ")
                                if options == "":
                                    system("cls")
                                    print("no entry. please try again.\n")
                                    
                                elif options in ("4", "Q"):
                                    break

                                elif options not in ("1", "C", "2", "N", "3", "S"):
                                    system("cls")
                                    print("wrong entry. please try again.\n")

                                else:
                                    system("cls")
                                    remove = None
                                    # region check the item and remove
                                    match options:
                                        case "1" | "C":
                                            # region show options
                                            while True:
                                                column_names = ["Code", "Name", "Family", "Age", "Gender", "National code", "Student code", "Class", "Php sc", "Python sc", "Js sc", "Status"]
                                                column_indexes = list(range(0, 12))
                                                print("Row", *column_names, sep="\t")
                                                print(
                                                    "----------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                if students == []:
                                                        print("the list is empty.")
                                                        print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        break
                                                        
                                                for row, student in enumerate(students):
                                                    print(row + 1, end="\t")
                                                    for item in column_indexes:
                                                        print(student[item], end="\t")
                                                    print()
                                                print(
                                                    "----------------------------------------------------------------------------------------------------------------------------------------------------------")
                                            # endregion
                                            
                                                remove = input("please enter the code: ")
                                                system("cls")
                                                
                                                codes = []
                                                for student in students:
                                                    codes.append(student[0])
                                                    
                                                if remove == "":
                                                    system("cls")
                                                    print("no entry. please try again.\n")
                                                elif int(remove) not in codes:
                                                    system("cls")
                                                    print("This code does not exist. please try again.\n")
                                                else: 
                                                    option = 0
                                                    remove = int(remove)
                                                    break
                                        
                                        case "2" | "N":
                                            while True:
                                                column_names = ["Code", "Name", "Family", "Age", "Gender", "National code", "Student code", "Class", "Php sc", "Python sc", "Js sc", "Status"]
                                                column_indexes = list(range(0, 12))
                                                print("Row", *column_names, sep="\t")
                                                print(
                                                    "----------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                
                                                if students == []:
                                                        print("the list is empty.")
                                                        print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        break
                                                    
                                                for row, student in enumerate(students):
                                                    print(row + 1, end="\t")
                                                    for item in column_indexes:
                                                        print(student[item], end="\t")
                                                    print()
                                                    
                                                remove = input("please enter the national code: ")
                                                system("cls")
                                                if remove == "":
                                                    system("cls")
                                                    print("no entry. please try again.\n")
                                                elif len(remove) != 10:
                                                    system("cls")
                                                    print("wrong entry. please try again.\n")
                                                else:
                                                    option = 5
                                                    break
                                        
                                        case "3" | "S":
                                            while True:
                                                column_names = ["Code", "Name", "Family", "Age", "Gender", "National code", "Student code", "Class", "Php sc", "Python sc", "Js sc", "Status"]
                                                column_indexes = list(range(0, 12))
                                                print("Row", *column_names, sep="\t")
                                                print(
                                                    "----------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                
                                                if students == []:
                                                        print("the list is empty.")
                                                        print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        break
                                                    
                                                for row, student in enumerate(students):
                                                    print(row + 1, end="\t")
                                                    for item in column_indexes:
                                                        print(student[item], end="\t")
                                                    print()
                                                    
                                                remove = input("please enter the student number: ")
                                                system("cls")
                                                if remove == "":
                                                    system("cls")
                                                    print("no entry. please try again.\n")
                                                elif len(remove) != 7:
                                                    system("cls")
                                                    print("wrong entry, please try again.\n")
                                                else:
                                                    option = 6
                                                    break
                                        case _:
                                            break
                                        
                                
                                    if remove:
                                        remove_found = False
                                        if input("do you really want to remove this contact?[yes]\t[no]\t") == "yes":
                                            for student in students:
                                                if student[option] == remove:
                                                    students.remove(student)
                                                    sleep(2)
                                                    print("student deleted.")
                                                    remove_found = True
                                            if not remove_found:
                                                print("can't find a student with this data. please try again.\n")
                                            break
                                        else:
                                            break
                                    # endregion
                            # endregion
                    # endregion
            # endregion    
        
            # region edit item
            case "4" | "E":
                # region ask to edit or not
                while True:
                    if input("do you want to edit an item?\t[yes]\t[no]\t") != "yes":
                        break
                    else:
                        system("cls")
                        # region checking for empty list
                        for student in students:
                            if student:
                                empty = False
                            else:
                                print("list is empty. please try again.")
                                empty = True
                        # endregion
                        
                        # region checking for empty entry
                        while not empty:
                            column_names = ["Code", "Name", "Family", "Age", "Gender", "National code", "Student code", "Class", "Php sc", "Python sc", "Js sc", "Status"]
                            column_indexes = list(range(0, 12))
                            print("Row", *column_names, sep="\t")
                            print(
                                "----------------------------------------------------------------------------------------------------------------------------------------------------------")
                            for row, student in enumerate(students):
                                print(row + 1, end="\t")
                                for item in column_indexes:
                                    print(student[item], end="\t")
                                print()
                            nc_check = input("please enter the student's national code: ")
                            system("cls")
                            if nc_check == "":
                                print("no entry. please try again.\n")
                            elif len(nc_check) != 10:
                                print("wrong entry. please try again.\n")
                            else:
                                break
                        # endregion
                        
                        # region edit the item in the list
                        if nc_check:
                            st_number = 0
                            nc_not_exist = 0
                            # region check existance of national code
                            for student in students:
                                st_number += 1
                                if student[5] != nc_check:
                                    nc_not_exist += 1
                                
                            if nc_not_exist == st_number:
                                print("This national code does not exist. please try again.\n")
                                break
                            # endregion
                            
                            # region ask for edit option
                            flag = True
                            while flag:
                                column_names = ["Code", "Name", "Family", "Age", "Gender", "National code", "Student code", "Class", "Php sc", "Python sc", "Js sc", "Status"]
                                column_indexes = list(range(0, 12))
                                print("Row", *column_names, sep="\t")
                                print(
                                    "----------------------------------------------------------------------------------------------------------------------------------------------------------")
                                for student in students:
                                    if student[5] == nc_check:
                                        print(*student, sep="\t")
                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
                                selected_column = input("\nplease choose the item you want to edit:\n1.[N]ame\n2.[F]amily\n3.[A]ge\n4.[G]ender\n5.[Na]tional code\n6.[St]udent code\n7.[C]lass\n8.[P]hp score\n9.[Py]thon score\n10.[J]s score\n11.[S]tatus\n12.[E]nd\t")
                                system("cls")
                                
                                match selected_column:
                                    case "":
                                        print("no entry. please try again.")
                                        
                                    case "12" | "E":
                                        break

                                    case "1" | "N":
                                        while True:
                                            new_firstname = input("please enter your first name: ")
                                            system("cls")
                                            if new_firstname == "":
                                                print("no entry. please try again.")
                                            else:
                                                for student in students:
                                                    if student[5] == nc_check:
                                                        student[1] = new_firstname
                                                        print("Done")
                                                        flag = False
                                                break

                                    case "2" | "F":
                                        while True:
                                            new_lastname = input("please enter your last name: ")
                                            system("cls")
                                            if new_lastname == "":
                                                print("no entry. please try again.")
                                            else:
                                                for student in students:
                                                    if student[5] == nc_check:
                                                        student[2] = new_lastname
                                                        print("Done")
                                                        flag = False
                                                break

                                    case"3" | "A":
                                        while True:
                                            new_age = input("please enter your age: ")
                                            system("cls")
                                            if new_age == "":
                                                print("no entry please try again.")
                                            elif 0 < int(new_age) < 18:
                                                print("not old enough. please try again.")
                                            elif int(new_age) < 0:
                                                print("invalid number. please try again.")
                                            else:
                                                for student in students:
                                                    if student[5] == nc_check:
                                                        student[3] = new_age
                                                        print("Done")
                                                        flag = False
                                                break

                                    case "4" | "G":
                                        while True:
                                            new_gender = input("please choose your gender:\n[F]emale\t[M]ale: ")
                                            system("cls")
                                            if new_gender == "":
                                                print("no entry. please try again.")
                                            elif new_gender not in ("F", "M"):
                                                print("invalid input. please try again.")
                                            else:
                                                if new_gender == "F":
                                                    new_gender = "Female"
                                                else:
                                                    new_gender = "Male"
                                                    
                                                for student in students:
                                                    if student[5] == nc_check:
                                                        student[4] = new_gender
                                                        print("Done")
                                                        flag = False
                                                break


                                    case "5" | "Na":
                                        while True:
                                            new_nationalcode = input("please enter your national code: ")
                                            system("cls")
                                            if new_nationalcode == "":
                                                print("no entry. please try again.")
                                            elif len(new_nationalcode) != 10:
                                                print("wrong entry. please try again.")
                                            else:
                                                for student in students:
                                                    if student[5] == nc_check:
                                                        student[5] = new_nationalcode
                                                        print("Done")
                                                        flag = False
                                                break

                                    case "6" | "St":
                                        while True:
                                            new_studentcode = input("please enter your student number: ")
                                            system("cls")
                                            if new_studentcode == "":
                                                print("no entry. please try again.")
                                            elif len(new_studentcode) < 7:
                                                print("wrong entry. please try again.")
                                            else:
                                                for student in students:
                                                    if student[5] == nc_check:
                                                        student[6] = new_studentcode
                                                        print("Done")
                                                        flag = False
                                                break

                                    case "7" | "C":
                                        while True:
                                            new_class = input("please choose your class:\n[A]\t[B]\t[C]\t")
                                            system("cls")
                                            if new_class == "":
                                                print("no entry. please try again.")
                                            elif new_class not in ("A", "B", "C"):
                                                print("wrong entry. please try again.")
                                            else:
                                                for student in students:
                                                    if student[5] == nc_check:
                                                        student[7] = new_class
                                                        print("Done")
                                                        flag = False
                                                break

                                    case "8" | "Php":
                                        while True:
                                            new_phpscore = input("please enter your php score: ")
                                            system("cls")
                                            if new_phpscore == "":
                                                print("no entry. please try again")
                                            else:
                                                new_phpscore = float(new_phpscore)
                                                if new_phpscore > 100 and new_phpscore < 0:
                                                    print("wrong entry. please try again.")
                                                else:
                                                    for student in students:
                                                        if student[5] == nc_check:
                                                            student[8] = new_phpscore
                                                            print("Done")
                                                            flag = False
                                                    break
                                                
                                    case "9" | "Py":
                                        while True:
                                            new_pythonscore = input("please enter your python score: ")
                                            system("cls")
                                            if new_pythonscore == "":
                                                print("no entry. please try again")
                                            else:
                                                new_pythonscore = float(new_pythonscore)
                                                if new_pythonscore > 100 and new_pythonscore < 0:
                                                    print("wrong entry. please try again.")
                                                else:
                                                    for student in students:
                                                        if student[5] == nc_check:
                                                            student[9] = new_pythonscore
                                                            print("Done")
                                                            flag = False
                                                    break

                                    case "10" | "J":
                                        while True:
                                            new_jsscore = input("please enter your js score: ")
                                            system("cls")
                                            if new_jsscore == "":
                                                print("no entry. please try again")
                                            else:
                                                new_jsscore = float(new_jsscore)
                                                if new_jsscore > 100 and new_jsscore < 0:
                                                    print("wrong entry. please try again.")
                                                else:
                                                    for student in students:
                                                        if student[5] == nc_check:
                                                            student[10] = new_jsscore
                                                            print("Done")
                                                            flag = False
                                                    break
                                    
                                    case "11" | "S":
                                        while True:
                                            new_status = input("please choose your status:\n[A]ctive\t[D]eactive: ")
                                            system("cls")
                                            if new_status == "":
                                                print("no entry. please try again.")
                                            elif new_status not in ("A", "D"):
                                                print("invalid input. please try again.")
                                            else:
                                                if new_status == "A":
                                                    new_status = "Active"
                                                elif new_status == "D":
                                                    new_status = "deactive"
                                                    
                                                for student in students:
                                                    if student[5] == nc_check:
                                                        student[11] = new_status
                                                        print("Done")
                                                        flag = False
                                                break

                                    case _:
                                        print("invalid option. please Try again.")
                            # endregion
                        # endregion
                # endregion
            # endregion
            
            # region search item
            case "5" | "Se":
                system("cls")
                # region ask to search or not
                while True:
                    if input("do you want to search a student?\t[yes]\t[no]\t") != "yes":
                        break
                    else:
                        system("cls")
                        # region get search item
                        continue_ = True
                        while continue_:
                            found = []
                            selected_false = False
                            selected_column = input("\nplease choose the item you want to search with:\n1.[N]ame\n2.[F]amily\n3.[A]ge\n4.[G]ender\n5.[Na]tional code\n6.[St]udent code\n7.[C]lass\n8.[P]hp score\n9.[Py]thon score\n10.[J]s score\n11.[S]tatus\n12.[E]nd\t")
                            system("cls")
                            
                            # region search item
                            match selected_column:
                                case "":
                                    print("empty entry. please try again.")
                                    selected_false = True
                                    
                                case "12" | "E":
                                    continue_ = False
                                    selected_false = True

                                case "1" | "N":
                                    while True:
                                        firstname = input("please enter your first name: ")
                                        system("cls")
                                        if firstname == "":
                                            print("no entry. please try again.")
                                        else:
                                            for student in students:
                                                if student[1] == firstname:
                                                    found.extend([student])
                                                    continue_ = False
                                            break

                                case "2" | "F":
                                    while True:
                                        lastname = input("please enter your last name: ")
                                        system("cls")
                                        if lastname == "":
                                            print("no entry. please try again.")
                                        else:
                                            for student in students:
                                                if student[2] == lastname:
                                                    found.extend([student])
                                                    continue_ = False
                                            break

                                case"3" | "A":
                                    while True:
                                        age = input("please enter your age: ")
                                        system("cls")
                                        if age == "":
                                            print("no entry please try again.")
                                        elif 0 < int(age) < 18:
                                            print("not old enough. please try again.")
                                        elif int(age) < 0:
                                            print("invalid number. please try again.")
                                        else:
                                            for student in students:
                                                if student[3] == age:
                                                    found.extend([student])
                                                    continue_ = False
                                            break

                                case "4" | "G":
                                    while True:
                                        gender = input("please choose your gender:\n[F]emale\t[M]ale: ")
                                        system("cls")
                                        if gender == "":
                                            print("no entry. please try again.")
                                        elif gender not in ("F", "M"):
                                            print("invalid input. please try again.")
                                        else:
                                            if gender == "F":
                                                gender = "Female"
                                            else:
                                                gender = "Male"
                                                
                                            for student in students:
                                                if student[4] == gender:
                                                    found.extend([student])
                                                    continue_ = False
                                            break


                                case "5" | "Na":
                                    while True:
                                        nationalcode = input("please enter your national code: ")
                                        system("cls")
                                        if nationalcode == "":
                                            print("no entry. please try again.")
                                        elif len(nationalcode) != 10:
                                            print("wrong entry. please try again.")
                                        else:
                                            for student in students:
                                                if student[5] == nationalcode:
                                                    found.extend([student])
                                                    continue_ = False
                                            break

                                case "6" | "St":
                                    while True:
                                        studentcode = input("please enter your student number: ")
                                        system("cls")
                                        if studentcode == "":
                                            print("no entry. please try again.")
                                        elif len(studentcode) < 7:
                                            print("wrong entry. please try again.")
                                        else:
                                            for student in students:
                                                if student[6] == studentcode:
                                                    found.extend([student])
                                                    continue_ = False
                                            break

                                case "7" | "C":
                                    while True:
                                        class_ = input("please choose your class:\n[A]\t[B]\t[C]\t")
                                        system("cls")
                                        if class_ == "":
                                            print("no entry. please try again.")
                                        elif class_ not in ("A", "B", "C"):
                                            print("wrong entry. please try again.")
                                        else:
                                            for student in students:
                                                if student[7] == class_:
                                                    found.extend([student])
                                                    continue_ = False
                                            break

                                case "8" | "Php":
                                    while True:
                                        phpscore = input("please enter your php score: ")
                                        system("cls")
                                        if phpscore == "":
                                            print("no entry. please try again")
                                        else:
                                            phpscore = float(phpscore)
                                            if phpscore > 100 and phpscore < 0:
                                                print("wrong entry. please try again.")
                                            else:
                                                for student in students:
                                                    if student[8] == phpscore:
                                                        found.extend([student])
                                                        continue_ = False
                                                break
                                            
                                case "9" | "Py":
                                    while True:
                                        pythonscore = input("please enter your python score: ")
                                        system("cls")
                                        if pythonscore == "":
                                            print("no entry. please try again")
                                        else:
                                            pythonscore = float(pythonscore)
                                            if pythonscore > 100 and pythonscore < 0:
                                                print("wrong entry. please try again.")
                                            else:
                                                for student in students:
                                                    if student[9] == pythonscore:
                                                        found.extend([student])
                                                        continue_ = False
                                                break

                                case "10" | "J":
                                    while True:
                                        jsscore = input("please enter your js score: ")
                                        system("cls")
                                        if jsscore == "":
                                            print("no entry. please try again")
                                        else:
                                            jsscore = float(jsscore)
                                            if jsscore > 100 and jsscore < 0:
                                                print("wrong entry. please try again.")
                                            else:
                                                for student in students:
                                                    if student[10] == jsscore:
                                                        found.extend([student])
                                                        continue_ = False
                                                break
                                
                                case "11" | "S":
                                    while True:
                                        status = input("please choose your status:\n[A]ctive\t[D]eactive: ")
                                        system("cls")
                                        if status == "":
                                            print("no entry. please try again.")
                                        elif status not in ("A", "D"):
                                            print("invalid input. please try again.")
                                        else:
                                            if status == "A":
                                                status = "Active"
                                            else:
                                                status = "Deactive"
                                                
                                            for student in students:
                                                if student[11] == status:
                                                   found.extend([student])
                                                   continue_ = False
                                            break

                                case _:
                                    print("invalid option. please Try again.")
                                    selected_false = True
                                    
                            # endregion

                            # region show found list
                            if not selected_false:
                                if found != []:
                                    column_names = ["Code", "Name", "Family", "Age", "Gender", "National code", "Student code", "Class", "Php sc", "Python sc", "Js sc", "Status"]
                                    column_indexes = list(range(0, 12))
                                    print("Row", *column_names, sep="\t")
                                    print(
                                        "----------------------------------------------------------------------------------------------------------------------------------------------------------")
                                    for row, student in enumerate(found):
                                        print(row + 1, *student, sep="\t")
                                        print()
                                        
                                    sleep(2)
                                        
                                else:
                                    print("no student was found with this data. please try again.")
                                    break
                            
                            # endregion
                        # endregion
                # endregion
            # endregion

        
            # region report
            case "6" | "Re":
                # region ask to report or not
                while True:
                    shown = False
                    if input("do you want to take a report?\t[yes]\t[no]: ") == "yes":
                        while not shown:
                            # region choose the type
                            report_type = input("please choose the type you want report for:\n1.[C]lass\n2.[S]ubject\n3.[Q]uit: ")
                            match report_type:
                                case "":
                                    system("cls")
                                    print("no entry. please try again.")
                                    
                                case "3" | "Q":
                                    break
                                
                                # region report by class
                                case "1" | "C":
                                    counter = 0
                                    sum_ = 0
                                    min_ = float("inf")
                                    max_ = float("-inf")
                                    # region get class
                                    while True:
                                        class_ = input("please choose the class:\n1.[A]\n2.[B]\n3.[C]: ")
                                        if class_ == "":
                                            system("cls")
                                            print("no entry. please try again.")
                                        elif class_ not in ("1", "2", "3", "A", "B", "C"):
                                            system("cls")
                                            print("wrong entry. please try again.")
                                        else:
                                            found = False
                                            
                                            # region assign class name
                                            match class_:
                                                case "1":
                                                    class_ = "A"
                                                case "2":
                                                    class_ = "B"
                                                case "3":
                                                    class_ = "C"
                                            # endregion
                                                   
                                            for student in students:
                                                if student[7] == class_:
                                                    sum_ += student[8] + student[9] + student[10]
                                                    counter += 3
                                                    new_min = min(student[8], student[9], student[10])
                                                    new_max = max(student[8], student[9], student[10])
                                                    if new_min <= min_ :
                                                        min_ = new_min
                                                    if new_max >= max_:
                                                        max_ = new_max
                                                    
                                                    found = True
                                                    
                                            if not found:
                                                system("cls")
                                                print("no student found with this class. please try again.")
                                                
                                            if counter:
                                                system("cls")
                                                print("the average of class", class_, "is", sum_ / counter)
                                                print("the minimun score in class", class_, "is", min_)
                                                print("the maximum score in class", class_, "is", max_)
                                                print()
                                                shown = True
                                                sleep(3)
                                                
                                            break
                                    # endregion
                                # endregion
                                
                                # region report by subject    
                                case "2" | "S":
                                    counter = 0
                                    sum_ = 0
                                    min_ = float("inf")
                                    max_ = float("-inf")
                                    while True:
                                        subject = input("choose the subject:\n1.[P]hp\n2.[Py]thon\n3.[J]s: ")
                                        i = 0
                                        match subject:
                                            case "":
                                                system("cls")
                                                print("no entry. please try again.")
                                                
                                            case "1" | "P":
                                                i = 8
                                            
                                            case "2" | "Py":
                                                i = 9
                                            
                                            case "3" | "J":
                                                i = 10
                                                
                                            case _:
                                                system("cls")
                                                print("wrong entry. please try again.")
                                            
                                        if i:
                                            for student in students:
                                                    sum_ += student[i]
                                                    counter += 1
                                                    if student[i] <= min_:
                                                        min_ = student[i]
                                                    if student[i] >= max_:
                                                        max_ = student[i]
                                                        
                                            if counter:
                                                system("cls")
                                                                                                
                                                match subject:
                                                    case "1" | "P":
                                                        subject = "Php scores"
                                                    case "2" | "Py":
                                                        subject = "Python score"
                                                    case "3" | "J":
                                                        subject = "js score"
                                                    
                                                print("the average of", subject, "is", sum_ / counter)
                                                print("the minimum score in", subject, "is", min_)
                                                print("the maximum score in", subject, "is", max_)
                                                print()
                                                shown = True
                                                sleep(3)
                                            break
                                # endregion
                                
                                case _:
                                    system("cls")
                                    print("wrong entry. please try again.")
                            # endregion    
                    # endregion
                    else:
                        break
                # endregion
                
        
            # region quit
            case "7" | "Q":
                break
            # endregion
#endregion