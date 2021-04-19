from manipulateDB import *

class Teacher :

    sql_create_teacher_table = """CREATE TABLE IF NOT EXISTS teachers (
        teacherId INTEGER PRIMARY KEY, 
        fullName text,                          
        phoneNbr integer
    );"""

    def __init__(self,teacherId,fullName,phoneNbr): 
        self.__teacherId = teacherId
        self.__fullName = fullName
        self.__phoneNbr = phoneNbr    
        
    def getTeacherId(self):
        return self.__teacherId
    def getFullName(self):
        return self.__fullName
    def getPhoneNbr(self):
        return self.__phoneNbr  
      
    def setTeacherId(self,teacherId):
        self.__teacherId = teacherId
    def setFullName(self,fullName):
        self.__fullName = fullName  
    def setPhoneNbr(self,phoneNbr):
        self.__phoneNbr = phoneNbr 
         
    def getData(self):
        sql_select_query = """SELECT * FROM teachers WHERE teacherId='{teacherId}' """.format(teacherId=self.__teacherId)
        return sql_select_query

    def insertData(self):
        sql_insert_query ="""INSERT INTO teachers(fullName,phoneNbr) VALUES('{fullName}','{phoneNbr}')""".format(
            fullName = str(self.__fullName),
            phoneNbr = str(self.__phoneNbr),
        )
        return sql_insert_query
    
    def deleteData(self):
        sql_delete_query = """DELETE FROM teachers WHERE teacherId='{id}'""".format(
            id = self.__teacherId 
        )
        return sql_delete_query
    
    def updateData(self):
        sql_update_query = """UPDATE teachers SET fullName='{fullName}',phoneNbr='{phoneNbr}' WHERE teacherId='{id}'""".format(
            id = self.__teacherId,
            fullName = self.__fullName,
            phoneNbr = self.__phoneNbr,
        ) 
        return sql_update_query