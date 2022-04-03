# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""  
#height = int(input('Введите свой рост : \n в см' ))
#print(height)
#height = int(input('Введите свой рост : \n \t см' ))
#print(height)
print('Oдин',
'Два',
'Три',
sep='---')


heiGHT = int(input('Введите свой рост: \n'
                   'Вторая строка'))
print(heiGHT)
print("О\'Коннел")
print ( 'Пн\tВт\tCp')
print ( 'Чт\tПт\tСб')

print(format(12765.49876543,',.4f'))
print(format(12345.67894566,',.2f'))

monthly_pay = 30000.0
annual_pay = monthly_pay * 12
print('Baшa годовая заработная плата составляет\n$' ,
format(annual_pay, ',.2f'),
sep=' ~~~~~~')
print('Ваше число\n', format(12,'20.0f'), sep ='~~~~')
print(format(0.5,'.5%'))

print(format(123456,'d'))
"""
#your_color = int(input('Ваш любимый цвет?'))


#c = 5 / -2.5
#print(c)
#total = 10+14
#due = total - payment
#sales = 12.568765
#print(format(sales, '.2f') )
#number = 1234567.456
#print(format(number,',.1f'))
"""
import turtle
turtle.hideturtle()
turtle.pos()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.pos()
turtle.penup()
turtle.goto(-50,10)
turtle.pendown().
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.done
"""
"""
print('Возраст.....\n',
      'Имя.....\n',
       'Фамилия.....\n',
      'Телефон.....\n', 
      sep='......')
"""
"""
yearSALES = int(input('Введите итоговую сумму объема продаж'))
benefit = (yearSALES * 23)//100
print('Ваша прибыль состаляет  :\n \t ',format( benefit, ',.0f' ),'рублей')
"""
"""
listpay = []

while True:
    item =int(input('Введите стоимотсь товара'))
    listpay.append(item)
    request =  input('Выхотите продолжить?\n Нажмите Да или Нет')
    if request == 'Нет':
         break
    else:
         continue
summ = sum(listpay)
print('Сумма ваших покупок\n', summ, 'рубля')


nalog_sale = int((summ * 7)/100)
itogo = nalog_sale + summ
print('Итого с учетом налога Ваша покупка стоит  :\n', itogo, 'рублей' )

"""
"""
speed = 70
h1 = 2
h2 = 3
h3 = 4

s1 = speed * h1
s2 = speed * h2
s3 = speed * h3
print(s1,s2,s3)

buyer = int(input('Ведите величину покупки?'))
fed = buyer *0.05
reg = buyer * 0.025
itogo = fed + reg
print('Сумма ваших налогов составляем :', format(itogo, ',.3f' ), 'рубл')
print(format(itogo, ',.1f'))
"""
"""
bild = int(input('Введите стоимость за хавало в рублях'))
nalog = bild * 0.07
tip = bild * 0.18
itogo = tip + nalog + bild
print('Ваш счет :', itogo, 'рублей\n','НДС составляет :', format(nalog,'.0f')) 
print('Чаевые :' , int(tip),' в рублях')
"""
"""
celciy = float(input('Введите значение по шкале Цельсия'))
farengeit = (9*celciy)/5 + 32
print(float(farengeit))
"""
"""
cake_sugar = float(48/1.5)
cake_butter = float(48/1)
cake_floawer = float(48/2.75)
yours_cake = int(input('Сколько булок хочешь забубенить?'))
item1 = yours_cake * cake_butter
item2 = yours_cake * cake_floawer
item3 = yours_cake * cake_sugar

print('Вам нужно сахара', int(cake_sugar), 'Масла', int(cake_butter), 'Муки', int(cake_floawer))
"""
"""
r = int(input('Длинная гряды'))
e = int(input('Площадь опоры'))
s = int(input('Между лозами'))

v = (r-(2*e))/s
print(v)
"""
import turtle
turtle.title('Ромбы')
turtle.shape("turtle")
turtle.setup(600,600)
turtle.bgcolor('gray')
turtle.color('red', 'yellow')
turtle.begin_fill()

for i in range(4):
    turtle.left(45)
    turtle.forward(100)
    turtle.left(45)
    turtle.done
turtle.left(45)
turtle.forward(100)
turtle.end_fill()


turtle.color('red', 'yellow')
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
    turtle.done
turtle.end_fill()    
turtle.exitonclick()  


"""
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.left(90)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()
turtle.done
"""