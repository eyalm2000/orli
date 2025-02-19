grade1, grade2, grade3 = int(input("enter grade 1: ")), int(input("enter grade 2: ")), int(input("enter grade 3: "))
average = (grade1 + grade2 + grade3) / 3
rounded_average = round(average)
rounded_average_2 = round(average, 2)
print("your average is: ", average)
print("your rounded average is: ", rounded_average)
print("your rounded average with 2 decimal digits is: ", rounded_average_2)