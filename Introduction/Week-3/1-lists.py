# write a program that requests five grades as input, displays the average - BUT, only after dropping the two lowest grades

grades = []
grade = float(input('Enter your first grade:'))
grades.append(grade)

grade = float(input('Enter your grade:'))
grades.append(grade)

grade = float(input('Enter your grade:'))
grades.append(grade)

grade = float(input('Enter your grade:'))
grades.append(grade)

grade = float(input('Enter your grade:'))
grades.append(grade)

grades.remove(min(grades))
grades.remove(min(grades))

print('Average grade is: ', (sum(grades) / len(grades)))