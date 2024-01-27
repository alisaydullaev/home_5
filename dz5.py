import random

def welcome_message():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадаю число от 1 до 100, а вы попробуете угадать его.")

def generate_secret_number():
    return random.randint(1, 100)

def play_guessing_game(secret_number):
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
    welcome_message()
    secret_number = generate_secret_number()
    play_guessing_game(secret_number)