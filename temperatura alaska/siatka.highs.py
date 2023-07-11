import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_full.csv'
with open(filename) as file:
    reader = csv.reader(file)
    head_row = next(reader)

    # Pobranie maksymalnych temperatur z pliku

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        low = int(row[9])
        high = int(row[8])
        dates.append(current_date)
        lows.append(low)
        highs.append(high)

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatowanie wykresu
ax.set_title("Temperatura maxsymalna w lipcu 2018", fontsize=14)
ax.set_xlabel("Dni", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
