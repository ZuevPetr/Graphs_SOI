#СТОЛБЧАТАЯ ДИАГРАММА
import matplotlib.pyplot as plt

# 1. Данные
countries = [
    "Афганистан", "Непал", "Гондурас", "Бангладеш", "Мексика", "Чили", 
    "Канада", "США", "Финляндия", "Ирландия", "Израиль", "Италия", 
    "Аргентина", "Норвегия", "Кыргызстан", "Греция", "Куба", "Азербайджан", 
    "Эстония", "Армения", "Китай", "Франция", "Польша", "Венгрия", 
    "Австрия", "РФ", "Германия", "Беларусь", "Монголия", "Япония"
]

beds_count = [
    3.6, 3.9, 6.6, 9.4, 10.1, 19.8, 25.7, 27.0, 27.6, 29.0, 
    30.5, 30.9, 33.4, 34.0, 40.5, 42.3, 42.7, 43.5, 43.9, 44.3, 
    52.0, 57.7, 62.2, 67.9, 69.1, 69.9, 77.1, 100.2, 105.7, 126.0
]

# 2. Построение
plt.figure(figsize=(12, 7))

# Цвета
bars = plt.bar(countries, beds_count, color='#70AD47', edgecolor='#548235')

# 3. Настройка оформления
plt.title('Распределения больничных коек на 10000 населения в разных странах в 2021 году', 
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
