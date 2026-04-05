#СТОЛБЧАТАЯ ДИАГРАММА 2019
import matplotlib.pyplot as plt

# 1. Данные
countries = [
    "Афганистан", "Непал", "Гондурас", "Бангладеш", "Мексика", "Чили", 
    "Канада", "США", "Финляндия", "Ирландия", "Израиль", "Италия", 
    "Аргентина", "Норвегия", "Кыргызстан", "Греция", "Куба", "Азербайджан", 
    "Эстония", "Армения", "Китай", "Франция", "Польша", "Венгрия", 
    "Австрия", "РФ", "Германия", "Беларусь", "Монголия", "Япония"
]

beds_count = [3.8, 2.9, 6.5, 8.9, 9.6, 20.2, 25.1, 27.2, 33.5, 28.8, 31.0, 31.4, 36.9, 34.8, 40.9, 41.5, 42.1, 39.4, 45.3, 40.6, 48.2, 59.6, 61.3, 69.1, 71.9, 70.3, 78.7, 99.3, 79.4, 127.9]

# 2. Построение
plt.figure(figsize=(12, 7))

# Цвета
bars = plt.bar(countries, beds_count, color='#70AD47', edgecolor='#548235')

# 3. Настройка оформления
plt.title('Распределения больничных коек на 10000 населения в разных странах в 2019 году', 
          fontsize=12, fontweight='bold', pad=20, color='#385723')

plt.ylabel('Количество коек', fontsize=10)
plt.xlabel('Страны', fontsize=10)

# Поворот названия стран, чтобы все читались
plt.xticks(rotation=45, ha='right', fontsize=9)

# Стилизация под Excel
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, yval, 
             ha='center', va='bottom', fontsize=8, color='#385723')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.grid(axis='y', linestyle='-', color='#D9D9D9', alpha=0.7)

plt.tight_layout() # Чтобы названия стран не вылезли за границы картинки
plt.show()
