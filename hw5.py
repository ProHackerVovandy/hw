word = ' '
string = ''
while word != '':
    word = input()
    if len(word) > 5:
        string = string + word + '\n'

with open('text.txt', "w", encoding="utf-8") as f:
    f.write(string)

print('Запись завершена!')