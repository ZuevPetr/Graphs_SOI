import matplotlib.pyplot as plt

years = list(range(2000, 2024))
beds = [
    107.3, 106.6, 104.9, 103.4, 97.9, 96.4, 95.5, 93.9, 
    91.2, 88.9, 86.9, 85.1, 83.3, 80.8, 78.5, 75.5, 
    73.7, 72.1, 71.4, 70.3, 70.5, 69.9, 68.4, 68.1
]

plt.figure(figsize=(10, 5.5), facecolor='white')

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Calibri', 'Arial', 'DejaVu Sans']
bars = plt.bar(years, beds, color='#4F81BD', edgecolor='#385D8A', linewidth=0.7, width=0.6)

plt.grid(axis='y', linestyle='-', color='#D9D9D9', linewidth=0.75)
plt.gca().set_axisbelow(True)
plt.title('Количество больничных коек на 10000 населения', fontsize=16, fontname='Calibri', color='#333333', weight='bold', pad=20, loc='left')
plt.xticks(years, rotation=90, color='#595959', fontsize=11, fontname='Calibri')
plt.yticks(color='#595959', fontsize=11, fontname='Calibri')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('#D9D9D9')
plt.gca().spines['bottom'].set_color('#D9D9D9')


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}'.replace('.', ','), ha='center', va='bottom', fontsize=9, color='#595959', fontname='Calibri')


plt.xlim(1999, 2024)
plt.ylim(0, 120)
plt.tight_layout()
plt.show()

# ============================КРУГОВАЯ ДИАГРАММА===================================


pie_years = ['2000 год', '2005 год', '2010 год', '2015 год', '2020 год', '2023 год']
pie_beds = [107.3, 96.4, 86.9, 75.5, 70.5, 68.1]


excel_pie_colors = ['#4F81BD', '#70AD47', '#95B3D7', '#B8CCE4', '#DCE6F1', '#7F7F7F']

plt.figure(figsize=(10, 5.5), facecolor='white')

wedges, texts, autotexts = plt.pie(
    pie_beds, 
    labels=pie_years, 
    colors=excel_pie_colors,
    autopct=lambda p: f'{p:.1f}%'.replace('.', ','),
    startangle=140, 
    textprops={'fontname': 'Calibri', 'color': '#333333', 'fontsize': 11},
    wedgeprops={'edgecolor': 'white', 'linewidth': 1})

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

plt.title('Долевое соотношение обеспеченности койками по ключевым периодам', 
          fontsize=16, fontname='Calibri', color='#333333', weight='bold', pad=20, loc='left')

plt.tight_layout()
plt.show()
