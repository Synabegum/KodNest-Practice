class StudentProfile:
    def __init__(self, student_id, name, course, score, skills, is_placed):
        # Store received values in instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed

# Read inputs from the user
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())

# Parse comma-separated skills into a list of strings
skills = [skill.strip() for skill in input().strip().split(",")]

# Parse placement input into a boolean (case-insensitive)
placement_input = input().strip().lower()
is_placed = placement_input == "yes"

# Create exactly one StudentProfile object
student = StudentProfile(student_id, name, course, score, skills, is_placed)

# Determine placement status display text
placement_status = "Placed" if student.is_placed else "Not Placed"

# Print details strictly from the object's instance attributes
print(f"Student ID: {student.student_id}")
print(f"Name: {student.name}")
print(f"Course: {student.course}")
print(f"Score: {student.score:.1f}")
print(f"Skills: {', '.join(student.skills)}")
print(f"Placement Status: {placement_status}")