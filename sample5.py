import csv

data = [
    {'name': 'Thomas', 'branch': 'MCA', 'year': 2, 'cgpa': 9.0},
    {'name': 'Vishnu', 'branch': 'MCA', 'year': 2, 'cgpa': 1.1},
    {'name': 'Tessa', 'branch': 'MCA', 'year': 2, 'cgpa': 9.3},
    {'name': 'Adwaith', 'branch': 'MCA', 'year': 1, 'cgpa': 9.5},
]

fields = ['name', 'branch', 'year', 'cgpa']
filename = "dict.csv"

# Writing to the file
with open(filename, mode="w",newline="") as file:  # Added `newline=""` here
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print("Dictionary")

# Reading from the file
with open(filename, mode="r",newline="") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
