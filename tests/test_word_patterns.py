import json
import os
import tempfile
import unittest

from word_patterns import Patterns


class WordPatternTests(unittest.TestCase):

    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        patterns_file = os.path.join(self.td.name, 'x.json')
        dictionary = ['A', 'AA', 'B', 'AB']
        self.patterns = Patterns(dictionary=dictionary, patterns_file=patterns_file, create_patterns=True)

    def tearDown(self):
        self.td.cleanup()

    def test_create_word_pattern(self):
        word = 'ABC'
        expected_pattern = '0.1.2'
        pattern = self.patterns.create_word_pattern(word)
        self.assertEqual(pattern, expected_pattern)

    def test_multiples_of_a_letter_get_same_number(self):
        word = 'AAAA'
        expected_pattern = '0.0.0.0'
        pattern = self.patterns.create_word_pattern(word)
        self.assertEqual(pattern, expected_pattern)

    def test_increments_correctly_even_when_repeating_letters(self):
        word = 'ABCABD'
        expected_pattern = '0.1.2.0.1.3'
        pattern = self.patterns.create_word_pattern(word)
        self.assertEqual(pattern, expected_pattern)

    def test_create_patterns_file_from_dictionary(self):
        output = self.patterns.word_patterns
        expected_dict = json.loads('{"0": ["A", "B"], "0.0": ["AA"], "0.1": ["AB"]}')
        self.assertEqual(output, expected_dict)

    def test_find_all_possible_matches_in_dictionary(self):
        word = '@'
        matches = self.patterns.possible_matches(word)
        self.assertEqual(matches, ['A', 'B'])

    def test_returns_empty_list_if_no_pattern_match(self):
        word = '@' * 5
        matches = self.patterns.possible_matches(word)
        self.assertEqual(matches, [])
