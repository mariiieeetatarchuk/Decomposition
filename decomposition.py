# функція, яка обчислює суму чисел
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# функція, яка обчислює середнє значення
def average_list(numbers):
    total = sum_list(numbers)
    count = len(numbers)
    avg = total / count
    return avg

# список чисел для обробки
numbers = [2, 4, 6, 8, 10]

# виклик функції для обчислення середнього значення
result = average_list(numbers)

# виведення результату
print("Середнє значення:", result)
