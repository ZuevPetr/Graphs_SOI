import numpy as np
import matplotlib.pyplot as plt

beds = np.array([
    107.3, 106.6, 104.9, 103.4, 97.9, 96.4, 95.5, 93.9, 
    91.2, 88.9, 86.9, 85.1, 83.3, 80.8, 78.5, 75.5, 
    73.7, 72.1, 71.4, 70.3, 70.5, 69.9, 68.4, 68.1
])
years = list(range(2000, 2024))
trend_cycle = np.convolve(beds, np.ones(3)/3, mode='same')
trend_cycle[0] = beds[0]
trend_cycle[-1] = beds[-1]
residual = beds - trend_cycle
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), facecolor='white')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Calibri', 'Arial']


ax1.plot(years, beds, color='#4F81BD', marker='o', linewidth=2, label='Исходный ряд (Yt)')
ax1.plot(years, trend_cycle, color='#70AD47', linestyle='--', linewidth=2, label='Тренд-циклическая компонента (Tt)')
ax1.set_title('Декомпозиция временного ряда обеспеченности койками', fontsize=14, fontname='Calibri', color='#333333', weight='bold', pad=15, loc='left')
ax1.grid(axis='y', linestyle='-', color='#D9D9D9', linewidth=0.5)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=90, color='#595959', fontsize=9)
ax1.legend(frameon=False, prop={'family': 'Calibri', 'size': 10})
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)


ax2.bar(years, residual, color='#C00000', alpha=0.7, edgecolor='none', width=0.5, label='Случайная компонента (Et)')
ax2.axhline(0, color='#595959', linewidth=0.8)
ax2.grid(axis='y', linestyle='-', color='#D9D9D9', linewidth=0.5)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=90, color='#595959', fontsize=9)
ax2.legend(frameon=False, prop={'family': 'Calibri', 'size': 10})
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
