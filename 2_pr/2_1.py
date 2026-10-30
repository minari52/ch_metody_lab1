def get_determinant(matrix):
    """Универсальная функция для вычисления определителя матрицы (метод разложения)"""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for i in range(n):
        # Формируем минор (вычеркиваем первую строку и i-й столбец)
        sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        # Знакочередующаяся сумма: (+ - + -) * элемент * определитель минора
        det += ((-1) ** i) * matrix[0][i] * get_determinant(sub_matrix)
    return det

def solve_kramer_4x4(A, B):
    print("\n=== РЕШЕНИЕ СЛУ МЕТОДОМ КРАМЕРА (4x4) ===")
    delta = get_determinant(A)
    print(f"Главный определитель (Δ) = {delta}")
    
    if delta == 0:
        print("Ошибка: Главный определитель равен нулю! Метод Крамера не применим.")
        return

    n = len(A)
    x = []
    for i in range(n):
        # Создаем копию матрицы A и заменяем i-й столбец на B
        A_i = [row[:] for row in A]
        for j in range(n):
            A_i[j][i] = B[j]
        
        delta_i = get_determinant(A_i)
        print(f"Определитель Δ{i+1} = {delta_i}")
        x_i = delta_i / delta
        x.append(x_i)
        
    print("\nКорни системы (Точный ответ):")
    for i, val in enumerate(x):
        print(f"x{i+1} = {val:.6f}")

# --- ДАННЫЕ ТВОЕГО ВАРИАНТА 120 ---
A = [
    [4.5, -1.0, 0.6, 0.9],
    [0.8, 5.0, -1.2, -0.7],
    [-1.1, 0.9, 4.0, 1.3],
    [0.7, -1.4, 0.8, -5.5]
]
B = [8.5, 10.7, 14.6, -15.8]

solve_kramer_4x4(A, B)