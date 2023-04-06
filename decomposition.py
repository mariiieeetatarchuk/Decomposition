import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def partition(points, low, high):
    pivot = points[high]
    i = low - 1
    for j in range(low, high):
        if (points[j].x < pivot.x) or (points[j].x == pivot.x and points[j].y < pivot.y):
            i += 1
            points[i], points[j] = points[j], points[i]
    points[i + 1], points[high] = points[high], points[i + 1]
    return i + 1

def quicksort(points, low, high):
    if low < high:
        pivot_index = partition(points, low, high)
        quicksort(points, low, pivot_index - 1)
        quicksort(points, pivot_index + 1, high)

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def convex_hull(points):
    n = len(points)
    if n < 3:
        return points

    hull = []

    l = 0
    for i in range(1, n):
        if points[i].x < points[l].x or (points[i].x == points[l].x and points[i].y < points[l].y):
            l = i

    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n

        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == l:
            break

    return hull

# Генеруємо випадкові точки на площині
points = [Point(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(10)]

print("Початкові точки:")
for point in points:
    print("({}, {})".format(point.x, point.y))

# Сортуємо точки за кутовим порядком використовуючи QuickSort
quicksort(points, 0, len(points) - 1)

print("Відсортовані точки:")
for point in points:
    print("({}, {})".format(point.x, point.y))

# Обчислюємо опуклу оболонку
convex_points = convex_hull(points)

print("Точки опуклої оболонки:")
for point in convex_points:
    print("({}, {})".format(point.x, point.y))
