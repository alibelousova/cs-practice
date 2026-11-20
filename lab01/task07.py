n = int(input('Введите четырёхзначное число:'))
n1 = n // 1000
n2 = n // 100 % 10
n3 = n % 100 // 10
n4 = n % 10
sum = n1 + n2 + n3 + n4
obr = n4 * 1000 + n3 * 100 + n2 * 10 + n1
print(n1)
print(n2)
print(n3)
print(n4)
print(sum)
print(obr)
