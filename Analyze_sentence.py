sentence = input()
position = int(input())
count = 0
# Remove outer spaces and convert the sentence to lowercase
cleaned = sentence.strip().lower()
# Replace the required punctuation marks with spaces
punctuation_marks = cleaned.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(";", " ").replace(":", " ")

# Split the sentence into words and rebuild the cleaned sentence
words = punctuation_marks.split()
cleaned_sentence = " ".join(words)
# Extract the required words and slices
selected_word = position -1
first_word = words[0]
last_word = words[-1]
prefix = words[0][:3]
suffix = words[-1][-3:]
for i in words:
    count+=1
# Display the complete analysis
print(f"Cleaned Sentence: {cleaned_sentence}")
print(f"Word Count: {count}")
print(f"First Word: {first_word}")
print(f"Last Word: {last_word}")
print(f"Selected Word: {words[selected_word]}")
print(f"First Word Prefix: {prefix}")
print(f"Last Word Suffix: {suffix}")