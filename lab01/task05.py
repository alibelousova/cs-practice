sc = int(input('Введите продолжительность в секундах:'))
k = sc // 60 // 60
l = (sc - k * 60 * 60)//60
s = (sc - k * 60 * 60)%60
print(k)
print(l)
print(s)
