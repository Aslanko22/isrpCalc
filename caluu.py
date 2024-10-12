def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

def get_operation():
    operations = {
        '1': 'Сложение',
        '2': 'Вычитание',
        '3': 'Умножение',
        '4': 'Деление',
        '5': 'Возведение в степень',
        '6': 'Извлечение корня'
    }
    
    print("Выберите операцию:")
    for key, value in operations.items():
        print(f"{key}: {value}")
    
    while True:
        choice = input("Введите номер операции (1-6): ")
        if choice in operations:
            return choice
        else:
            print("Некорректный выбор. Пожалуйста, выберите операцию от 1 до 6.")

def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 == 0:
            return "Ошибка: Деление на ноль!"
        return num1 / num2
    elif operation == '5':
        return num1 ** num2  # Возведение в степень
    elif operation == '6':
        if num1 < 0 and num2 % 2 == 0:
            return "Ошибка: Невозможно извлечь корень из отрицательного числа!"
        return num1 ** (1/num2)  # Извлечение корня

def main():
    while True:
        num1 = get_number("Введите первое число: ")
        num2 = get_number("Введите второе число: ")
        operation = get_operation()
        
        result = calculate(num1, num2, operation)
        print(f"Результат: {result}")
        
        repeat = input("Хотите выполнить еще одну операцию? (да/нет): ").strip().lower()
        if repeat != 'да':
            print("Выход из программы.")
            break

if __name__ == "__main__":
    main()
