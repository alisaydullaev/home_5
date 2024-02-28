# class Person:
#     def __init__(self,fullname,age,is_married):
#         self.fullname=fullname
#         self.age=age
#         self.is_married=is_married

#     def info (self):
#         print(f"{self.fullname},{self.age},{self.is_married}")

# Aziz=Person("Muhammadaziz saydullaev","17","not married")         
# Ali=Person("Muhammadali saydullaev","17","not married")      

# Aziz.info()
# Ali.info()

##----------------------------------------------------------------------------------------------------------------------------------------------



# class Person:
#     def init(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def introduce_myself(self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age} лет, и я {self.gender}.")

# # Пример использования
# person1 = Person("Али", 17, "мужчина")
# person1.introduce_myself()

#----------------------------------------------------------------------------------------------------------------------------------------------

# class Person:
#     def init(self, name, age):
#         self.name = name
#         self.age = age

# class Teacher(Person):
#     def init(self, name, age, experience):
#         super().init(name, age)
#         self.experience = experience


# teacher1 = Teacher("Ali", 17, 10)
# print(teacher1.name)        
# print(teacher1.age)         
# print(teacher1.experience)  

#----------------------------------------------------------------------------------------------------------------------------------------------

# class Teacher:
#     def init(self, name, subject, salary):
#         self.name = name
#         self.subject = subject
#         self.salary = salary

# teacher1 = Teacher("Али", "Математика", 50000)
# print(teacher1.salary)
 


#----------------------------------------------------------------------------------------------------------------------------------------------




# class Teacher:
#     def init(self, name, subject, standard_salary, experience_years):
#         self.name = name
#         self.subject = subject
#         self.standard_salary = standard_salary
#         self.experience_years = experience_years

#     def calculate_salary(self):
#         bonus_per_year = 3000
#         bonus = self.experience_years * bonus_per_year
#         total_salary = self.standard_salary + bonus
#         return total_salary


# teacher1 = Teacher("али", "Математика", 50000, 5)
# salary_result = teacher1.calculate_salary()
# print(salary_result)


#----------------------------------------------------------------------------------------------------------------------------------------------


# class Teacher:
#     def init(self, name, subject, standard_salary, experience_years):
#         self.name = name
#         self.subject = subject
#         self.standard_salary = standard_salary
#         self.experience_years = experience_years

#     def calculate_salary(self):
#         bonus_per_year = 3000
#         bonus = self.experience_years * bonus_per_year
#         total_salary = self.standard_salary + bonus
#         return total_salary


# teacher1 = Teacher("Али", "Математика", 50000, 5)


# print(f"Имя: {teacher1.name}")
# print(f"Предмет: {teacher1.subject}")
# print(f"Стандартная зарплата: {teacher1.standard_salary}")
# print(f"Опыт (в годах): {teacher1.experience_years}")


# salary_result = teacher1.calculate_salary()
# print(f"Зарплата: {salary_result}")