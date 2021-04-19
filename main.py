from manipulateDB import *

#testing teachers functionality
teacher = Teacher(None, "Darken", 29653638) 
teacherId = crud(conn, 'c', teacher.insertData())
teacher.setTeacherId(teacherId)
print(crud(conn, 'r', teacher.getData()))
teacher.setFullName("fullName")
crud(conn, 'u', teacher.updateData()) 

#testing students functionality
student = Student(None, "achraf affes", "gremda km9", "55212353", "supcom", "indp2")
studentId =  crud(conn, 'c', student.insertData()) 
student.setStudentId(studentId)
print(crud(conn, 'r', student.getData()))
student.setLevel("55555")
crud(conn, 'u', student.updateData())
print(crud(conn, 'r', student.getData()))
crud(conn, 'd', student.deleteData())

#testing payments functionality
payment = Payment(None, 1, 3, "1998-08-32", "mathematics", 5, 70)
paymentId =  crud(conn, 'c', payment.insertData()) 
payment.setPaymentId(paymentId)
print(crud(conn, 'r', payment.getData()))
payment.setPrice(500)
crud(conn, 'u', payment.updateData())
conn.close()