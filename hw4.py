with open('text.txt', encoding='utf-8') as f:
    lines = f.readlines()
with open('text.txt', encoding='utf-8') as f:
    text = f.read()
lines = text.splitlines()

min = 2*10^5
max = -1
for i in lines:
    if len(i) < min:
        min = len(i)
for i in lines:
    if len(i) > max:
        max = len(i)

print('Самая короткая строка короче самой длинной в ', max/min, ' раз!')