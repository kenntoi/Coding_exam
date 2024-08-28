# Problem Set 2: Valid Parentheses
## Problem Description
#### Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
## Solution
#### 
1. Use Stack because it allows to keep track of the last opened bracket that hasn't been match yet.
2. If it is and opening bracket, push into the stack, If it is a closing bracket, check if it matches the top element of the stack. If the stack is empty or the the closing bracket does not match the top of the stack the string is invalid.
3. Stack check if the stack is empty, all brackets are match and the string is valid. If stack is not empty, there are umatched bracket so string is invalid.
## How to Run (python required)
#### 1. Double click the 'parentheses.py' file in Windows Explorer to run it. Howecer, the terminal
window might close immediately after execution so its better to run it from the command prompt to see the output.
### Using Command Prompt
#### 
1. Open Command Prompt
2. Navigate to the directory where palindrome.py is located using cd command. example. 'cd path/to/palindrome.py
3. Run the file by typing Python parentheses.py.
