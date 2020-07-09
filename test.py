import csv


js = []


f = 'H:\\Python\\projects\\news-analysis\\data.csv'


reader = csv.DictReader(open(f, "rt", encoding='utf-8'))
for line in reader:
    js.append(line)

