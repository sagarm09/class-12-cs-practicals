# count csv records with marks above 80
import csv
count =0
with open("student.csv","r",newline="") as f:
    reader = csv.reader(f)
    next(reader,None)
    for row in reader:
        if int(row[2])>80:
            count +=1
print("students scoring above 80 =", count)
