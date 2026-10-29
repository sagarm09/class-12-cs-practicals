#writes rows to a csv file
import csv
rows = [["rollno", "name","marks"],
        [1,"asha",88],
        [2, "ravi",76]]
with open("student.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("csv file created")
