entered_word = input()

character_count = dict()

for char in entered_word:
    if char not in character_count.keys():
        character_count[char] = 1
    else:
        character_count[char] += 1

result = "\n".join(f"{key} {value}" for key, value in sorted(character_count.items()))

print(result)