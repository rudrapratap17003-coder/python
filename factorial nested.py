n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
elif n == 0:
    print("Factorial of 0 is 1")    
else:
    factorial = 1
for i in range(1, n + 1):
    for j in range(1, 2):
        factorial = factorial * i
print("Factorial of", n, "=", factorial)