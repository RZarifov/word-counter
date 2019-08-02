#### Info
The purpose of this example code is to count the words in a given file using a command line.\
The word count also takes into respect an alphabetical order of words, not only the word count alone.\
The code is overengineered on purpose, and doesn't indicate that the actual production code will be overengineered in the same manner.

#### Usage
The given example uses pipenv as it's environment handler, therefore it must be installed on the system: \
`pip install pipenv`

After pipenv successfully installed you can launch a virtual environment: \
`pipenv shell`

And install dependencies by running: \
`pipenv install`

After that, you're ready to roll:
##### Testing: 
`python -m unittest`

##### Running a script: 
Example 1: `python main.py file.txt` \
Example 2: `python main.py ~/The_Old_Man_and_the_Sea-Ernest_Hemingway.txt --output_file ~/output.txt` \
 \
_"Example 2" shows a way to output the processed data into a file._
