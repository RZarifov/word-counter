import asyncio

import aiounittest

from word_counter import WordCounter
from collections import defaultdict


class WordCounterTests(aiounittest.AsyncTestCase):
    async def test_word_counter(self):
        expected_dict = defaultdict(int, {"this": 3, "is": 3, "a": 3, "test": 2, "text": 3, "that": 1, "need": 1, "to": 1, "pass": 1, "the": 2, "and": 2, "yet": 1, "another": 2, "line": 2, "with": 2, "amazing": 1, "right": 1, "words": 1, "of": 1, "various": 1, "case": 1, "test's": 1, "parser's": 1, "text's": 1, "what_about_this": 1, "также": 3, "как": 1, "текст": 1, "на": 1, "русском": 1, "языке": 2})

        expected_sorted_words = ['a: 3\n', 'is: 3\n', 'text: 3\n', 'this: 3\n', 'также: 3\n', 'and: 2\n', 'another: 2\n', 'line: 2\n', 'test: 2\n', 'the: 2\n', 'with: 2\n', 'языке: 2\n', 'amazing: 1\n', 'case: 1\n', 'need: 1\n', 'of: 1\n', "parser's: 1\n", 'pass: 1\n', 'right: 1\n', "test's: 1\n", "text's: 1\n", 'that: 1\n', 'to: 1\n', 'various: 1\n', 'what_about_this: 1\n', 'words: 1\n', 'yet: 1\n', 'как: 1\n', 'на: 1\n', 'русском: 1\n', 'текст: 1\n']

        word_counter = WordCounter("file.txt", return_output = True)
        output = await word_counter.process_file()
        self.assertEqual(output[0], expected_dict)
        self.assertEqual(output[1], expected_sorted_words)
