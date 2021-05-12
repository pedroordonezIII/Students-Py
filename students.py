#INF 360 Programming in Python
#Pedro Ordonez
#Assignment Final Project
#students.py

"""
This will create a student object 
"""

class Student:

    #Initializer/Instance Attributes
    def __init__(self, name):
        self.name = name
        #self.grade = grade
        #self.average = average
        #self.activity = activity

    #function to tell the user the student is in the course
    def getActiveStudentInfo(self):
        print("The student {} is in the course.".format(self.name))

    #function to tell the user the student is dropped from the course
    def getDroppedStudentInfo(self):
        print("The student {} has been dropped from the course.".format(self.name))
               
