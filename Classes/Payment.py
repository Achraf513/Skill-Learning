class Payment :

    sql_create_payment_table = """CREATE TABLE IF NOT EXISTS payments (
        paymentId INTEGER PRIMARY KEY, 
        studentId integer,                          
        teacherId integer, 
        sessionNbr integer,
        lastPaymentDate date,
        subject text,      
        price integer
    );"""

    def __init__(self,paymentId,studentId,sessionNbr,lastPaymentDate,subject,teacherId,price): 
        self.__paymentId = paymentId
        self.__studentId = studentId
        self.__sessionNbr = sessionNbr  
        self.__lastPaymentDate = lastPaymentDate        
        self.__subject = subject 
        self.__teacherId = teacherId 
        self.__price = price 

    def getPaymentId(self):
        return self.__paymentId
    def getStudentId(self):
        return self.__studentId
    def getSessionNbr(self):
        return self.__sessionNbr 
    def getLastPaymentDate(self):
        return self.__lastPaymentDate
    def getSubject(self):
        return self.__subject
    def getTeacherId(self):
        return self.__teacherId 
    def getPrice(self):
        return self.__price
    
    def setPaymentId(self,paymentId):
        self.__paymentId = paymentId
    def setStudentId(self,studentId):
        self.__studentId = studentId
    def setSessionNbr(self,sessionNbr):
        self.__sessionNbr = sessionNbr  
    def setLastPaymentDate(self,lastPaymentDate):
        self.__lastPaymentDate = lastPaymentDate
    def setSubject(self,subject):
        self.__subject = subject
    def setPrice(self,price):
        self.__price = price
    def setTeacherId(self,teacherId):
        self.__teacherId = teacherId
        

    def insertData(self):
        sql_insert_query ="""INSERT INTO payments(studentId,sessionNbr,lastPaymentDate,subject,price,teacherId)
            VALUES('{studentId}','{sessionNbr}','{lastPaymentDate}','{subject}','{price}','{teacherId}')""".format(
                studentId = self.__studentId,
                sessionNbr = self.__sessionNbr,
                lastPaymentDate = self.__lastPaymentDate,
                subject = self.__subject,
                price = self.__price,
                teacherId = self.__teacherId
            )
        return sql_insert_query

    def getData(self):
        sql_select_query = """SELECT * FROM payments WHERE paymentId='{id}' """.format(id=self.__paymentId)
        return sql_select_query

    def deleteData(self):
        sql_delete_query = """DELETE FROM payments WHERE paymentId='{id}'""".format(
            id = self.__paymentId 
        )
        return sql_delete_query
    
    def updateData(self):
        sql_update_query = """UPDATE payments SET studentId='{studentId}',sessionNbr='{sessionNbr}',lastPaymentDate='{lastPaymentDate}',
                            subject='{subject}',price='{price}',teacherId='{teacherId}' WHERE paymentId='{id}'""".format(
            id = self.__paymentId,
            studentId = self.__studentId,
            sessionNbr = self.__sessionNbr,
            lastPaymentDate = self.__lastPaymentDate,
            subject = self.__subject,
            price = self.__price,
            teacherId= self.__teacherId
        ) 
        return sql_update_query