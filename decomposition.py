import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def orientation(p, q, r):
    """
    Функція, яка визначає орієнтацію точок p, q, r
    Використовується формула векторного добутку
    """
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0 # точки лежать на одній прямій
    elif val > 0:
        return 1 # за годинниковою стрілкою
    else:
        return 2 # проти годинникової стрілки

def convex_hull(points):
    """
    Функція, яка реалізує алгоритм обчислення опуклої оболонки методом декомпозиції
    """
    # Перевірка, чи кількість точок достатня для обчислення опуклої оболонки
    if len(points) < 3:
        return []

    hull = []

    # Знаходимо точку з найменшою x-координатою
    min_x = points[0].x
    min_idx = 0
    for i in range(1, len(points)):
        if points[i].x < min_x or (points[i].x == min_x and points[i].y < points[min_idx].y):
            min_x = points[i].x
            min_idx = i

    p = min_idx
    q = 0

    while True:
        hull.append(points[p])
        q = (p + 1) % len(points)

        for i in range(len(points)):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == min_idx:
            break

    return hull

# Приклад використання

# Задаємо координати точок
points = [
    Point(0, 0),
    Point(1, 1),
    Point(2, 2),
    Point(0, 3),
    Point(3, 0),
    Point(2, 4),
    Point(4, 2)
]

# Обчислюємо опуклу оболонку
hull = convex_hull(points)

# Виводимо результат
print("Опукла оболонка:")
for point in hull:
    print("({}, {})".format(point.x, point.y))
