class StudentProfile:
    def __init__(self, student_id, name, course):
        # Store the received values in instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        pass

student_id = int(input())
name = input().strip()
course = input().strip()

# Create a StudentProfile object
student = StudentProfile(student_id,name,course)

# Print the stored student details
print("Student ID:",student_id)
print("Name:",name)
print("Course:",course)