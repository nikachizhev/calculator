#создаем словарь с операциями где указываем их приоретет
oper={'+':(1,lambda x,y:x+y),'-':(1,lambda x,y:x-y),'*':(2,lambda x,y:x*y),'/':(2,lambda x,y:x/y)}
stroka=input()
#чтобы не прочитать 90 как 9 и 0 создаем функцию которая отделяет числа от операций и скобок
def f(stroka):
    simbols=[]
    number=''
    for i in stroka:
        
        if i in '0123456789':
            number+=i
            
        elif number: #если i это не число добавляем number в наш массив и сбрасываем для будущих новых чисел
            simbols.append(number)
            number=''
        if i in oper or i in '()':
            simbols.append(i)
    simbols.append(number) #добавляем последнее собранное число
    return simbols

stack=[] #будем сохранять сюда операции и скобки
outpt=[] #сюда сохраняем числа и операции, если их не добавить в стек 
simbol=f(stroka) 

#проходим по полученному ранее массиву 
for i in simbol:
    if i in oper: #если наш элемент это операция, пока существует стек и текущая операция
        #имеет приоретет <= последенему эл-ту из стека удаляем из стека последний и добавляем
        # его в опн
        while stack and stack[-1]!='(' and oper[i][0]<=oper[stack[-1]][0]:
            outpt.append(stack.pop())
        #после завершения цикла добавляем текущий в стек
        stack.append(i)
    elif i==')':
        #удаляем из стека последний элемент пока не наткнемся на отк-ю скобку, удаленные эл-ты добав в опн
        while stack:
            dg=stack.pop()
            if dg=='(':
                break
            outpt.append(dg)
    elif i=='(':
        stack.append('(')
    else: #добавляем в опн тк это число 
        outpt.append(i)
while stack: #проверяем что все элементы из стека теперь в опн, если нет то добавляем 
    outpt.append(stack.pop())


pol=[]
for i in outpt: #outpt это получившеяся опн только в массиве 
    if i in oper:
        y,x=pol.pop(),pol.pop()
        pol.append(oper[i][1](x,y))
    else:
        pol.append(int(i))
print(pol[0])




     