def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадаю число от 1 до 100, а вы попробуете угадать его.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Ваше предположение: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
            break
        elif user_guess < secret_number:
            print("Нет, число больше. Попробуйте еще раз.")
        else:
            print("Нет, число меньше. Попробуйте еще раз.")

if name == "main":
    guess_the_number()