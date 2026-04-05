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

beds_count = a = [59.1, 70, 69, 73.1, 70.8, 79, 81.6, 76.4, 81.5, 81.6, 81.7, 82.2, 74.6, 82.9, 72.2, 79.6, 73.7, 72.9, 70.1, 73, 77.6, 81.9, 75.4, 74.4, 81, 70, 80.5, 73.1, 70.1, 84.5]

# 2. Построение
plt.figure(figsize=(12, 7))

# Цвета
bars = plt.bar(countries, beds_count, color='#70AD47', edgecolor='#548235')

# 3. Настройка оформления
plt.title('Ожидаемая продолжительность жизни при рождении в 2021 году', 
          fontsize=12, fontweight='bold', pad=20, color='#385723')

plt.ylabel('Возраст', fontsize=10)
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
