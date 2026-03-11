import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 1. Данные
bins_edges = [3.6, 24, 44.4, 64.8, 85.2, 105.6, 126]
mid_points = [13.8, 34.2, 54.6, 75, 95.4, 115.8]
width = 20.4

emp_density = [0.009803922, 0.022875817, 0.004901961, 0.006535948, 0.001633987, 0.003267974]

x_points = np.array([3.6] + mid_points + [126])
y_points = np.array([0.005415, 0.020020203, 0.013162662, 0.007036268, 0.003924185, 0.002314135, 0.001433323, 0.001146])

# Сглаживание
x_smooth = np.linspace(x_points.min(), x_points.max(), 300) 
spl = make_interp_spline(x_points, y_points, k=3)
y_smooth = spl(x_smooth)

# 2. Построение в стиле "Офис (Зеленая схема)"
plt.figure(figsize=(10, 6))

# Цвет #70AD47 — это классический зеленый из MS Office
plt.bar(mid_points, emp_density, width=width, 
        color='#70AD47',       # Основной зеленый
        edgecolor='#548235',   # Темно-зеленая рамка
        alpha=0.85, 
        label='Эмпирическая плотность')

# Цвет #385723 — темно-зеленый акцент для линии
plt.plot(x_smooth, y_smooth, 
         color='#385723',      # Глубокий зеленый
         linewidth=3, 
         label='Логнормальное (сглаженное)')

# Добавляем точки данных (маркеры)
plt.scatter(x_points, y_points, color='#385723', s=40, zorder=3)

# 3. Финальное оформление
plt.xlim(bins_edges[0], bins_edges[-1])
plt.ylim(bottom=0)
plt.xticks(bins_edges)

# Сделаем сетку более незаметной, как в Excel
plt.grid(axis='y', linestyle='-', color='#D9D9D9', alpha=0.7)

plt.title('Распределение плотности вероятностей', fontsize=14, color='#385723', fontweight='bold')
plt.xlabel('Интервалы', fontsize=11)
plt.ylabel('Плотность', fontsize=11)

# Убираем лишние рамки сверху и справа (стиль Excel)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.legend(frameon=False) # Легенда без рамки

plt.show()
