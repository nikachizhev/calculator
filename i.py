#создаем словарь с операциями где указываем их приоретет
operations={'+':(1, lambda x, y: x + y),
            '-':(1, lambda x, y: x - y),
            '*':(2, lambda x, y: x * y),
            '/':(2, lambda x, y: x / y)}
string=input()


#чтобы не прочитать 90 как 9 и 0 создаем функцию которая отделяет числа от операций и скобок
def separate_elements(string):
    simbols=[]
    number=''
    for element in string:
        if element in ' ':
            continue
        
        if element in '0123456789':
            number+=element
            
        elif number: #если i это не число добавляем number в наш массив и сбрасываем для будущих новых чисел
            simbols.append(number)
            number=''
        if element in operations or element in '()':
            simbols.append(element)
    if number:
        simbols.append(number) #добавляем последнее собранное число
    return simbols

stack=[] #будем сохранять сюда операции и скобки
out_put=[] #сюда сохраняем числа и операции, если их не добавить в стек
simbol_list= separate_elements(string)

#проходим по полученному ранее массиву 
for element in simbol_list:
    if element in operations: #если наш элемент это операция, пока существует стек и текущая операция
        #имеет приоретет <= последенему эл-ту из стека удаляем из стека последний и добавляем
        # его в опн
        while stack and stack[-1]!='(' and operations[element][0]<=operations[stack[-1]][0]:
            out_put.append(stack.pop())
        #после завершения цикла добавляем текущий в стек
        stack.append(element)
    elif element==')':
        #удаляем из стека последний элемент пока не наткнемся на отк-ю скобку, удаленные эл-ты добав в опн
        while stack:
            dg=stack.pop()
            if dg=='(':
                break
            out_put.append(dg)
    elif element=='(':
        stack.append('(')
    else: #добавляем в опн тк это число 
        out_put.append(element)


while stack: #проверяем что все элементы из стека теперь в опн, если нет то добавляем 
    out_put.append(stack.pop())


reverse_Polish_notation=[]
for element in out_put: #outpt это получившеяся опн только в массиве
    if element in operations:
        y= reverse_Polish_notation.pop()
        x= reverse_Polish_notation.pop()
        reverse_Polish_notation.append(operations[element][1](x, y))
    else:
        reverse_Polish_notation.append(int(element))
print(reverse_Polish_notation[0])




     