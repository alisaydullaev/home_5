# class GeeksPeople:
#     def __init__(self,phone,email,name):
#         self.phone=phone
#         self.email=email
#         self.name=name

#     def __str__(self):
#         return f" телефон - {self.phone}, почта-{self.email}, имя-{self.name}"

# class Student(GeeksPeople):
#     def __init__(self, phone, email, name, student_id , group_where_study, ):
#         GeeksPeople.__init__(self, phone, email, name)
#         self.student_id=student_id
#         self.group_where_study=group_where_study

#     def study(self):
#         print(f"группа где он учиться {self.group_where_study}, ")

#     def __str__(self):
#         return super().__str__() + f"группа где он учиться {self.group_where_study}, {self.student_id}"
    
# student = Student("Сыймык", "syimyk@gmail.com", "07535725758252", 5555, "14-2B")
# student.study()
# print(student)

# class Teacher(GeeksPeople):
#     def __init__(self, phone, email, name, teacher_id, group_where_teach):
#         GeeksPeople.__init__(self, phone, email, name)
#         self.teacher_id=teacher_id
#         self.group_where_teach=group_where_teach

#     def teach(self):
#         print(f"группа где он учит {self.group_where_teach},")

#     def __str__(self):
#         return super().__str__() + f"группа где он учит {self.group_where_teach}, ID- {self.teacher_id}"
    
# teacher= Teacher("Сыймык", "syimyk@gmail.com", "07535725758252", 5555, "14-2B") 
# teacher.teach() 
# print(teacher) 

# class Admin(GeeksPeople):
#     def __init__(self, phone, email, name, admin_id, group_where_admin):
#         GeeksPeople.__init__(self, phone, email, name)
#         self.admin_id=admin_id
#         self.group_where_admin=group_where_admin
#     def admin(self):
#         print(f"Админестратор группы: {self.group_where_admin},")

# class Mentor(Teacher,Student):
#     def __init__(self, phone, email, name, teacher_id, group_where_teach, student_id , group_where_study):
#         Student.__init__(self, phone, email, name, student_id , group_where_study)
#         Teacher.__init__(self, phone, email, name, teacher_id, group_where_teach)

#     def __str__(self):
#         return Student.__str__(self) + f"группа где он учит {self.group_where_teach}, {self.teacher_id}"

# mentor = Mentor(225353533, 'email@gmail.com', 'Nurai', 1, "14-2B", 1, "14-2B" )
# print(mentor)