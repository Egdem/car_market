import matplotlib
import matplotlib.pyplot as plt # Подключаем модули
import pandas as pd

matplotlib.use('Qt5Agg')  # Используем в качестве бекэнда PyQt5

data_2023, data_2022 = {}, {}

df = pd.read_excel('data.xlsx')  # Считываем имеющиеся данные в таблице Excel
barWidth = 0.45
plt.bar(df['Label'], height=df['This year'], color='c', width=barWidth, label='2023', align='edge')
plt.bar(df['Label'], height=df['Last year'], color='r', width=-barWidth, label='2022', align='edge')
plt.title("Продажи автомобилей за год, шт")
plt.xticks(rotation=90)
plt.legend()  # Выводим подписи к графикам(легенды)
plt.grid()  # Выводим сетку
plt.show()

plt.pie([int(x) for x in df['This year']][:10],labels=df['Label'][:10],shadow=True, autopct = '%.2f')       #Создаем круговую диагрмму 2023
plt.title("Доли рынка 2023 (6 месяцев)")
legend_obj = plt.legend()  #Добавим легенду(чтобы свободно перемещать)
legend_obj.set_draggable(True)
plt.show()

plt.pie([int(x) for x in df['Last year']][:10],labels=df['Label'][:10],shadow=True, autopct = '%.2f')       #Создаем круговую диагрмму 2022
plt.title("Доли рынка 2022 (6 месяцев)")
legend_obj = plt.legend()  #Добавим легенду
legend_obj.set_draggable(True)
plt.show()


