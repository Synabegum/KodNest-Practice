student_count = int(input())
marks = []

# Read and store all marks using append()
for i in range(0, student_count):
    score = int(input())
    marks.append(score)

position = int(input())
corrected_mark = int(input())
passing_mark = int(input())

# Update the mark at the entered student position
marks[position - 1] = corrected_mark

# Calculate the total, average, highest and lowest marks
highest = max(marks)
lowest = min(marks)
total = sum(marks)
average = total / student_count

passed_students = 0

# Count the students whose marks satisfy the passing condition
for mark in marks:
    if mark >= passing_mark:
        passed_students = passed_students + 1

# Display the updated analysis
print(f"Updated Marks: {marks}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")
print(f"Passed Students: {passed_students}")