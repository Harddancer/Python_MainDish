"""
Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов в диапазоне от 0 до 23, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд. Количество минут и секунд при необходимости дополняются до двузначного числа нулями.

Программа получает на вход число n - количество секунд, которое прошло с начала суток.

Выведите показания часов, соблюдая формат
"""

N = int(input())
n = N % (3600 * 24)
h = n // 3600
m = n % 3600 // 60
s = n % 60
print(h, ':', m // 10, (m % 10), ':', s // 10, s % 10, sep='')