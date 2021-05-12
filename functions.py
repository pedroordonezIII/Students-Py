#INF 360 Programming in Python
#Pedro Ordonez
#Assignment Final Project
#functions.py

#import pprint
import students

#The course dictionary with addedS tudents and droppedStudents Keys
#It is in the global scope
course = {"addedStudents":[],
          "droppedStudents":[], }

##attendance = {}

##roster list for with student objects for those currently in the class
activeRoster = []

##roster list for the student object for those dropping the course
droppedRoster = []

#Empty dictionary to hold student grade average
studentGradeAverage = {}

"""
This file will hold all of the basic functionality used throughout this program
"""

"""
This function takes a dictionary and adds students to the course. The students that
are taking the course are added by the user based on their input that must be in letters
and in title format.  
"""
def addStudents(dictionary):
    #continue looping while true
   #while True:
       #prompt user to enter their full name (first and last name)
       #print("Add students by typing their full name.:(Leave blank to stop adding)")
       #set student variable as input
       #student = input()

   #prompt user to enter their full name (first and last name) to add to course
   print("Add students by typing their full name.")
   #set student variable as input
   student1 = input()
   
   #the input must be in title format or blank to continue
   if student1.istitle() or student1 == "":
       #if user input is blank, stop adding users
       #if student == "":
           #break
        
       #if no students have been added, add the first student
       if len(dictionary["addedStudents"]) == 0:
           #add to the dictionary key addedStudents and append the student to its list
           dictionary["addedStudents"].append(student1)
           #create a student object and make the name attribute as the user input
           student = students.Student(student1)
           #add the student object into the activeRoster
           activeRoster.append(student.name)
           #tell the user the student has been added 
           student.getActiveStudentInfo()
       #if more than one student has been added, check if the student has
       #already been added and if they are not in the dictionary, append them to the list
       elif student1 not in dictionary["addedStudents"]:
           #add to the dictionary key addedStudents and append the students to its list
           dictionary["addedStudents"].append(student1)
           #make a student object and make the name as the user input
           student = students.Student(student1)
           #add the student into the active roster 
           activeRoster.append(student.name)
           #tell the user that the student has been added 
           student.getActiveStudentInfo()

       #if the student has not been added, add them into the class
       else:
           print("The student was already added.")
           
       #sort the dictionary by the first alphabetical letter    
       dictionary["addedStudents"].sort()
       
   #tell the user that they must enter their input in title case and lets them continue
   else:
       print("Must enter first name and last name with capital letter and proper case.")
       #continue

"""
This function take a dictionary as input and removes the students from the class
and places them in the dropped list of the dictionary. It does this by prompting
the user to drop students if they wish. If they say yes, the user must enter student
name to remove and if no students in the course, it breaks. If the student is in the
dictionary, it removes them from the key addedStudents and places them in the droppedStudents
key value list. If the student is not in the dictionary with the key addedStudents, then the
student is not in the class and the function begins again.  
"""
def dropStudents(dictionary):
    #executes while true
    #while True:
        #prompts the user to enter whether they want to drop a student or not
        #print("Do you want to drop any students? (Yes or No)")
        #set answer as user input
        #answer = input()

        #if the user answer is yes, do this block of code
        #if answer.lower() == "yes":
            
    #tell the user to enter the student to drop exactly as before
    print("Enter the students full name the exact way you entered it:")

    #set student variable equal to studentToDrop
    studentToDrop = input()

    #if the key is empty, tell the user no students are in the course and break
    if len(dictionary["addedStudents"]) == 0:
        print("No students in the course.")
        #break

    #if the student entered is in the list of the value addedStudent do this
    elif studentToDrop in dictionary["addedStudents"]:
        #remove the student from the key addedStudents
        dictionary["addedStudents"].remove(studentToDrop)
        #add the student to the key droppedStudents in the dictionary and append it to the list
        dictionary["droppedStudents"].append(studentToDrop)
        #make a student object and make the name attribute as the user input
        student = students.Student(studentToDrop)
        #place the student that is being dropped into the dropped roster
        droppedRoster.append(student.name)
        #remove the student from the active roster
        activeRoster.remove(student.name)
        #tell the user that the student has been dropped
        student.getDroppedStudentInfo()
        #print("Student dropped.")

    #if the student is not in the addedStudents dictionary, tell the user and allow them to start again
    elif studentToDrop not in dictionary["addedStudents"]:
        print("Student is not in the class.")
                
        #break if user no longer wants to drop students
        #elif answer.lower() == "no":
            #break

        #tell user to enter yes or no and let them continue
        #else:
            #print("You must enter yes or no!")
            

"""
This function takes a dictionary as a parameter and places the previous
values as the keys in a new dictionary while setting the values as the
average of their grade being entered. This function first asks the user
to enter a name to calculate the average for.  If the name is a key in
the course dictionary, then the student is in the class.  If the student
is in the class, calculate the student average by calling that specific
function, and that the return value equal to studentAverage.  It will then
set the studentGradeAverage dictionary key as the student and the average
of their grades as the value. 
"""
def setStudentGrade(dictionary):
    '''
    for i in course["addedStudents"]:
        studentGradeAverage.setdefault(i, )
    '''
    #continue looping while true
    #while True:
    
    #Prompt the user to enter a name to calculate the average for
    print("Enter the name of the student to calculate grade average for.: (first and last name)")
    #set this value as the input value
    global student
    student = input()

    #break loop if course dictionary is empty
    #if len(dictionary["addedStudents"]) == 0:
        #break

    #check if the student is actualy in the course by seeing if student is in the
    #course dictionary with the addedStudents key
    if student in course["addedStudents"]:
        #set this variable equal to the return value of the calculatedGradeAverage
        studentAverage = calculateGradeAverage()
        #if the student is already present, replace the updated average from the other one
        if student in studentGradeAverage:
            studentGradeAverage[student] = studentAverage
        #set the studentGradeAverage dictionary key as the student and the average grade
        #as the value. This block of code will only happen if no average has been calculated for the student
        else:
            studentGradeAverage.setdefault(student, studentAverage)

    #if the student is not in the course or actually the addedStudents key
    #, tell the user and continue
    else:
        print("Student is not in the class.")
            #continue

        #prompt the user to see if they want to do another average    
        #print("Do you want to calculate another student grade average?")
        #let response be the user input
        #response = input()

        #if the response is yes, continue executing
        #if response.lower() == "yes":
            #continue

        #if the response is no, break the loop 
        #elif response.lower() == "no":
            #break

        #tell the user to enter yes or no and let them continue executing   
        #else:
            #print("You must enter yes or no!")

                
#def studentAttendance(dictionary):


"""
This function calculated the average based on floating point numbers and integers
entered by the user.  This average number will be assigned to the value in a dictionary.
This program will keep a running addition total based on user input and will store the
grades in a grades list.  Once the user is done entering grades, the average is found
by taking the total and dividing by the length of the grades list. The average is then
returned.  
 """
def calculateGradeAverage():
    #a variable to hold the running total of the sum
    total = 0
    #a variable to hold the average of all the averages for a student
    total2 = 0
    #a variable to hold the average 
    average = 0
    #a list to hold the grades entered by the user
    grades = []
    if student in studentGradeAverage:
        grades.append(studentGradeAverage.get(student))
        #pprint.pprint(grades)
    #continue while true
    while True:
        #this try statement will check if the input is a floating point number or integer
        #If it is not, tell the user to enter a number and continue the input
        try:
            #prompt the user to enter the grade in integer or floating point format
            print("Enter the grade in integer or floating point format for this student.: (Ex: 90.5)")
            #set grade as the input of the user 
            grade = input()
            #if the user input is a float or integer continue with this block of code
            if float(grade) or int(grade):
                #append the value to the grades list
                grades.append(grade)
        #tell the user to enter the number and continue 
        except:
            print("Enter a number!")
            
        #ask the user if they want to continue entering more grades
        print("Do you want to enter another grade for this student? (Yes or No)")
        #set response1 equal to the user input
        response1 = input()
        #if the response is yes, let the user continue
        if response1.lower() == "yes":
            continue
        #if the response is no, break the loop and continue 
        elif response1.lower() == "no":
            break
        #if the user enters wrong information, tell them and let them continue
        else:
            print("You must enter yes or no!")
            break
    if(len(grades)) > 0:
        #loop through the grades list from index 0 to length - 1   
        for i in range(len(grades)):
            #update the total value and turn the value to a float because it may be an integer
            total += float(grades[i])
        #calculate the average based on the total and the length of the list
        average = total / len(grades)
 
    #return the average
    return average

"""
This function print the key value pairs to show the name and the average of the
student.
"""
def displayAverageRecords(dictionary):
        #using the key value pair, print the items from the dictionary
        for k, v in dictionary.items():
            print("The grade average for " + k + " is " + str(v) + ".")

"""
This function will print out the active roster of students in the course
"""
def displayActiveRoster(list):
   #header for the dropped roster
   print("**********Active Student Roster**********")
   #for loop that iterates through the range of the list
   for i in range(len(list)):
         #prints each item in the list with a new line character after it
         print(list[i])

"""
This function will print out the dropped roster of students in the course
"""
def displayDroppedRoster(list):
   #header for the dropped roster
   print("**********Dropped Student Roster**********")
   #for loop that iterates through the range of the list
   for i in range(len(list)):
         #prints each item in the list with a new line character after it
         print(list[i])
    
"""
def displayCourseRecords(dictionary):
    for v in dictionary.values():
        if len(dictionary) > 0:
            print("The studentts in the course are
"""

