import os
import tempfile
import unittest

from word_patterns import Patterns


class FilterTests(unittest.TestCase):

    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.patterns_file = os.path.join(self.td.name, 'x.json')
        dictionary = ['A', 'AA', 'B', 'AB']
        self.patterns = Patterns(dictionary=dictionary, patterns_file=self.patterns_file, create_patterns=True)

    def test_unittest_matching_letters(self):
        word1 = 'abc'
        word2 = 'cde'
        word3 = 'zyx'
        self.assertTrue(self.patterns.contains_matching_letters(word1, word2))
        self.assertFalse(self.patterns.contains_matching_letters(word1, word3))

    def test_unittest_intersect_positions(self):
        word1 = 'abc'
        word2 = 'cxcwiao'
        isect = self.patterns.intersect_positions(word1, word2)
        self.assertEqual({0: 5, 2: 0}, isect)

    def test_unittest_intersect_positions_returns_empty_dict_if_no_intersection(self):
        word1 = 'abc'
        word2 = 'xewio'
        isect = self.patterns.intersect_positions(word1, word2)
        self.assertEqual({}, isect)

    def test_filter_to_matching(self):
        word1 = '12345'
        word2 = '631'
        dictionary = ['ABCDE', 'FCA']
        patterns = Patterns(dictionary=dictionary, patterns_file=self.patterns_file, create_patterns=True)
        results = patterns.filter(word1, word2)
        self.assertEqual({'1': {'A'}, '3': {'C'}}, results)
        print(results)
        self.fail('x')
