marks = []

n = int(input("How many students? "))

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

print("Marks:", marks)

print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))