Thanh Kha (Tkha)
CSC 254 Assignment 2
Prof. Chen

INCLUDED IN FILE
1. tokenizer.py 
2. c_tests
3. README.txt

COMPILE AND RUN CODE (Mac): 

1. Locate tokenizer.py in directory, inside of a2_tkha.
2. Enter: python tokenizer.py
3. You will be asked to type any C files that's inside of c_tests
	- So you may type "ab.c", "automaton.c", ... "tax.c" (without quotes)
4. Compile the new C file named test_(filename you chose).c by:
	a. gcc test_(filename you chose).c -O
	b. ./a.out

OVERVIEW

The tokenizer is a program written in Python, and it takes in a .c file that contains C-syntax program and converts it into a new .c file through a tokenizing process. The tokenizer takes a user input (String) in the main() and adds it to the path that leads to c_tests, which contains all the .c files to choose from. The .c file is then opened and eliminates every comments and white space lines then starts reading character-by-character. These characters are grouped into individual tokens based on the tokens' description, as described on the assignment pdf. By using a look-ahead method in order to identify the tokens of grouped characters and using the predefined (reserved) words, I was able to put individual tokens into an array, which then outputs each token into a new .c file. 

METHODS DESCRIPTION

Thanh Kha (Tkha)
CSC 254 Assignment 2
Prof. Chen

INCLUDED IN FILE
1. tokenizer.py 
2. c_tests
3. README.txt

COMPILE AND RUN CODE (Mac): 

1. Locate tokenizer.py in directory, inside of a2_tkha.
2. Enter: python tokenizer.py
3. You will be asked to type any C files that's inside of c_tests
	- So you may type "ab.c", "automaton.c", ... "tax.c" (without quotes)
4. Compile the new C file named test_(filename you chose).c by:
	a. gcc test_(filename you chose).c -O
	b. ./a.out

OVERVIEW

The tokenizer is a program written in Python, and it takes in a .c file that contains C-syntax program and converts it into a new .c file through a tokenizing process. The tokenizer takes a user input (String) in the main() and adds it to the path that leads to c_tests, which contains all the .c files to choose from. The .c file is then opened and eliminates every comments and white space lines then starts reading character-by-character. These characters are grouped into individual tokens based on the tokens' description, as described on the assignment pdf. By using a look-ahead method in order to identify the tokens of grouped characters and using the predefined (reserved) words, I was able to put individual tokens into an array, which then outputs each token into a new .c file. 

METHODS DESCRIPTION

main(): 
- Takes in user inputs to read the file to then convert into tokens. 
- Writes the new .c file with with user-defined methods and variables ending with _csc254

read_file():
- Inserts each line of code for scanning into the read_line() method:

read_line():
- Iterates through each character to easily identify which lines are comments, modules, or codes.
- Removes white space, comments, and tokenize modules. 
- Utilized the look-ahead method to identify token types and names

check_token(): identifies each token type and stores user variables and methods. 