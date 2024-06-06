number = int(input("How many words will you enter?(between 3 and 6) >"))
while number < 3 or number > 6:
    number = int(input("How many words will you enter?(between 3 and 6) >"))

words = []
for word in range(1, number + 1):
    word = input(f"Word #{word} please ")
    words.append(word)

shortest = words[0]
longest = words[0]
total = 0
for word in words:
    total += len(word)
    if len(shortest) >= len(word):
        shortest = word
    if len(longest) <= len(word):
        longest = word

average_length = total / number
print("Shortest word:", shortest)
print("Longest word:", longest)
print(f"Average length: {average_length:.2f}")

