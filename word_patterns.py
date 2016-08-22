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
        return self.word_patterns[pattern] if pattern in self.word_patterns else []

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

    def contains_matching_letters(self, word1, word2):
        return not set(word1).isdisjoint(set(word2))

    def intersect_locations(self, word1, word2):
        intersections = {}
        for idx, i in enumerate(word1):
            try:
                intersections[idx] = word2.index(i)
            except ValueError:
                pass
        return intersections

    # get possible_matches() for each word
    # find which cypher letters are the same in word1 and word2
    # find which words in matches1 where letter in position of word1 has same letter as words in matches2 that has same letter

    def filter(self, cypher1, cypher2):
        # if not contains_matching_letters(word1, word2):
        #     return {}
        print('c1:', cypher1, 'c2:', cypher2)
        intersects = self.intersect_locations(cypher1, cypher2)
        print('INT:', intersects)
        possible_letters = defaultdict(set)
        for l1, l2 in intersects.items():
            print(l1, l2)
            letters1 = {x[l1] for x in self.possible_matches(cypher1)}
            print('L1:', letters1)
            letters2 = {y[l2] for y in self.possible_matches(cypher2)}
            print('L2:', letters2)
            print('cyph:', cypher1[l1])
            possible_letters[cypher1[l1]] = letters1.union(letters2)
        return possible_letters
