n = int(input())

m = n % 60
if n <= 1440:
    h = n //60
    m = n % 60
elif n > 1440:
    n = 1440
    h = n //60
    m = n % 60
print(h,m)
