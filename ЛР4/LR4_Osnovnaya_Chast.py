import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

# =====================================================================
# ЧАСТЬ 1: ИСХОДНЫЙ КОД (БЕЗ ИЗМЕНЕНИЙ)
# =====================================================================

# Исходные данные
y = np.array([107.3, 106.6, 104.9, 103.4, 97.9, 96.4, 95.5, 93.9, 91.2, 88.9, 
              86.9, 85.1, 83.3, 80.8, 78.5, 75.5, 73.7, 72.1, 71.4, 70.3, 
              70.5, 69.9, 68.4, 68.1])
n = len(y)
t = np.arange(1, n+1)
years = np.arange(2000, 2024)

print("--- 1.7 Метод Ирвина ---")
sigma_y = np.std(y, ddof=1)
lambda_t = np.abs(np.diff(y)) / sigma_y
print(f"Максимальное значение lambda: {np.max(lambda_t):.3f} (критическое ~1.33)")

print("\n--- 1.8 Критерий Фостера-Стюарта ---")
p_count, q_count = 0, 0
max_y, min_y = y[0], y[0]
for i in range(1, n):
    if y[i] > max_y:
        p_count += 1
        max_y = y[i]
    elif y[i] < min_y:
        q_count += 1
        min_y = y[i]
S = p_count + q_count
d = p_count - q_count
# Табличные значения для n=24
mu_S, sigma_S = 5.55, 1.81 
mu_d, sigma_d = 0, 2.31
t1 = (S - mu_S) / sigma_S
t2 = (d - mu_d) / sigma_d
print(f"S = {S}, d = {d}")
print(f"t1 = {t1:.2f}, t2 = {t2:.2f} (t_crit = 2.069)")

print("\n--- 1.8 Сглаживание (ПСС, m=3) ---")
y_ma3 = np.convolve(y, np.ones(3)/3, mode='valid')
print("Сглаженные значения (центр):", np.round(y_ma3, 2))

print("\n--- 1.9 Модели тренда (МНК) ---")
# Линейная
slope, intercept, r_lin, _, _ = stats.linregress(t, y)
# Полиномиальная 2-й степени
poly2 = np.polyfit(t, y, 2)
y_pred_poly2 = np.polyval(poly2, t)
r2_poly2 = 1 - np.sum((y - y_pred_poly2)**2) / np.sum((y - np.mean(y))**2)
print(f"Линейная: y = {intercept:.2f} + {slope:.2f}*t (R2 = {r_lin**2:.3f})")
print(f"Полином 2: y = {poly2[2]:.2f} + {poly2[1]:.2f}*t + {poly2[0]:.4f}*t^2 (R2 = {r2_poly2:.3f})")

print("\n--- 2.1 Оценка остатков (Полином 2) ---")
residuals = y - y_pred_poly2

# =====================================================================
# ДОПОЛНЕНИЕ ДЛЯ ПУНКТА 2.2: СРАВНЕНИЕ МЕТОДОВ СГЛАЖИВАНИЯ
# =====================================================================

print("\n--- 2.2 Сравнение методов сглаживания (ПСС m=3 и m=5) ---")
# Считаем ПСС с окном m=5
y_ma5 = np.convolve(y, np.ones(5)/5, mode='valid')

print("ПСС (m=3), первые 5 значений:", np.round(y_ma3[:5], 2))
print("ПСС (m=5), первые 5 значений:", np.round(y_ma5[:5], 2))

print(f"Мат. ожидание остатков: {np.mean(residuals):.5f}")
dw_res = np.sum(np.diff(residuals)**2) / np.sum(residuals**2)
print(f"Критерий Дарбина-Уотсона для остатков: {dw_res:.2f}")
# RS-тест
rs = (np.max(residuals) - np.min(residuals)) / np.std(residuals, ddof=1)
print(f"RS-критерий нормальности: {rs:.2f} (норма: 3.05 - 4.38)")

print("\n--- 2.3 Расширенный тест Дики-Фуллера (ADF) ---")
adf_result = adfuller(y)
print(f"ADF Statistic: {adf_result[0]:.2f}, p-value: {adf_result[1]:.4f}")


# =====================================================================
# ЧАСТЬ 2: ГРАФИКИ (СТРОГО ПОСЛЕ РАСЧЕТОВ)
# =====================================================================

# Ограничим вывод графиков, чтобы они не конфликтовали со старыми окнами matplotlib
plt.close('all')

# ---------------------------------------------------------------------
# График 1: к пунктам 1.8 и 1.9 (Исходный ряд + Сглаживание + Линии тренда)
# ---------------------------------------------------------------------
plt.figure(figsize=(11, 5))
plt.plot(years, y, marker='o', color='black', label='Исходный ряд', linewidth=1.5)
# Для скользящей средней берем срез по годам, так как mode='valid' урезает 2 точки
plt.plot(years[1:-1], y_ma3, linestyle='--', color='blue', label='Скользящая средняя (m=3)', linewidth=2)
plt.plot(years, intercept + slope * t, color='orange', linestyle=':', label=f'Линейный тренд (R²={r_lin**2:.2f})')
plt.plot(years, y_pred_poly2, color='red', label=f'Квадратичный тренд (R²={r2_poly2:.2f})')

plt.title('Сглаживание и моделирование тренда временного ряда (2000–2023 гг.)', fontsize=12, fontweight='bold')
plt.xlabel('Годы', fontsize=10)
plt.ylabel('Значения y', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right')
plt.xticks(years[::2])
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------
# График 2: к пункту 2.1 (Анализ остатков полиномиальной модели)
# ---------------------------------------------------------------------
plt.figure(figsize=(11, 4))
plt.bar(years, residuals, color='purple', alpha=0.6, edgecolor='black', label='Остатки (y - y_pred)')
plt.axhline(0, color='red', linestyle='--', linewidth=1)

plt.title('График остатков квадратичной модели тренда', fontsize=12, fontweight='bold')
plt.xlabel('Годы', fontsize=10)
plt.ylabel('Величина остатка', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower left')
plt.xticks(years[::2])
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------
# График 3: к пункту 2.2 (Сравнение методов сглаживания)
# ---------------------------------------------------------------------
plt.figure(figsize=(11, 5))
plt.plot(years, y, marker='o', color='black', alpha=0.4, label='Исходный ряд', linewidth=1)
plt.plot(years[1:-1], y_ma3, linestyle='--', color='blue', label='Скользящая средняя (m=3)', linewidth=2)
# Для m=5 mode='valid' срезает по 2 точки с каждого края (n=24 -> 20 точек)
plt.plot(years[2:-2], y_ma5, linestyle='-', color='darkgreen', label='Скользящая средняя (m=5)', linewidth=2)

plt.title('Пункт 2.2: Сравнение методов сглаживания временного ряда', fontsize=12, fontweight='bold')
plt.xlabel('Годы', fontsize=10)
plt.ylabel('Значения y', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right')
plt.xticks(years[::2])
plt.tight_layout()
plt.show()
