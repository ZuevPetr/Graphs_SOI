#КРУГОВАЯ ДИАГРАММА
import matplotlib.pyplot as plt

# 1. Данные
labels = [
    '3.6 – 24.0', 
    '24.0 – 44.4', 
    '44.4 – 64.8', 
    '64.8 – 85.2', 
    '85.2 – 105.6', 
    '105.6 – 126.0'
]
sizes = [6, 14, 3, 4, 1, 2] # Частоты (количество стран)

# 2. Цветовая схема 14 (оттенки зеленого из MS Office)
office_greens = [
    '#385723', # Темно-зеленый
    '#548235', 
    '#70AD47', # Основной зеленый
    '#A9D08E', 
    '#C6E0B4', 
    '#E2EFDA'  # Самый светлый
]

# 3. Построение
plt.figure(figsize=(10, 7))

# Создаем круговую диаграмму
patches, texts, autotexts = plt.pie(
    sizes, 
    labels=labels, 
    autopct='%1.1f%%',      # Показываем проценты
    startangle=140,         # Поворот для красоты
    colors=office_greens,   # Наша зеленая палитра
    pctdistance=0.85,       # Расстояние процентов от центра
    explode=(0, 0, 0, 0, 0, 0), #
    wedgeprops={'edgecolor': 'white', 'linewidth': 2} # Белые границы между секторами
)

# Настройка шрифтов
plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=11)

plt.title('Распределение стран по интервалам количества коек', 
          fontsize=14, fontweight='bold', color='#385723', pad=20)

# Добавляем легенду сбоку
plt.legend(labels, title="Интервалы", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()
