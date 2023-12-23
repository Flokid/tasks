import random
import string
import sys

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_pass_len(pass_len):
    if 8 <= pass_len <= 32:
        generated_password = generate_password(pass_len)
        print(f"Сгенерированный пароль: {generated_password}")
    else:
        print("Некорректная длина пароля! Длина должна быть от 8 до 32 символов.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password_length = int(sys.argv[1])
        check_pass_len(password_length)
    else:
        print("Введите длину пароля от 8 до 32 символов в качестве аргумента командной строки.")
