"""
Name: Seth Everett
File Name: Student_GPA_Cal.py
Description: The program will ask the user to input the student's last name
                based upon the input the program will either as for the rest of
                the student's informaiton such as first name and gpa or move on
                to the processing the students gpa and designating which student's
                gpa is within range of the Dean's list and the Honor Roll List.
"""


class Students:
    def __init__ (self,last_name,first_name,gpa):
        self.Last_Name = str(last_name)
        self.First_Name = str(first_name)
        self.GPA = float(gpa)
        self.Dean_List = False
        self.Honor_List = False
        self.__calc__()
    def __calc__(self):
        if self.GPA >= 3.5:
            self.Dean_List = True
            self.Honor_List = True
        elif (self.GPA > 3.25) and (self.GPA < 3.5):
            self.Dean_List = False
            self.Honor_List = True

#Initialization of Variables
point = ""
Students_List = []

#While loop will cont. till ZZZ is entered
while point != "ZZZ":
    point = str(input("Enter Student's last name or ZZZ to continue  -"))
    if point == "ZZZ":
        break
    else:
        #Creates the a Students object then add oject into list
        Students_List.append(Students(str(input("Enter Student's first name  -"))
                                      ,point,
                                      float(input("Enter Student's GPA  -"))))
#Formats and Prints out the top part of the table
print ("{:<20} {:<10} {:<20} {:<10}".format("Student's Name",'GPA',"Dean's List","Honor's List"))
#For loop goes through the Students List for the Students object
for x in range(len(Students_List)):
    #Prints out the properties of each student object based on position within the list
    print("{:<20} {:<10} {:<20} {:<10}".format(((Students_List[x].Last_Name)+"  "+(Students_List[x].First_Name)),
                                               (str(Students_List[x].GPA)),
                                               (Students_List[x].Dean_List),
                                               (Students_List[x].Honor_List)))
