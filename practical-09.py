#check wheather a number is prime::::::::
n = int(input("Enter a number :"))
prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        prime = False
        break
print("Prime" if prime else "Not a prime")    