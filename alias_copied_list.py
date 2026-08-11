value_count = int(input())
original_list = []

for index in range(value_count):
    value = int(input())
    original_list.append(value)

alias_list = original_list
copied_list = original_list.copy()

alias_position = int(input())
alias_value = int(input())
copy_position = int(input())
copy_value = int(input())

alias_index = alias_position - 1
copy_index = copy_position - 1

alias_list[alias_index] = alias_value
copied_list[copy_index] = copy_value

different_positions = 0

for index in range(value_count):
    if original_list[index] != copied_list[index]:
        different_positions += 1

print(f"Original List: {original_list}")
print(f"Alias List: {alias_list}")
print(f"Copied List: {copied_list}")

if alias_list is original_list:
    print("Alias Shares Original: Yes")
else:
    print("Alias Shares Original: No")

print(f"Different Positions: {different_positions}")