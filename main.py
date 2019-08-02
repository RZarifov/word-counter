"""
Script input is a text file and the output is statistics of word occurrences. As a result, the program must print out all unique words from the text with the number of their occurrences. 

Words in output must be sorted by number of their occurrences in descending order, words with the equal number of occurrences must be sorted in alphabetic order.

Each word and number of its occurrences must be printed on a new line in format: <word>: <frequency>.
"""

import asyncio
import argparse

from word_counter import WordCounter


async def main(args):
    word_counter = WordCounter(args.input_file, args.output_file)
    await word_counter.process_file()

# This script file MAYBE should not exist,
# and these lines should be present in word_counter.py file,
# but I'll leave them here anyway.
if __name__ == "__main__":
    # It is not required to use argparse for this task,
    # and we could just go with good old sys.argv,
    # but I would like to please the potential employer, to let him know
    # that I do posses some knowledge about built-in python library
    parser = argparse.ArgumentParser(description='Word frequency counter.')
    parser.add_argument(
        'input_file', metavar='input_file', type=str,
        help='Provide a file to process')
    # optional --output file argument
    parser.add_argument('--output_file', metavar='output_file', type=str,
        help='Provide optional output file')

    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args))
    loop.close()
