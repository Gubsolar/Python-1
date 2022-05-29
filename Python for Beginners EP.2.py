print(hello world)
name = 'prame'
money = 300000
bank = 3400000.25
print(name + str(money))
print(name, type(name))
print(bank, type(bank))
print(money, type(money))
deck = 'prame'
print(deck)
mymoney = '20'
print(type(mymoney))
print('prame' + mymoney)
print(name + ' มีเงินในกระเป๋า ' + str(money) + ' บาท ' + 'มีเงินในบัญชี ' + str(bank) + ' บาท')
print('{} มีเงินในกระเป๋า {:,d} บาท มีเงินในบัญชี {:,.3f} บาท'.format(name,money,bank))
print(f'{name} มีเงินในกระเป๋า {money:,d} บาท มีเงินในบัญชี {bank:,.0f} บาท')
print('%s มีเงินในกระเป๋า %d บาท มีเงินในบัญชี %.2f บาท'%(name,money,bank))
import turtle
tao = turtle.Turtle()
tao.shape('turtle')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.reset()
tao.goto(200,200)
tao.pensize(2)
tao.forward(50)
tao.pensize(4)
tao.reset()
tao.pensize(4)
tao.home()
tao.clear()
for i in range(5):
    print('hello',i)
list (range(5))
for i in [20,30,40,50]:
    print(i)
for i in ['somchai','somsak','sompong']:
    print(i)
for student in ['somchai','somsak','sompong']:
    print(student)
for i in range(4):
    tao.forward(100)
    tao.left(90)
    print('เต่าเดินครังที่',i)
tao.clear()
color = ['red','blue','yellow','green']
type(color)
for c in color:
    print(c)
    tao.color(c)
    tao.forward(100)
    tao.left(90)
tao.clear()
import random
random.choice(color)
color = ['red','blue','yellow','green']
random.choice(color)
random.choice(color)
random.choice(color)
random.choice(color)
for i in range(1,11):
    c = random.choice(color)
    tao.color(c)
    tao.circle(50)
    tao.left(36)
    print('หมุนครังที่',i)
for i in range(1,11):
    c = random.choice(color)
    tao.color(c)
    r = random.randint(50,100)
    print('สุ่มได้รัสมี:',r)
    tao.circle(r)
    tao.left(36)
    print('หมุนครังที่',i)
tao.reset()
for i in range(10):
    c = random.choice(color)
    tao.color(c)
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
    s = random.randint(0,200)
    for i in range(4):
        tao.forward(s)
        tao.left(90)