from collections import defaultdict
import json

from dictionaries import system_dictionary


class Patterns(object):

    def __init__(self, dictionary=None, patterns_file=None, create_patterns=False):
        self.dictionary = dictionary or system_dictionary()
        self.patterns_file = patterns_file or 'system_patterns.json'
        if create_patterns:
            self.create_patterns_file_from_dictionary(self.dictionary, self.patterns_file)

    @property
    def word_patterns(self):
        with open(self.patterns_file) as f:
            return json.loads(f.read())

    def possible_matches(self, word):
        pattern = self.create_word_pattern(word)
        return self.patterns[pattern] if pattern in self.patterns else []

    def create_word_pattern(self, word):
        next_num = 0
        letter_ids = {}
        word_pattern = []
        for letter in word.upper():
            if letter not in letter_ids:
                letter_ids[letter] = str(next_num)
                next_num += 1
            word_pattern.append(letter_ids[letter])
        return '.'.join(word_pattern)

    def create_patterns_file_from_dictionary(self, dictionary, out_file):
        all_patterns = defaultdict(list)
        for word in dictionary:
            pattern = self.create_word_pattern(word)
            all_patterns[pattern].append(word)
        with open(out_file, 'w') as f:
            f.write(json.dumps(all_patterns, sort_keys=True, indent=4))
