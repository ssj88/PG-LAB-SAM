import csv
filename = "emp.csv"
fields = []
rows = []
cf=open(filename, 'r')
csvreader = csv.DictReader(cf)
for r in csvreader:
  print(dict(r))