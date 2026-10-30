def check_diagonal(A):
    n = len(A)
    is_diag_dominant = True
    print("\n--- Проверка условия сходимости (преобладание диагонали) ---")
    for i in range(n):
        diag = abs(A[i][i])
        sum_other = sum(abs(A[i][j]) for j in range(n) if j != i)
        status = "ОК" if diag > sum_other else "НЕ ВЫПОЛНЕНО"
        if diag <= sum_other:
            is_diag_dominant = False
        print(f"Строка {i+1}: |A{i+1}{i+1}| = {diag:.2f} | Сумма остальных = {sum_other:.2f} -> {status}")
    
    if is_diag_dominant:
        print("Условие выполняется! Метод итераций сойдется.")
    else:
        print("ВНИМАНИЕ: Условие диагонали НЕ выполнено. Метод может не сойтись.")
    return is_diag_dominant

def simple_iteration_4x4(A, B, eps=0.0001, max_iter=1000):
    n = len(A)
    check_diagonal(A)
    
    x = [0.0] * n
    print(f"\nНачальное приближение: {x}")
    print(f"{'Итерация':<10} | {'x1':<8} | {'x2':<8} | {'x3':<8} | {'x4':<8} | {'Макс. разница':<15}")
    print("-" * 75)
    
    for k in range(max_iter):
        x_new = [0.0] * n
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (B[i] - s) / A[i][i]
        
        diff = max(abs(x_new[i] - x[i]) for i in range(n))
        
        print(f"{k+1:<10} | {x_new[0]:<8.4f} | {x_new[1]:<8.4f} | {x_new[2]:<8.4f} | {x_new[3]:<8.4f} | {diff:<15.6f}")
        
        if diff < eps:
            print(f"\nСошлось за {k+1} итераций!")
            return x_new
        x = x_new.copy()
    
    print("\nДостигнуто максимальное количество итераций.")
    return x

# --- ДАННЫЕ ТВОЕГО ВАРИАНТА 120 ---
A = [
    [4.5, -1.0, 0.6, 0.9],
    [0.8, 5.0, -1.2, -0.7],
    [-1.1, 0.9, 4.0, 1.3],
    [0.7, -1.4, 0.8, -5.5]
]
B = [8.5, 10.7, 14.6, -15.8]

eps = 0.0001 # Точность

result = simple_iteration_4x4(A, B, eps)
print("\nИтоговый ответ (Приближенный):")
for i, val in enumerate(result):
    print(f"x{i+1} = {val:.5f}")