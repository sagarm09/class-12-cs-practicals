# Create a dictionary of names and marks 
marks = {}
n = int(input("how many students ???"))
for i in range(n):
    name = input("Enter name:")
    score = int(input("Enter marks:"))
    marks[name] = score
print(marks)    