import random

# Генерируем 4-значное число с неповторяющимися цифрами
digits = list("0123456789")
random.shuffle(digits)
rand = ''.join(digits[:4])

print('*** Игра "Быки и коровы" ***')
print('Компьютер загадал 4-значное число с разными цифрами.')
print('Попробуйте его угадать!')

count = 1
number = input('Введите 4-значное число: ')

while number != rand:
    bulls = 0  # цифры на правильных местах
    cows = 0   # цифры есть, но на других местах

    for i in range(4):
        if number[i] == rand[i]:
            bulls += 1
        elif number[i] in rand:
            cows += 1

    print(f'Быков: {bulls}, Коров: {cows}')
    count += 1
    number = input('Попробуйте ещё раз: ')

print('Вы угадали число!')
print('Количество потраченных попыток:', count)
