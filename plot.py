from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
import csv

dates = []
plaetze = []
with open('data.csv') as f:
    reader = csv.reader(f)
    for r in reader:
        t = float(r[0])
        p = int(r[1])
        dates.append(datetime.fromtimestamp(t))
        plaetze.append(p)


def plot_since(t):
    d, p = zip(*filter(lambda p: p[0] >= t, zip(dates, plaetze)))
    plt.clf()
    plt.subplots(figsize=(12,4))
    plt.tight_layout()
    plt.ylim(0,171)
    plt.margins(0)
    formatter = DateFormatter('%d.%m %H:00')
    plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
    plt.plot(d,p)

plot_since(datetime.now()-timedelta(days=14))
plt.savefig('docs/two_week.svg')
plot_since(datetime.now()-timedelta(days=7))
plt.savefig('docs/week.svg')
plot_since(datetime.now()-timedelta(days=2))
plt.savefig('docs/two_day.svg')
plot_since(datetime.now()-timedelta(days=1))
plt.savefig('docs/day.svg')