"""
Author: Shaun Ratcliff
File Name: student_gpa_checker.py
Description: This program will accept a student names and GPAs and tests if the student has made the Dean's List or the Honor Roll.


"""

def check_student_gpa():
    while True:
        # Ask for student's last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        
        # Quit processing  the student records if the last name entered is 'ZZZ'
        if last_name == 'ZZZ':
            break
        
        # Ask for student's first name
        first_name = input("Enter the student's first name: ")
        
        # Ask for the student's GPA as a float
        gpa = float(input("Enter the student's GPA: "))
        
        # Test if the student's GPA is 3.5 or greater print a message saying that the student has made the Dean's List
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        # Test if the student's GPA is 3.25 or greater print a message saying that the student has made the Honor Roll
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")
check_student_gpa()