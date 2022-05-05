import csv
import pandas as pd

file=open('richathletes.csv')
type(file)
csvreader = csv.reader(file)

header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
"""https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/"""
"""https://realpython.com/python-csv/"""
"""https://www.geeksforgeeks.org/working-csv-files-python/"""