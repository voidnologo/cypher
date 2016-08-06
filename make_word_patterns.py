# import pprint
# import english
# from collections import defaultdict
# import subprocess

# word_list = subprocess.check_output(
#     "cat /usr/share/dict/words | grep -v \"'s\"",
#     shell=True,
#     universal_newlines=True
# ).split('\n')


def create_word_pattern(word):
    next_num = 0
    letter_ids = {}
    word_pattern = []

    for letter in word.upper():
        if letter not in letter_ids:
            letter_ids[letter] = str(next_num)
            next_num += 1
        word_pattern.append(letter_ids[letter])
    return '.'.join(word_pattern)


# def main():
#     all_patterns = defaultdict(list)
#     # for word in english.load_dictionary():
#     for word in word_list:
#         pattern = create_word_pattern(word)
#         all_patterns[pattern].append(word)
#     with open('system_patterns.py', 'w') as f:
#         f.write('all_patterns = ')
#         f.write(pprint.pformat(all_patterns, width=120))


# if __name__ == '__main__':
#     main()
