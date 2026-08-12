class StudentProfile:
    pass
name = input().strip()
student = StudentProfile()
student.name = name
print(f"Student Name: {student.name}")