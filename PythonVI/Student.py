class Student():
    def __init__(self,dni,name,surname,age,city,province,email):
        self.__Dni = dni
        self.__Name = name
        self.__Surnames = surname
        self.__Age = age
        self.__City = city
        self.__Province = province
        self.__Email = email

    def getDni(self):
        return self.__Dni
    def setName(self):
        return self.__Name
    def getSurnames(self):
        return self.__Surnames
    def getAge(self):
        return self.__Age 
    def getCity(self):
        return self.__City 
    def getProvince(self):
        return self.__Province
    def getEmail(self):
        return self.__Email