#store  and read records using pickel
import pickle

found = False
with open("student.dat",'rb') as f:
    try:
        while True:
            record = pickle.load(f)

            if record[0] == 101:
                print("Record found:", record)
                found = True
                break

    except EOFError:
        pass

    if not found:
        print("Record not found")
