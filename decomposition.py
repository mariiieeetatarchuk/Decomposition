from typing import List, Tuple
from functools import cmp_to_key

# Порівняння точок за кутом відносно точки p0
def compare_points(p0: Tuple[int, int], p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
    x2, y2 = p2[0] - p0[0], p2[1] - p0[1]
    cross = x1 * y2 - x2 * y1
    dot = x1 * x2 + y1 * y2
    angle1 = -1 if cross > 0 else 1 if cross < 0 else 0
    angle2 = -1 if dot < 0 else 1 if dot > 0 else 0
    if angle1 == angle2:
        return 0
    elif angle1 < angle2:
        return -1
    else:
        return 1

# Знаходження точки з найменшою координатою y
def find_lowest_point(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    return min(points, key=lambda p: (p[1], p[0]))

# Обчислення опуклої оболонки методом декомпозиції
def convex_hull(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if len(points) < 3:
        return points
    p0 = find_lowest_point(points)
    sorted_points = sorted(points, key=cmp_to_key(lambda p1, p2: compare_points(p0, p1, p2)))
    stack = [p0, sorted_points[1]]
    for i in range(2, len(sorted_points)):
        while len(stack) > 1 and compare_points(stack[-2], stack[-1], sorted_points[i]) < 1:
            stack.pop()
        stack.append(sorted_points[i])
    return stack

# Приклад використання
points = [(0, 0), (0, 3), (2, 0), (5, 1), (1, 0.5), (0, 1.5), (2, 0.5), (2, 1.5)]
convex_hull_points = convex_hull(points)
print(convex_hull_points)
