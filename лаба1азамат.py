import math

# 1. Запрашиваем у пользователя угол альфа в градусах
alpha_deg = float(input("Введите значение угла альфа (в градусах): "))

# 2. Переводим градусы в радианы, так как math работает с радианами
alpha = math.radians(alpha_deg)

# 3. Вычисление по первой формуле
z1 = (
    math.cos(alpha)
    + math.sin(alpha)
    + math.cos(3 * alpha)
    + math.sin(3 * alpha)
)

# 4. Вычисление по второй формуле
z2 = 2 * math.sqrt(2) * math.cos(alpha) * math.sin(math.pi / 4 + 2 * alpha)

# 5. Вывод результатов в консоль PyCharm
print(f"Результат z1 = {z1:.6f}")
print(f"Результат z2 = {z2:.6f}")
print("Результаты совпадают!" if math.isclose(z1, z2, abs_tol=1e-5) else "Ошибка!")