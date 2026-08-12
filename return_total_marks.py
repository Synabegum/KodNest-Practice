def calculate_total(first_mark, second_mark):
    total_marks = first_mark + second_mark
    return total_marks

mark1 = int(input())
mark2 = int(input())

total = calculate_total(mark1, mark2)

print(total)