import math
#Seth Everett
#2/1/2023

#run main()

#Section 6:Methods and Functions
    #57 Methods and Functions Homework Overview
def vol_sphere(radius):
    print((4/3)*3.14*(radius**3))
def range_check(num,low,high):
    if num > low and num < high:
        print(num," is out of the range between ",low," and ", high)
    else:
        print(num," is in the range between ", low," and ", high)
def upper_and_lower(text):
    Upper = 0
    Lower = 0
    for x in range(len(text)):
        if text[x].isupper() == True:
            Upper = Upper + 1
        if text[x].islower() == True:
            Lower = Lower + 1
    print("Upper :",Upper)
    print("Lower :", Lower)
def unique_list(lists):
    lists.sort()
    print( list(set(lists)))
def multiply(numbers):
    total = numbers[0]
    for x in range(len(numbers)-1):
        total = total * numbers[(x+1)]
    print(total)

def palindrome(string):
    string = string.replace(' ', '')
    print( string == string[::-1])
                   
#Section 8:Object oriented programming
    #73 Object oriented programming homework

class line:
    def __init__(self,coor1,coor2):
        self.c1a = coor1[0]
        self.c1b = coor1[1]
        self.c2a = coor2[0]
        self.c2b = coor2[1]
        self.distance()
        self.slop()
        print("Distance :",self.distance)
        print("Slop :",self.slop)
    def distance(self):
        self.distance = math.sqrt((2**(self.c2a - self.c1a))+(2**(self.c2b - self.c1b)))
    def slop(self):
        self.slop = (self.c2b - self.c1b)/(self.c2a - self.c1a)
class cylinder:
    def __init__(self,height,radius):
        self.h = height
        self.r = radius
        self.d = radius ** 2
        self.vol()
        self.sa()
        print("Volume :",self.vol)
        print("Surface Area :", self.sa)

    def vol(self):
        self.vol = 3.14159265 * self.d * self.h
    def sa(self):
        self.sa = 2 * 3.14159265 * self.r * (self.r+self.h)

def main():
    print("Volume of Sphere Function size 4")
    vol_sphere(4)
    print("Range check")
    range_check(2,4,5)
    range_check(4,3,6)
    print("Count uppers and lower case letters in text")
    print("Sample text: Apples are red and oranges grow on trees")
    upper_and_lower("Apples are red and oranges grow on trees")
    print("unique listing, list:1,1,1,1,4,3,2,4,4,3,2,1,4,4")
    unique_list([1,1,1,1,4,3,2,4,4,3,2,1,4,4])
    print("Multiply list, list:1,2,3,4,5,6,7,8,9")
    multiply([1,2,3,4,5,6,7,8,9])
    print("Palindrome test, phrase: nurse run")
    palindrome("nurse run")
    print("Class for line")
    li = line((3,2),(8,10))
    print("Class for cylinder")
    cy = cylinder(3,2)
