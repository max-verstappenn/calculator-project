# Простой калькулятор
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

# Основная программа
print("Простой калькулятор")
print("Доступные операции: +, -, *, /")
def power(a, b):
    return a ** b

def square_root(a):
    return a ** 0.5

print("Улучшенный калькулятор")
print("Доступные операции: +, -, *, /, ^, sqrt")