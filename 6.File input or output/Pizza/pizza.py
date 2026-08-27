import csv
import os
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

if not os.path.exists(filename):
    sys.exit("File does not exist")

with open(filename) as file:
    reader = csv.reader(file)
    rows = list(reader)

print(tabulate(rows[1:], headers=rows[0], tablefmt="grid"))
