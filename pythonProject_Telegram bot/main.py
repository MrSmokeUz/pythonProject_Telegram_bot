import telebot
from telebot import types

# Укажите действительный токен вашего бота
bot = telebot.TeleBot('7565080323:AAGFgMxAvQrehCJG1unhKtXLoijGet_m1iM')

# Глобальная переменная для хранения текста пользователя
shifr = ''

# Шифр Цезаря
def caesar_cipher(text, shift):
    encrypted = ''
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted += char
    return encrypted

# Упрощенный AES
# AES (Advanced Encryption Standard) — это симметричный блочный шифр, который шифрует данные блоками по 128 бит, используя ключ длиной 128, 192 или 256 бит.
#
# Процесс шифрования:
#
#     SubBytes: Заменяет каждый байт по таблице замен (S-Box).
#     ShiftRows: Сдвигает строки блока для перемешивания данных.
#     MixColumns: Перемешивает байты в столбцах блока.
#     AddRoundKey: Добавляет ключ раунда с помощью XOR.
#
#
#
# Декодирование — обратный процесс с использованием того же ключа.
# AES безопасен благодаря множественным преобразованиям и сложности подбора ключа.

# Шаги:
#
#     Итерация по символам текста:
#     Цикл проходит по каждому символу строки text.
#
#     Применение XOR:
#         ord(text[i]): Преобразует символ текста в его числовое представление (код символа в Unicode).
#         ord(key[i % len(key)]): Берёт символ из ключа (с использованием остатка % для циклического использования ключа, если он короче текста) и преобразует его в числовое представление.
#         ^: Выполняет побитовое XOR между числовыми представлениями символа текста и символа ключа.
#
#     Преобразование обратно в символ:
#         chr(...): Преобразует результат XOR обратно в символ.
#
#     Добавление символа в зашифрованный текст:
#     Каждый результат преобразования добавляется к строке encrypted.

# text = "Hello"
# key = "key"
#
# # Пошаговое выполнение:
# # i = 0: text[0] = 'H', key[0 % 3] = 'k' → ord('H') ^ ord('k') = 72 ^ 107 = 35 → chr(35) = '#'
# # i = 1: text[1] = 'e', key[1 % 3] = 'e' → ord('e') ^ ord('e') = 101 ^ 101 = 0 → chr(0) = '\x00'
# # i = 2: text[2] = 'l', key[2 % 3] = 'y' → ord('l') ^ ord('y') = 108 ^ 121 = 21 → chr(21) = '\x15'
# # ...
#
# # Результат:
# encrypted = "#\x00\x15..."


def simple_aes(text, key):
    encrypted = ''
    for i in range(len(text)):
        encrypted += chr(ord(text[i]) ^ ord(key[i % len(key)]))  # XOR с ключом
    return encrypted

# a) Разделение на блоки:
#
#     range(0, len(text), 8): Цикл обрабатывает текст по блокам длиной 8 символов.
#     text[i:i+8]: Извлекается текущий блок текста.
#     .ljust(8, '\0'): Если блок короче 8 символов, он дополняется символом '\0' (нулевой байт).
#
# Пример:
#
#     Текст: "HelloWorld".
#     Первый блок: "HelloWor".
#     Второй блок: "ld\0\0\0" (добавлены три нулевых байта).

# Каждый символ в блоке шифруется с помощью XOR:
#
#     Циклический выбор ключа: key[j % len(key)] позволяет использовать ключ повторно, если он короче блока.
#     Преобразование символов:
#         ord(block[j]): Преобразует символ блока в числовой код (Unicode).
#         ord(key[j % len(key)]): Преобразует символ ключа в числовой код.
#         ^: Выполняет побитовое XOR между кодами символа блока и ключа.
#         chr(...): Преобразует результат обратно в символ.
#
# Результат: Зашифрованный блок длиной 8 символов
# text = "HelloWorld"
# key = "key"
#
# # Пошагово:
# # Блок 1: "HelloWor"
# # Шифрование: Каждый символ XOR'ится с символами ключа "key".
# # Блок 2: "ld\0\0\0" (дополнено '\0').
#
# encrypted = simple_blowfish(text, key)


# Упрощенный Blowfish
def simple_blowfish(text, key):
    encrypted = ''
    for i in range(0, len(text), 8):
        block = text[i:i+8].ljust(8, '\0')
        encrypted_block = ''.join(chr(ord(block[j]) ^ ord(key[j % len(key)])) for j in range(8))
        encrypted += encrypted_block
    return encrypted

# Шаги:
#
#     Обработка каждого символа текста: Цикл проходит по каждому символу строки text.
#
#     Конвертация символа в число:
#         ord(char): Преобразует символ в числовое представление (код символа в Unicode).
#
#     Шифрование с использованием RSA:
#         pow(ord(char), e, n): Выполняет операцию (ord(char)e)mod  n(ord(char)e)modn.
#         Это основное шифрование в алгоритме RSA.
#             ord(char)ord(char): Исходное значение символа.
#             ee: Открытая экспонента (часть ключа).
#             nn: Модуль (часть ключа).
#
#     Преобразование обратно в символ:
#         chr(...): Преобразует результат шифрования обратно в символ.
#
#     Добавление зашифрованного символа в результат:
#         Каждый зашифрованный символ добавляется в строку encrypted.
# text = "Hi"
# e = 3
# n = 33
# Пошаговая обработка:
#
#     Первый символ: 'H'
#         ord('H') = 72
#         Шифрование: (723)mod  33=18(723)mod33=18
#         chr(18) = '\x12' (непечатный символ).
#
#     Второй символ: 'i'
#         ord('i') = 105
#         Шифрование: (1053)mod  33=15(1053)mod33=15
#         chr(15) = '\x0f'.
#
# Результат: encrypted = '\x12\x0f'.
# Упрощенный RSA
def rsa_encrypt(text, e, n):
    encrypted = ''
    for char in text:
        encrypted += chr(pow(ord(char), e, n))  # (char ^ e) mod n
    return encrypted

def rsa_decrypt(encrypted_text, d, n):
    decrypted = ''
    for char in encrypted_text:
        decrypted += chr(pow(ord(char), d, n))  # (char ^ d) mod n
    return decrypted
# Начало работы бота , бот отправляет пользавателю сообщение с предложением ввести текст который он хочет зашифровать или дешифровать
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Введи текст, который ты хочешь зашифровать или расшифровать.')
    # Переходит на следующий этап
    bot.register_next_step_handler(message, ask)
# Отправляет сообщению  с выбором кнопки операции
def ask(message):
    global shifr
    shifr = message.text  # Сохраняем текст пользователя
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Зашифровать', callback_data='crypt')
    key_no = types.InlineKeyboardButton(text='Расшифровать', callback_data='decrypt')
    keyboard.add(key_yes, key_no)

    question = 'Что ты хочешь сделать?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "crypt")
def crypt_handler(call):
    ask_crypt(call.message.chat.id)  # Переходим к выбору шифра

@bot.callback_query_handler(func=lambda call: call.data == "decrypt")
def decrypt_handler(call):
    ask_decrypt(call.message.chat.id)  # Переходим к выбору дешифрования

# Выводит выбор из различных шифрований
def ask_crypt(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    key_one = types.InlineKeyboardButton(text='Шифр Цезаря', callback_data='crypt_caesar')
    key_two = types.InlineKeyboardButton(text='Шифр AES', callback_data='crypt_aes')
    key_three = types.InlineKeyboardButton(text='Шифр Blowfish', callback_data='crypt_blowfish')
    key_four = types.InlineKeyboardButton(text='Шифр RSA', callback_data='crypt_rsa')
    keyboard.add(key_one, key_two, key_three, key_four)

    question = 'Выбери метод шифрования:'
    bot.send_message(chat_id, text=question, reply_markup=keyboard)

# Выводит выбор из различных шифрований
def ask_decrypt(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    key_one = types.InlineKeyboardButton(text='Шифр Цезаря', callback_data='decrypt_caesar')
    key_two = types.InlineKeyboardButton(text   ='Шифр AES', callback_data='decrypt_aes')
    key_three = types.InlineKeyboardButton(text='Шифр Blowfish', callback_data='decrypt_blowfish')
    key_four = types.InlineKeyboardButton(text='Шифр RSA', callback_data='decrypt_rsa')
    keyboard.add(key_one, key_two, key_three, key_four)

    question = 'Выбери метод дешифрования:'
    bot.send_message(chat_id, text=question, reply_markup=keyboard)

# Обработчики для каждого шифра

@bot.callback_query_handler(func=lambda call: call.data == 'crypt_caesar')
def crypt_caesar(call):
    bot.send_message(call.message.chat.id, 'Введите сдвиг для шифра Цезаря:')
    bot.register_next_step_handler(call.message, encrypt_caesar)

def encrypt_caesar(message):
    global shifr
    shift = int(message.text)  # Получаем сдвиг
    encrypted = caesar_cipher(shifr, shift)
    bot.send_message(message.from_user.id, f'Зашифрованный текст: {encrypted}')
    start(message)  # Запрашиваем новый текст для шифрования/дешифрования

@bot.callback_query_handler(func=lambda call: call.data == 'crypt_aes')
def crypt_aes(call):
    bot.send_message(call.message.chat.id, 'Введите ключ для шифрования:')
    bot.register_next_step_handler(call.message, encrypt_aes)

def encrypt_aes(message):
    global shifr
    key = message.text
    encrypted = simple_aes(shifr, key)
    bot.send_message(message.from_user.id, f'Зашифрованный текст: {encrypted}')
    start(message)  # Запрашиваем новый текст для шифрования/дешифрования

@bot.callback_query_handler(func=lambda call: call.data == 'crypt_blowfish')
def crypt_blowfish(call):
    bot.send_message(call.message.chat.id, 'Введите ключ для шифрования:')
    bot.register_next_step_handler(call.message, encrypt_blowfish)

def encrypt_blowfish(message):
    global shifr
    key = message.text
    encrypted = simple_blowfish(shifr, key)
    bot.send_message(message.from_user.id, f'Зашифрованный текст: {encrypted}')
    start(message)  # Запрашиваем новый текст для шифрования/дешифрования

@bot.callback_query_handler(func=lambda call: call.data == 'crypt_rsa')
def crypt_rsa(call):
    bot.send_message(call.message.chat.id, 'Введите ключ для шифрования:')
    bot.register_next_step_handler(call.message, encrypt_rsa)

def encrypt_rsa(message):
    global shifr
    public_key = message.text
    e = 65537  # Простой пример публичного ключа
    n = 3233  # Простое произведение для RSA
    encrypted = rsa_encrypt(shifr, e, n)
    bot.send_message(message.from_user.id, f'Зашифрованный текст: {encrypted}')
    start(message)  # Запрашиваем новый текст для шифрования/дешифрования

# Запуск бота
bot.polling(none_stop=True)
