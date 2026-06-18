import math
print('(a + b) / (c - d) + math.sqrt(f)')
def func(a,b,c,d,f):
    return (a + b) / (c - d) + math.sqrt(f)


def err(a,b,c,d,f):
    try:
        return func(a,b,c,d,f)
    except(ZeroDivisionError):
        return"Деление на ноль запрещено (c не равно d)"
    except(ValueError):
        return "Вычисление корня из отрицательного числа запрещено (f >= 0)"
    except(TypeError):
        return "Неверный тип данных"
        
err(52,42,69,67,169)

