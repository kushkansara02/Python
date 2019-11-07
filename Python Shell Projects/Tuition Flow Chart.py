#kush

passes = 0
failures = 0
students = 1

while students <= 10:
    a = int(input("What is the student's exam result? "))

    if a >= 50:
        passes += 1

    else:
        failures += 1

    students += 1

print("The number of passes is:",passes)
print("The number of failures is:",failures)

if passes >= 8:
    print("raise tuition")
