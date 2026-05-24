import numpy as np
import matplotlib.pyplot as plt

# Исходные данные из вашей таблицы
beds = np.array([
    107.3, 106.6, 104.9, 103.4, 97.9, 96.4, 95.5, 93.9, 
    91.2, 88.9, 86.9, 85.1, 83.3, 80.8, 78.5, 75.5, 
    73.7, 72.1, 71.4, 70.3, 70.5, 69.9, 68.4, 68.1
])
n = len(beds)

# 1. Расчет коэффициентов автокорреляции (rho_k) для лагов k=1, 2, 3
mean_y = np.mean(beds)
var_y = np.var(beds, ddof=0)

lags = [1, 2, 3]
rho_values = []

for k in lags:
    # Центрированные значения
    y_t = beds[:-k] - mean_y
    y_tk = beds[k:] - mean_y
    # Коэффициент автокорреляции
    rho = np.sum(y_t * y_tk) / (n * var_y)
    rho_values.append(rho)

# 2. Расчет критерия Дарбина-Уотсона (d) строго по формуле из методички
numerator = np.sum((beds[1:] - beds[:-1]) ** 2)
denominator = np.sum(beds ** 2)
d_stat = numerator / denominator

print(f"Коэффициенты автокорреляции: rho_1 = {rho_values[0]:.4f}, rho_2 = {rho_values[1]:.4f}, rho_3 = {rho_values[2]:.4f}")
print(f"Критерий Дарбина-Уотсона d = {d_stat:.4f}")

# 3. Построение коррелограммы в стиле Excel
plt.figure(figsize=(8, 4.5), facecolor='white')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Calibri', 'Arial']

# Столбцы коррелограммы
bars = plt.bar(lags, rho_values, color='#4F81BD', edgecolor='#385D8A', linewidth=0.7, width=0.4)

# Стилизация осей и сетки
plt.grid(axis='y', linestyle='-', color='#D9D9D9', linewidth=0.75)
plt.gca().set_axisbelow(True)

plt.title('Коррелограмма временного ряда', fontsize=16, fontname='Calibri', color='#333333', weight='bold', pad=20, loc='left')
plt.xlabel('Лаг (k)', fontsize=11, fontname='Calibri', color='#333333')
plt.ylabel('Коэффициент автокорреляции (ρk)', fontsize=11, fontname='Calibri', color='#333333')

plt.xticks(lags, [f'Лаг {k}' for k in lags], color='#595959', fontsize=11, fontname='Calibri')
plt.yticks(color='#595959', fontsize=11, fontname='Calibri')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('#D9D9D9')
plt.gca().spines['bottom'].set_color('#D9D9D9')

# Значения над столбцами
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval - 0.08 if yval > 0 else yval + 0.02, 
             f'{yval:.3f}'.replace('.', ','), ha='center', va='bottom', fontsize=10, color='#333333', fontname='Calibri', weight='bold')

plt.xlim(0.5, 3.5)
plt.ylim(-1, 1.1)
plt.axhline(0, color='#595959', linewidth=0.8) # Линия нуля

plt.tight_layout()
plt.show()
