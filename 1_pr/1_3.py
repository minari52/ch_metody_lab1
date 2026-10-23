import numpy as np
import matplotlib.pyplot as plt
import math

# =========================================================
# УРАВНЕНИЯ И ПРОИЗВОДНЫЕ
# =========================================================

# Уравнение А: 3*lg(x) - 0.5*x + 1 = 0
# ОДЗ: x > 0
def f_a(x):
    return 3 * math.log10(x) - 0.5 * x + 1

def df_a(x):
    return 3 / (x * math.log(10)) - 0.5

# Уравнение Б: x^3 - 4x^2 - 4x - 8 = 0
def f_b(x):
    return x**3 - 4*x**2 - 4*x - 8

def df_b(x):
    return 3*x**2 - 8*x - 4

# Уравнение В: x^3 - 2x^2 - 8 = 0
def f_c(x):
    return x**3 - 2*x**2 - 8

def df_c(x):
    return 3*x**2 - 4*x


# =========================================================
# МЕТОДЫ УТОЧНЕНИЯ
# =========================================================

def chord_method(f, a, b, tol=0.001):
    """Метод хорд"""
    if f(a) * f(b) > 0:
        raise ValueError("На концах интервала функция должна иметь разные знаки!")
    
    iter_count = 0
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        iter_count += 1
        
        if abs(f(c)) < tol:
            return c, iter_count
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

def tangent_method(f, df, x0, tol=0.001, max_iter=100):
    """Метод касательных (Ньютона)"""
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Производная равна нулю, метод не сработает")
        
        x_next = x - fx / dfx
        
        if abs(x_next - x) < tol:
            return x_next, i + 1
        x = x_next
    return x, max_iter

def combined_method(f, df, a, b, tol=0.001):
    """Комбинированный метод (Хорд + Касательных)"""
    iter_count = 0
    while abs(b - a) > tol:
        if f(b) * df(b) > 0:
            b_new = b - f(b) / df(b)
            a_new = a - f(a) * (b - a) / (f(b) - f(a))
        else:
            a_new = a - f(a) / df(a)
            b_new = b - f(b) * (b - a) / (f(b) - f(a))
        
        a, b = a_new, b_new
        iter_count += 1
        
        if iter_count > 100:
            break
            
    return (a + b) / 2, iter_count


# =========================================================
# ОТДЕЛЕНИЕ КОРНЕЙ (Чистый вывод без np.float64)
# =========================================================

def isolate_roots(f, start, end, step=0.1):
    """Ищет интервалы смены знака, возвращает красивые кортежи float"""
    intervals = []
    x_vals = np.arange(start, end, step)
    
    for i in range(len(x_vals) - 1):
        x1 = round(float(x_vals[i]), 2)
        x2 = round(float(x_vals[i+1]), 2)
        
        try:
            y1, y2 = f(x1), f(x2)
            if y1 * y2 < 0:
                intervals.append((x1, x2))
        except ValueError:
            continue
            
    return intervals


# =========================================================
# РЕШЕНИЕ И ВЫВОД
# =========================================================

print("="*50)
print("ЗАДАНИЕ 3: Отделение и уточнение корней")
print("="*50)

# --- А) Метод Хорд ---
print("\n[А] 3*lg(x) - 0.5*x + 1 = 0  (Метод хорд)")
intervals_a = isolate_roots(f_a, 0.1, 10)
print(f"Интервалы отделения: {intervals_a}")

# У этого уравнения ДВА корня, найдем оба
for idx, (a, b) in enumerate(intervals_a, 1):
    root_a, iters_a = chord_method(f_a, a, b, tol=0.001)
    print(f"  Корень #{idx} на [{a}, {b}]:")
    print(f"    x ≈ {root_a:.4f}  |  итераций: {iters_a}  |  f(x) = {f_a(root_a):.6f}")

# --- Б) Метод Касательных ---
print("\n[Б] x^3 - 4x^2 - 4x - 8 = 0  (Метод касательных)")
intervals_b = isolate_roots(f_b, -5, 10)
print(f"Интервалы отделения: {intervals_b}")

if intervals_b:
    a, b = intervals_b[0]
    # Выбираем начальную точку: тот край, где f(x) и f''(x) одного знака
    x0 = b if abs(df_b(b)) > abs(df_b(a)) else a
    root_b, iters_b = tangent_method(f_b, df_b, x0, tol=0.001)
    print(f"  Корень на [{a}, {b}]:")
    print(f"    x ≈ {root_b:.4f}  |  итераций: {iters_b}  |  f(x) = {f_b(root_b):.6f}")

# --- В) Комбинированный метод ---
print("\n[В] x^3 - 2x^2 - 8 = 0  (Комбинированный метод)")
intervals_c = isolate_roots(f_c, -5, 10)
print(f"Интервалы отделения: {intervals_c}")

if intervals_c:
    a, b = intervals_c[0]
    root_c, iters_c = combined_method(f_c, df_c, a, b, tol=0.001)
    print(f"  Корень на [{a}, {b}]:")
    print(f"    x ≈ {root_c:.4f}  |  итераций: {iters_c}  |  f(x) = {f_c(root_c):.6f}")


# =========================================================
# ГРАФИКИ
# =========================================================

print("\nСтроим графики...")
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# График А
x_vals_a = np.linspace(0.1, 10, 400)
y_vals_a = [f_a(x) for x in x_vals_a]
ax1.plot(x_vals_a, y_vals_a, color='blue')
ax1.axhline(0, color='black')
ax1.set_title("А) 3*lg(x) - 0.5*x + 1")
ax1.grid(True)

# График Б
x_vals_b = np.linspace(-3, 7, 400)
ax2.plot(x_vals_b, f_b(x_vals_b), color='green')
ax2.axhline(0, color='black')
ax2.set_title("Б) x^3 - 4x^2 - 4x - 8")
ax2.grid(True)

# График В
x_vals_c = np.linspace(-3, 5, 400)
ax3.plot(x_vals_c, f_c(x_vals_c), color='red')
ax3.axhline(0, color='black')
ax3.set_title("В) x^3 - 2x^2 - 8")
ax3.grid(True)

plt.tight_layout()
plt.show()