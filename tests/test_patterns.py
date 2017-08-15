import unittest

from test_helpers.helpers import create_pattern_dict
from word_patterns import create_word_pattern


class PatternsTests(unittest.TestCase):

    def test_find_words_with_common_letters(self):
        dictionary = ['dumbo', 'rabbit', 'corn', 'hold']
        pattern_dict = create_pattern_dict(dictionary)
        word1 = 'ABRYZ'
        word2 = 'CEIA'
        self.fail('x')