from datetime import datetime, date, time, timedelta
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
import csv

dates = []
spots = []
with open('data.csv') as f:
    reader = csv.reader(f)
    for r in reader:
        t = float(r[0])
        p = int(r[1])
        dates.append(datetime.fromtimestamp(t))
        spots.append(p)

spots_max = max(spots)
spots = [spots_max-p for p in spots]


def plot(d, s, formatter=None):
    plt.subplots(figsize=(16, 4))
    plt.tight_layout()
    plt.ylim(0, spots_max+10)
    plt.margins(0)

    if formatter is not None:
        plt.gcf().axes[0].xaxis.set_major_formatter(formatter)

    plt.plot(d, s)


def plot_since(t, formatter=None):
    d, s = zip(*filter(lambda p: p[0] >= t, zip(dates, spots)))
    plot(d, s, formatter)


def save_clear(filename):
    plt.savefig(filename)
    plt.clf()


def avg_weekday(weekday, from_t=0, to_t=24):
    datetime_weekday = date.today() + timedelta(days=weekday-date.today().weekday())
    hourly_buckets = {n: [] for n in range(from_t, to_t)}
    for t, s in zip(dates, spots):
        if t.weekday() == weekday and t.hour in hourly_buckets.keys():
            hourly_buckets[t.hour].append(s)

    hourly_s = {datetime.combine(datetime_weekday, time(hour=k)): (0 if len(l) == 0 else sum(l)/len(l))
                for k, l in hourly_buckets.items()}

    return hourly_s


# today.svg
plot_since(datetime.combine(date.today(), time(hour=9)), DateFormatter('%H:%M'))
save_clear('docs/today.svg')

# today_avg.svg
hourly_s = avg_weekday(date.today().weekday(), from_t=9, to_t=23)
plot(list(hourly_s.keys()), list(hourly_s.values()), DateFormatter('%H:%M'))
save_clear('docs/today_avg.svg')

# week.svg
today = date.today()
plot_since(datetime.combine(today - timedelta(days=today.weekday()), time(0, 0)), DateFormatter('%a %H:%M'))
save_clear('docs/week.svg')

# week_avg.svg
hourly_s_week = {}
for i in range(0, 7):
    hourly_s_week = {**hourly_s_week, **avg_weekday(i)}

plot(list(hourly_s_week.keys()), list(hourly_s_week.values()), DateFormatter('%a %H:%M'))
save_clear('docs/week_avg.svg')

# [monday-sunday].svg
for i in range(0, 7):
    hourly_s_daily = avg_weekday(i, from_t=9, to_t=23)
    plot(list(hourly_s_daily.keys()), list(hourly_s_daily.values()), DateFormatter('%H:%M'))
    save_clear('docs/' + ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][i] + '.svg')
