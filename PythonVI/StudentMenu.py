import Student
import re

StudentsList = {}

def readDni():
    try:
       dni = input("Set a Dni: ")
       assert(re.search("^[0-9]{8,8}[A-Za-z]$",dni))
       return dni
    except:
        print("Invalid Dni")

def readName():
    try:
        name = input("Set a Name: ")
        return name
    except:
        print("Invalid Name")

def readSurnames():
    try:
        Surnames = input("Set Surnames: ")
        return Surnames
    except:
        print("Invalid Surnames")
def readAge():
    try:
        Age = int(input("Set an age"))
        return Age
    except:
        print("Invalid Age")
def readCity():
    try:
        City = input("Set a city")
        return City
    except:
        print("Invalid city")
def readProvince():
    try:
        Province = int(input("Set a province"))
        return Province
    except:
        print("Invalid Province")
def readEmail():
    try:
        Email= int(input("Set an Email"))
        assert(re.search("^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}", email))
        return Email
    except:
        print("Invalid Email")
def addStudent(dni,name,surname,age,city,province,email):
    try:
        student = Student.Student(dni,name,surname,age,city,province,email)
        StudentsList[student.getDni()] = student
    except:
        print("Add this student is not possible")
def searchStudent(dni,ListStudents):
    try:
        for key,st in ListStudents.items():
            if key == dni:
                return st
        return None
    except:
        print("SOmething wrone with the search")
        return None
def deleteStudent(st):
    StudentsList.popitem(st)
def modifyStudent(st):
     while True:
            print("MODIFY")
            print("----------")
            print("2.- Modify Name")
            print("3.- Modify Surnames")
            print("4.- Modify Age")
            print("5.- Modify City")
            print("6.- Modify Province")
            print("7.- Modify Email")
            opt = int(input("Choose an option: "))
            break
while True:
    try:
        while True:
            print("STUDENT CRUD")
            print("----------")
            print("1.- Add a student")
            print("2.- Delete a student")
            print("3.- Modify a student")
            print("4.- Search a student")
            print("5.- Exit")
            option = int(input("Choose an option: "))
            break

        if option == 5:
            print("Goodbye!!")
            break
        elif option==1:    
            dni = readDni()
            name = readName()
            surnames = readSurnames()
            age = readAge()
            city = readCity()
            province = readProvince()
            email = readEmail()
            addStudent(dni,name,surnames,age,city,province,email)
        elif option ==2:
            dni = readDni()
            st = searchStudent(dni)
            deleteStudent(st)

        elif option == 3:
            dni = readDni()
            st = searchStudent(dni)
            modifyStudent(st)

    except AssertionError:
        print("Bad data")
    except Exception:
        print("Something isn't good!")
