import csv
with open("student.csv", mode="r") as file:
    csvr = list(csv.reader(file))  # Convert to a list for easy indexing  # Total rows in the CSV file
    for row in csvr:
        print(row)
    n = int(input("\nEnter column number to display\n"))
    if n<0 or n> len(csvr):
        print("not valid")
    else:
        print("selected row\n",csvr[n])
    