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
def simple_aes(text, key):
    encrypted = ''
    for i in range(len(text)):
        encrypted += chr(ord(text[i]) ^ ord(key[i % len(key)]))  # XOR с ключом
    return encrypted

# Упрощенный Blowfish
def simple_blowfish(text, key):
    encrypted = ''
    for i in range(0, len(text), 8):
        block = text[i:i+8].ljust(8, '\0')
        encrypted_block = ''.join(chr(ord(block[j]) ^ ord(key[j % len(key)])) for j in range(8))
        encrypted += encrypted_block
    return encrypted

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

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Введи текст, который ты хочешь зашифровать или расшифровать.')
    bot.register_next_step_handler(message, ask)

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

def ask_crypt(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    key_one = types.InlineKeyboardButton(text='Шифр Цезаря', callback_data='crypt_caesar')
    key_two = types.InlineKeyboardButton(text='Шифр AES', callback_data='crypt_aes')
    key_three = types.InlineKeyboardButton(text='Шифр Blowfish', callback_data='crypt_blowfish')
    key_four = types.InlineKeyboardButton(text='Шифр RSA', callback_data='crypt_rsa')
    keyboard.add(key_one, key_two, key_three, key_four)

    question = 'Выбери метод шифрования:'
    bot.send_message(chat_id, text=question, reply_markup=keyboard)

def ask_decrypt(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    key_one = types.InlineKeyboardButton(text='Шифр Цезаря', callback_data='decrypt_caesar')
    key_two = types.InlineKeyboardButton(text='Шифр AES', callback_data='decrypt_aes')
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
    bot.send_message(call.message.chat.id, 'Введите публичный ключ для шифрования:')
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
