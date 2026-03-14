import csv
marks=[]

with open("students.csv","r") as file:
    reader=csv.DictReader(file)   #DictReader reads each row as a dictionary

    for row in reader:
        marks.append(int(row["marks"]))

print("Average:", sum(marks)/len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))