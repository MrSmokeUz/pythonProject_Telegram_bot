import telebot
from telebot import types

# Укажите действительный токен вашего бота
bot = telebot.TeleBot('7565080323:AAGFgMxAvQrehCJG1unhKtXLoijGet_m1iM')

# Глобальная переменная для хранения текста пользователя
shifr = ''

# Шифр Цезаря
def caesar_cipher(text, shift, decrypt=False):
    """
    Функция для шифрования и дешифрования с помощью шифра Цезаря.
    :param text: Исходный текст
    :param shift: Сдвиг для шифрования
    :param decrypt: True, если нужно расшифровать
    :return: Зашифрованный/расшифрованный текст
    """
    if decrypt:
        shift = -shift  # Для дешифрования сдвиг в обратную сторону
    encrypted = ''
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted += char
    return encrypted

# Упрощенный AES
def simple_aes(text, key):
    """
    XOR-шифрование, имитирующее упрощенный AES.
    :param text: Исходный текст
    :param key: Ключ для шифрования/дешифрования
    :return: Зашифрованный текст
    """
    encrypted = ''
    for i in range(len(text)):
        encrypted += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted

# Упрощенный Blowfish
def simple_blowfish(text, key):
    """
    Шифрование блоками длиной 8 символов с использованием XOR.
    :param text: Исходный текст
    :param key: Ключ
    :return: Зашифрованный текст
    """
    encrypted = ''
    for i in range(0, len(text), 8):
        block = text[i:i+8].ljust(8, '\0')
        encrypted_block = ''.join(chr(ord(block[j]) ^ ord(key[j % len(key)])) for j in range(8))
        encrypted += encrypted_block
    return encrypted

# Упрощенный RSA
def rsa_encrypt(text, e, n):
    """
    Упрощенное RSA-шифрование.
    :param text: Исходный текст
    :param e: Публичная экспонента
    :param n: Модуль
    :return: Зашифрованный текст
    """
    encrypted = ''
    for char in text:
        encrypted += chr(pow(ord(char), e, n))
    return encrypted

def rsa_decrypt(encrypted_text, d, n):
    """
    Упрощенное RSA-дешифрование.
    :param encrypted_text: Зашифрованный текст
    :param d: Приватная экспонента
    :param n: Модуль
    :return: Расшифрованный текст
    """
    decrypted = ''
    for char in encrypted_text:
        decrypted += chr(pow(ord(char), d, n))
    return decrypted

# Стартовая команда
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Введи текст, который ты хочешь зашифровать или расшифровать.')
    bot.register_next_step_handler(message, ask)

# Выбор действия (зашифровать/расшифровать)
def ask(message):
    global shifr
    shifr = message.text  # Сохраняем текст пользователя
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Зашифровать', callback_data='crypt')
    key_no = types.InlineKeyboardButton(text='Расшифровать', callback_data='decrypt')
    keyboard.add(key_yes, key_no)
    bot.send_message(message.from_user.id, 'Что ты хочешь сделать?', reply_markup=keyboard)

# Обработка кнопки "Зашифровать"
@bot.callback_query_handler(func=lambda call: call.data == "crypt")
def crypt_handler(call):
    ask_crypt(call.message.chat.id)

# Обработка кнопки "Расшифровать"
@bot.callback_query_handler(func=lambda call: call.data == "decrypt")
def decrypt_handler(call):
    ask_decrypt(call.message.chat.id)

# Выбор метода шифрования
def ask_crypt(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    key_caesar = types.InlineKeyboardButton(text='Шифр Цезаря', callback_data='crypt_caesar')
    key_aes = types.InlineKeyboardButton(text='Шифр AES', callback_data='crypt_aes')
    key_blowfish = types.InlineKeyboardButton(text='Шифр Blowfish', callback_data='crypt_blowfish')
    key_rsa = types.InlineKeyboardButton(text='Шифр RSA', callback_data='crypt_rsa')
    keyboard.add(key_caesar, key_aes, key_blowfish, key_rsa)
    bot.send_message(chat_id, 'Выбери метод шифрования:', reply_markup=keyboard)

# Выбор метода дешифрования
def ask_decrypt(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    key_caesar = types.InlineKeyboardButton(text='Шифр Цезаря', callback_data='decrypt_caesar')
    key_aes = types.InlineKeyboardButton(text='Шифр AES', callback_data='decrypt_aes')
    key_blowfish = types.InlineKeyboardButton(text='Шифр Blowfish', callback_data='decrypt_blowfish')
    key_rsa = types.InlineKeyboardButton(text='Шифр RSA', callback_data='decrypt_rsa')
    keyboard.add(key_caesar, key_aes, key_blowfish, key_rsa)
    bot.send_message(chat_id, 'Выбери метод дешифрования:', reply_markup=keyboard)

# Шифрование/дешифрование для каждого метода (Цезарь, AES, Blowfish, RSA)
@bot.callback_query_handler(func=lambda call: call.data.startswith('crypt_') or call.data.startswith('decrypt_'))
def process_crypt_decrypt(call):
    global shifr
    operation, method = call.data.split('_')
    if method == 'caesar':
        bot.send_message(call.message.chat.id, 'Введите сдвиг:')
        bot.register_next_step_handler(call.message, lambda msg: process_caesar(msg, operation == 'crypt'))
    elif method == 'aes' or method == 'blowfish':
        bot.send_message(call.message.chat.id, 'Введите ключ:')
        bot.register_next_step_handler(call.message, lambda msg: process_aes_blowfish(msg, method, operation == 'crypt'))
    elif method == 'rsa':
        bot.send_message(call.message.chat.id, 'Введите ключи (e,n) для шифрования или (d,n) для дешифрования через пробел:')
        bot.register_next_step_handler(call.message, lambda msg: process_rsa(msg, operation == 'crypt'))

def process_caesar(message, encrypt):
    global shifr
    try:
        shift = int(message.text)
        result = caesar_cipher(shifr, shift, not encrypt)
        bot.send_message(message.from_user.id, f'Результат: {result}')
    except ValueError:
        bot.send_message(message.from_user.id, 'Ошибка: введите число!')
    start(message)

def process_aes_blowfish(message, method, encrypt):
    global shifr
    key = message.text
    cipher_func = simple_aes if method == 'aes' else simple_blowfish
    result = cipher_func(shifr, key)
    bot.send_message(message.from_user.id, f'Результат: {result}')
    start(message)

def process_rsa(message, encrypt):
    global shifr
    try:
        keys = message.text.split(',')
        key1, n = map(int, keys)
        if encrypt:
            result = rsa_encrypt(shifr, key1, n)
        else:
            result = rsa_decrypt(shifr, key1, n)
        bot.send_message(message.from_user.id, f'Результат: {result}')
    except ValueError:
        bot.send_message(message.from_user.id, 'Ошибка: введите ключи в формате "число,число"!')
    start(message)

# Запуск бота
bot.polling(none_stop=True)


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# Пример использования
text = "Hello, World!"
shift = 3
encrypted = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted)

decrypted = caesar_cipher(encrypted, -shift)
print("Расшифрованный текст:", decrypted)
