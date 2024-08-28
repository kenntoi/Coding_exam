## 3. Longest Increasing Subsequence
### Problem Description:
##### Given an unsorted array of integers, find the length of the longest increasing subsequence
## Solution
####
1. Set 'dp' array to 1
2. For the nested loop, the outer loop iterates through each lements 'i' in 'nums'. The inner loop check all previous elements
   'j' to see if nums[i] can extend the sequence ending at num[j].
3. If num[i] > num [j], update dp[i] to be the maximum current value and dp[j] + 1
4. The maximum value in the 'dp' is the lenght of the longest increasing subsequence.
## How to Run (python required)
#### 1. Double click the 'LISlenght.py' file in Windows Explorer to run it. Howecer, the terminal
window might close immediately after execution so its better to run it from the command prompt to see the output.
### Using Command Prompt
#### 
1. Open Command Prompt
2. Navigate to the directory where palindrome.py is located using cd command. example. 'cd path/to/palindrome.py
3. Run the file by typing Python LISlenght.py.
