# Problem Set 1: Palindrome Pairs
## Problem Description
#### Given a list of unique words, your task is to find all pairs of distinct indices (i, j) in the list so that
the concatenation of the two words, i.e., words[i] + words[j], forms a palindrome.
## Solution
##### 1.Define 'is_palindrome' Function to check if a string is a palindrom.
2. Create 'word_map' to map each word to its index in the list.
3. For each word, consider Every Possible split into two parts: 'left_part' and 'right_part'.
4. Check the indces to avoid pairing word by itself
5. Return all valid pairs.
## How to Run (python required)
#### 1. Double click the 'palindrome.py' file in Windows Explorer to run it. Howecer, the terminal
window might close immediately after execution so its better to run it from the command prompt to see the output.
### Using Command Prompt
#### 1. Open Command Prompt
2. Navigate to the directory where palindrome.py is located using cd command. example. 'cd path/to/palindrome.py
3. Run the file by typing Python palindrome.py.
