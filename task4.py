# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file_1.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('file_1.txt', 'r') as file:
    text = file.readline()
    text_compression = text.split()

enconding = ''
prev_char = ''
count = 1
for char in text:
    if char != prev_char:
        if prev_char:
            enconding += str(count) + prev_char
        count = 1
        prev_char = char
    else:
        count += 1
else:
    enconding += str(count) + prev_char
    
print(text)
print(enconding)
with open('file_2.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{enconding}')


input('Для востонавления текста нажмите Enter')

with open('file_2.txt', 'r', encoding='utf_8') as file:
    text = file.read()

number = ''
text_return = ''
for i in text:
    if i.isdigit():
        number = number + i
    else:
        text_return += int(number)*i
        number = ''

print(f'Востановленный текст представляет последовательность:\n{text_return}')

with open('file_1.txt', 'w', encoding='utf_8') as file:
    file.write(text_return)