a = float(input())
b = float(input())
c = float(input())

n = 0

if a % b == c:
    n = n + 1
if a*c + b == 0:
    n = n + 1
if n == 2:
    print("YES")
else:
    print("NO")


#Второй вариант - 2-й — (3) и (4); 3 - (a даёт остаток c при делении на b), 4 - (c является решением линейного уравнения ax + b = 0)
#int - integer - целые
#float - рациональные
#bool - булевые(1,0)(True, False)
#char - символ
#string - строка
#массив
