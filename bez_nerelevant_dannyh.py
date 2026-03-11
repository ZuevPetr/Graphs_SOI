#ГИСТОГРАММА ЭМПИРИЧЕСКОГО И ЛОГНОРМАЛЬНОГО РАСПРЕДЕЛЕНИЯ БЕЗ НЕРЕЛЕВАНТНЫХ ДАННЫХ
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 1. Данные из таблицы со скрина
# Границы интервалов (столбцы "Лев" и "Прав")
bins_edges = [6.6, 18.35, 30.1, 41.85, 53.6, 65.35, 77.1]
# Середины интервалов (столбец "Ср")
mid_points = [12.475, 24.225, 35.975, 47.725, 59.475, 71.225]
# Ширина интервала (18.35 - 6.6 = 11.75)
width = 11.75

# Эмпирическое распределение
emp_density = [0.010212766, 0.017021277, 0.017021277, 0.020425532, 0.006808511, 0.013617021]

# Точки для построения сглаженной кривой (Логнормальное распределение)
# Добавляем краевые точки 0 по краям, чтобы кривая не висела в воздухе
x_points = np.array([6.6] + mid_points + [77.1])
y_points = np.array([0.005, 0.013842631, 0.022755607, 0.017786703, 0.011636099, 0.007245031, 0.004475921, 0.002])

# Сглаживание кривой
x_smooth = np.linspace(x_points.min(), x_points.max(), 300) 
spl = make_interp_spline(x_points, y_points, k=3)
y_smooth = spl(x_smooth)

# 2. Построение в стиле "Офис (Зеленая схема)"
plt.figure(figsize=(10, 6))

# Гистограмма
plt.bar(mid_points, emp_density, width=width, 
        color='#70AD47',       
        edgecolor='#548235',   
        alpha=0.85, 
        label='Эмпирическая плотность')

# Сглаженная линия логнормального распределения
plt.plot(x_smooth, y_smooth, 
         color='#385723',      
         linewidth=3, 
         label='Логнормальное (сглаженное)')

# Точки данных логнормального распределения
plt.scatter(x_points[1:-1], y_points[1:-1], color='#385723', s=40, zorder=3)

# 3. Финальное оформление
plt.xlim(bins_edges[0], bins_edges[-1])
plt.ylim(bottom=0)
plt.xticks(bins_edges)

# Сетка в стиле Excel
plt.grid(axis='y', linestyle='-', color='#D9D9D9', alpha=0.7)

plt.title('Распределение плотности вероятностей (новые данные)', fontsize=14, color='#385723', fontweight='bold')
plt.xlabel('Интервалы', fontsize=11)
plt.ylabel('Плотность', fontsize=11)

# Убираем лишние рамки
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.legend(frameon=False)

plt.tight_layout()
plt.show()
