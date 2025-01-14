import csv
print("The CSV Content")
with open("student.csv",mode="r") as file:
    csvr=csv.reader(file)
    for row in csvr:
        print(row)