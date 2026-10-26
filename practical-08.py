#Find factorial using a loop ::
n = int(input("ENTER A NON NEGATIVE NUMBER :"))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("factorial = ", fact)