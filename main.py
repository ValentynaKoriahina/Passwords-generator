import random

digits = '123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

password_amount = int(input('Сколько паролей надо сгенерировать? '))

password_lenth = int(input('Какая длинна должна быть у пароля? '))

including_digits = input('Включать ли цифры? + - ')
if including_digits == '+':
    chars += digits

including_uppercases = input('Включать ли прописные буквы? + - ')
if including_uppercases == '+':
    chars += uppercase_letters

including_lowercases = input('Включать ли строчные буквы? + - ')
if including_lowercases == '+':
    chars += lowercase_letters

including_symbols = input('Включать ли символы !#$%&*+-=?@^_? + - ')
if including_symbols == '+':
    chars += punctuation

excluding_undefined_characters = input('Включать ли неоднозначные символы il1Lo0O? + - ')
if including_symbols == '+':
    for i in chars:
        if i in ['i','l','1','L','o','0','O']:
            chars = chars.replace(i, '')

def generate_password(length, chars):
    password = random.sample(chars, length)
    return ''.join(password)
    
passwords = []
    
for i in range(password_amount):
    passwords.append(generate_password(password_lenth, chars))
    
print('Вот результат:')
    
print(passwords)
