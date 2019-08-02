import re
from collections import defaultdict

import aiofiles


class WordCounter(object):
    # This pattern takes into account all non-alphanumeric characters
    # excluding "_" since it do counts as a "letter" most of the times.
    # but including ' (apostrophes), since I decided to think about the words
    # with apostrophes as an actual words.
    # otherwise we would have a word "s" with some count,
    # which does not make any sense.
    pattern = re.compile("[^\w']")

    # "magic" methods aren't designed to work asynchronously
    # but I don't need to have workarounds exactly here, fortunately
    def __init__(self, input_file_name, 
                output_file_name = None,
                return_output = False):
        # instead of passing arguments around I decided to keep track of
        # some values as class attributes.
        # should provide some flexibility, without the need to change stuff
        # in multiple places in the code.
        # But maybe it is antipattern, and the code proves itself unclear.
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.return_output = return_output

    async def process_file(self):
        await self.count_words()

        if self.return_output:
            return (self.words_count, self.sorted_words)

        await self.process_output_data()

    async def count_words(self):
        # The defaultdict just allows us append new, nonexisting key
        # in more nicer way than "if not key in dict" or "if not dict.get(key)"
        self.words_count = defaultdict(int)

        try:
            # usage of asyncronous file IO
            async with aiofiles.open(self.input_file_name,
                                    encoding="utf8") as input_file:
                async for line in input_file:
                    # using our regex we could substitude
                    # all not required characters
                    for word in self.pattern.sub(' ', 
                                    line.lower()).split():
                        self.words_count[word] += 1
        except FileNotFoundError as exception:
            print(f"The program experienced an error: {exception.strerror}")
            print(f"While trying to open the file \"{self.input_file_name}\"")
            exit(1)

        self.sorted_words = [f"{word[0]}: {word[1]}\n" for word in sorted(
                            self.words_count.items(), 
                            key=lambda item: (-item[1], item[0])
                            )]

    async def process_output_data(self):
        if self.output_file_name:
            await self.write_in_output_file()
        else:
            self.print_on_screen()

    def print_on_screen(self):
        for word in self.sorted_words:
            print(word, end="")

    # another usage of asyncronous file IO
    async def write_in_output_file(self):
        try:
            async with aiofiles.open(self.output_file_name, "w+", 
                                    encoding="utf8") as output_file:
                await output_file.writelines(self.sorted_words)
        except OSError as exception:
            print(f"The program experienced an error: {exception.strerror}")
            print(f"While writing to the file \"{self.output_file_name}\"")
            exit(1)
