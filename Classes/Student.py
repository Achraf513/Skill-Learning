
class Student :

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS students (
        studentId INTEGER PRIMARY KEY, 
        fullName text,
        address text,                                
        level text, 
        phoneNbr integer, 
        establishement text
    );"""

    def __init__(self,studentId,fullName,address,phoneNbr,establishement,level): 
        self.__studentId = studentId
        self.__fullName = fullName  
        self.__address = address        
        self.__level = level 
        self.__phoneNbr = phoneNbr 
        self.__establishement = establishement 

    def getStudentId(self):
        return self.__studentId
    def getFullName(self):
        return self.__fullName 
    def getAddress(self):
        return self.__address
    def getLevel(self):
        return self.__level 
    def getPhoneNbr(self):
        return self.__phoneNbr 
    def getEstablishement(self):
        return self.__establishement
    
    def setStudentId(self,studentId):
        self.__studentId = studentId
    def setFullName(self,fullName):
        self.__fullName = fullName  
    def setAddress(self,address):
        self.__address = address
    def setLevel(self,level):
        self.__level = level
    def setPhoneNbr(self,phoneNbr):
        self.__phoneNbr = phoneNbr
    def setEstablishement(self,establishement):
        self.__establishement = establishement 

    def insertData(self):
        sql_insert_query ="""INSERT INTO students(fullName,address,level,phoneNbr,establishement)
            VALUES('{fullName}','{address}','{level}','{phoneNbr}','{establishement}')""".format(
                fullName = self.__fullName,
                address = self.__address,
                level = self.__level,
                phoneNbr = self.__phoneNbr,
                establishement = self.__establishement
            )
        return sql_insert_query
    
    def getData(self):
        sql_select_query = """SELECT * FROM students WHERE studentId='{id}' """.format(id=self.__studentId)
        return sql_select_query

    def deleteData(self):
        sql_delete_query = """DELETE FROM students WHERE studentId='{id}'""".format(
            id = self.__studentId 
        )
        return sql_delete_query
    
    def updateData(self):
        sql_update_query = """UPDATE students SET fullName='{fullName}',address='{address}',level='{level}',
            phoneNbr='{phoneNbr}',establishement='{establishement}' WHERE studentId='{id}'""".format(
            id = self.__studentId,
            fullName = self.__fullName,
            address = self.__address,
            level = self.__level,
            phoneNbr = self.__phoneNbr,
            establishement = self.__establishement
        ) 
        return sql_update_query