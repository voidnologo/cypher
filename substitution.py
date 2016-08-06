from make_word_patterns import create_word_pattern
# from word_patterns_dict import all_patterns
from system_patterns import all_patterns

# pattern = create_word_pattern('cflmifmb')
# print(all_patterns[pattern])
# print('*' * 20, '\n', pattern)

with open('ascii.txt', 'r') as f:
    contents = f.read()
words = set(contents.split())

substitutions = {}
for word in words:
    pattern = create_word_pattern(word)
    possibles = all_patterns[pattern] if pattern in all_patterns else []
    substitutions[word] = len(possibles)

print(substitutions)
