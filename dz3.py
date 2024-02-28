# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory

# my_computer = Computer("Intel i7", 16)


# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory

#     def make_computations(self, operation, operand):
#         if operation == '+':
#             result = self.cpu + self.memory + operand
#         elif operation == '-':
#             result = self.cpu - self.memory - operand
#         elif operation == '*':
#             result = self.cpu * self.memory * operand
#         elif operation == '/':
#             result = self.cpu / (self.memory + operand)
#         else
#             return "Invalid operation"

#         return f"Result of {self.cpu} {operation} {self.memory} {operation} {operand} is {result}"

# my_computer = Computer(4, 2)
# result = my_computer.make_computations('+', 3)
# print(result)





# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory

#     @property
#     def cpu(self):
#         return self.__cpu

#     @property
#     def memory(self):
#         return self.__memory

#     def make_computations(self, operation, operand):
#         if operation == '+':
#             result = self.cpu + self.memory + operand
#         elif operation == '-':
#             result = self.cpu - self.memory - operand
#         elif operation == '*':
#             result = self.cpu * self.memory * operand
#         elif operation == '/':
#             result = self.cpu / (self.memory + operand)
#         else:
#             return "Invalid operation"

#         return f"Result of {self.cpu} {operation} {self.memory} {operation} {operand} is {result}"

# my_computer = Computer(4, 2)
# cpu_value = my_computer.cpu
# memory_value = my_computer.memory
# print(f"CPU: {cpu_value}, Memory: {memory_value}")
# result = my_computer.make_computations('+', 3)
# print(result)




# class Laptop(Computer):
#     def __init__(self, cpu, memory, memory_card):
#         super().init(cpu, memory)
#         self.__memory_card = memory_card

#     @property
#     def memory_card(self):
#         return self.__memory_card


# my_laptop = Laptop("Intel i5", 8, "SDXC")
# cpu_value = my_laptop.cpu
# memory_value = my_laptop.memory
# memory_card_value = my_laptop.memory_card
# print(f"CPU: {cpu_value}, Memory: {memory_value}, Memory Card: {memory_card_value}")
# result = my_laptop.make_computations('*', 2)
# print(result)



# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory

#     @property
#     def cpu(self):
#         return self.__cpu

#     @property
#     def memory(self):
#         return self.__memory

# class Laptop(Computer):
#     def __init__(self, cpu, memory, memory_card):
#         super().init(cpu, memory)
#         self.__memory_card = memory_card

#     @property
#     def memory_card(self):
#         return self.__memory_card

# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory

#     @property
#     def cpu(self):
#         return self.__cpu

#     @property
#     def memory(self):
#         return self.__memory

#     def make_computations(self, operation, operand):

#     def info(self):
#         return f"Computer - CPU: {self.cpu}, Memory: {self.memory}"


# class Laptop(Computer):
#     def init(self, cpu, memory, memory_card):
#         super().init(cpu, memory)
#         self.__memory_card = memory_card

#     @property
#     def memory_card(self):
#         return self.__memory_card

#     def info(self):
#         return f"Laptop - CPU: {self.cpu}, Memory: {self.memory}, Memory Card: {self.memory_card}"


# my_computer = Computer("Intel i7", 16)
# my_laptop = Laptop("Intel i5", 8, "SDXC")

# print(my_computer.info())
# print(my_laptop.info())




# class Computer:
#     def init(self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory

#     @property
#     def cpu(self):
#         return self.__cpu

#     @property
#     def memory(self):
#         return self.__memory

#     def make_computations(self, operation, operand):
#         if operation == '+':
#             result = self.cpu + self.memory + operand
#         elif operation == '-':
#             result = self.cpu - self.memory - operand
#         elif operation == '*':
#             result = self.cpu * self.memory * operand
#         elif operation == '/':
#             result = self.cpu / (self.memory + operand)
#         else:
#             return "Invalid operation"

#         return f"Result of {self.cpu} {operation} {self.memory} {operation} {operand} is {result}"

#     def info(self):
#         return f"Computer - CPU: {self.cpu}, Memory: {self.memory}"


# class Laptop(Computer):
#     def __init__(self, cpu, memory, memory_card):
#         super().init(cpu, memory)
#         self.__memory_card = memory_card

#     @property
#     def memory_card(self):
#         return self.__memory_card

#     def info(self):
#         return f"Laptop - CPU: {self.cpu}, Memory: {self.memory}, Memory Card: {self.memory_card}"


# my_computer = Computer("Intel i7", 16)
# my_laptop = Laptop("Intel i5", 8, "SDXC")

# print(my_computer.info())
# print(my_laptop.info())

# result_computer = my_computer.make_computations('+', 5)
# result_laptop = my_laptop.make_computations('*', 2)

# print(result_computer)
# print(result_laptop)
