import random

n = int(input('Степень'))
x = ''
for k in range(n, 0, -1):
    x += f'{random.randint(0, 100)}*x**{k + 1} + {random.randint(0, 100)}*x**{k}'
x += '= 0'
print(x)
# data = open('file.txt', 'a')
# data.writelines(x)
# data.close()
m = int(input('Степень'))
y = ''
for s in range(m, 0, -1):
    y += f'{random.randint(0, 100)}*x**{s + 1} + {random.randint(0, 100)}*x**{s}'
y += '= 0'
print(y)
# date = open('file2.txt', 'a')
# date.writelines(y)
# date.close()
summa = x + y
print(summa)
date = open('file3.txt', 'a')
date.writelines(summa)
date.close()