import matplotlib.pyplot as plt

# 1. Данные
data = [3.6, 3.9, 6.6, 9.4, 10.1, 19.8, 25.7, 27.0, 27.6, 29.0, 
        30.5, 30.9, 33.4, 34.0, 40.5, 42.3, 42.7, 43.5, 43.9, 44.3, 
        52.0, 57.7, 62.2, 67.9, 69.1, 69.9, 77.1, 100.2, 105.7, 126.0]

plt.figure(figsize=(7, 8))

# 2. Построение Boxplot (Зеленая схема)
# showmeans=True добавляет среднее значение
# meanprops настраивает его как крестик 'x'
box = plt.boxplot(data, vert=True, patch_artist=True, widths=0.5,
                  showmeans=True,
                  meanprops=dict(marker='x', markeredgecolor='#385723', markersize=10, markeredgewidth=2),
                  flierprops=dict(marker='o', markerfacecolor='#70AD47', markersize=6, markeredgecolor='#548235'),
                  medianprops=dict(color='white', linewidth=2),
                  whiskerprops=dict(color='#548235', linewidth=1.5),
                  capprops=dict(color='#548235', linewidth=1.5))

# Раскрашиваем тело ящика в основной зеленый
for patch in box['boxes']:
    patch.set_facecolor('#70AD47')
    patch.set_edgecolor('#548235')
    patch.set_alpha(0.85)

# 3. Оформление осей и подписей
plt.title('Boxplot (Распределение показателей)', fontsize=14, color='#385723', fontweight='bold', pad=20)
plt.ylabel('Обеспеченность койками', fontsize=11)
plt.xlabel('Исследуемый показатель', fontsize=11)

# Фиксируем шкалу от 0 до 140 как на скрине
plt.ylim(0, 140)

# Горизонтальная сетка
plt.grid(axis='y', linestyle='-', color='#D9D9D9', alpha=0.7)

# Убираем лишние рамки для стиля "чистый отчет"
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('#D9D9D9')
plt.gca().spines['bottom'].set_color('#D9D9D9')

plt.tight_layout()
plt.show()

