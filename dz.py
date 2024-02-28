class Math:
    def init(self, value):
        self.value = value

    def add(self, other):
        if isinstance(other, Math):
            return Math(self.value + other.value)
        else:
            raise TypeError("Unsupported operand type for +")

    def sub(self, other):
        if isinstance(other, Math):
            return Math(self.value - other.value)
        else:
            raise TypeError("Unsupported operand type for -")

# Создаем экземпляр класса
math_instance = Math(5)

# Примеры сложения и вычитания
result_addition = math_instance + Math(3)
result_subtraction = math_instance - Math(2)

# Выводим результаты
print("Сложение:", result_addition.value)
print("Вычитание:", result_subtraction.value)