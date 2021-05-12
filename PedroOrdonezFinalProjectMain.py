# INF 360 - Programming in Python
# Pedro Ordonez
# Assignment Final Project

# 20 points: Does the program execute with no errors

# 20 points: The program should contain: Good flow control, good use of functions,
    # code should be as clean as possible (i.e. writing the smallest amount
    # of code necessary to complete the function), and contain examples
    # of lists or dictionaries

# 20 points: The project should be well documented. Make use of block and line
    # comments to describe the program as a whole, individual functions,
    # and major areas of the project

# 20 points: Use of the logging module. This should be used in place of where you
    # might have had print statements (unless your project was intended to
    # have console output. Refer to Chapter 10 – Debugging. You should
    # import the module, setup the basic config, and then you must have a
    # combination of logging.debug and logging.critical statements used
    # appropriately. You can use any additional logging level you choose,
    # possibly logging.warning

# 20 points: Use of Object-Oriented Programming. This can be you creating your
    # own classes and modules OR the use of third party modules. If using
    # third party modules, be sure to put in the comments the
    # packages that need to be installed (probably from pip)

import logging
import sys
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
import pprint
                    
try:
    import functions as fn
    import students as st
    logging.debug("Able to import files...")
except:
    logging.critical("Missing functions.py!")
    print("Missing functions.py! Program is closing.")
    sys.exit()
    
"""
This project will allow the user to store students in a dictionary which will add them to the course.
In addition, it will also allow the user to drop the students from the course. Finally, the program will
allow the user to enter grades for the specified student and calculate their average.  The program will first
add students into the course. It will then give the option to drop students from the course. The only way to drop
those students is if they are already in the course. Finally, the user will be able to calculate the students average
based on their scores.  The only way to calculate the students average is if the student is present in the course
As a result, the user will be able to add students into the class, remove students from the class if they drop the
course, and calculate their grade average.

"""

"""
This is a main function that will allow all other function to run insde of it
all functions will call their specific dictionary in this function
"""
def main():
    print("Student Record Keeper".center(50, "*"))
    #executes while true to enter students into the class usinf addStudents function
    while True:
        #Ask user if they want to add students to the class (Yes or No)
        print("Do you want to enter students into the class? (Yes or No)")
        #set answer as the user input
        answer = input()
        #if user says yes, execute this block of code and continue
        if answer.lower() == "yes":
            #call the addStudents function passing
            #it the course dictionary
            fn.addStudents(fn.course)
            continue
        #if the user says no, execute this block of code to break
        elif answer.lower() == "no":
            break
        #Tell the user that they must enter yes or no to continue
        print("You must enter Yes or No!")
        continue
    
    #executes while true to drop students from the course
    while True:
        #prompts the user to enter whether they want to drop a student or not
        print("Do you want to drop any students? (Yes or No)")
        #set answer as user input
        answer = input()
        #if the user answer is yes, do this block of code
        if answer.lower() == "yes":
            #call the dropStudents functions
            fn.dropStudents(fn.course)
            #if no students in the dictionary, do this block of code
            if len(fn.course["addedStudents"]) == 0:
                #tell the user that no students to be dropped
                print("No students to drop from the course")
                break
            continue
        #if the user does not want to drop the students execute this and break
        elif answer.lower() == "no":
            break
        #tell the user to enter yes or no and start the loop over
        print("You must enter Yes or No!")
        continue
            
     #continue looping while true
    while True:
        #prompt user to calculate grade average
        print("Do you want to calculate the grade average for any student? (Yes or No)")
        answer = input()
        #if the the user answers yes, do this block of code
        if answer.lower() == "yes":
            #if no  students are in the dictionary, do this code
            if len(fn.course["addedStudents"]) == 0:
                #tell the user that there are no grades to calculate
                print("No students to calculate grades for.")
                break
            #call the setStudentGrade function
            else:
                #call the setStudentFunction and pass it the studentGradeAverage dictionary
                fn.setStudentGrade(fn.studentGradeAverage)        
        #if the user answers no, execute this and break
        elif answer.lower() == "no":
            break
        else:
            #tell the user that they must enter yes or no and continue with the loop
            print("You must enter yes or no!")
            continue

    #once you reach this point, everything will be in the records and
    #this section will print everything out
    fn.displayAverageRecords(fn.studentGradeAverage)
    #displayCourseRecords(course)
    #pprint.pprint(fn.studentGradeAverage)
    #pprint.pprint(fn.course)
    fn.displayActiveRoster(fn.activeRoster)
    fn.displayDroppedRoster(fn.droppedRoster)

#call the main function
main()
