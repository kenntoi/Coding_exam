def is_valid(s: str) -> bool:
    
    stack = []
    
    matching_brackets = {')': '(', '}': '{', ']': '['}

    
    for char in s:
        if char in matching_brackets.values():
            
            stack.append(char)
        elif char in matching_brackets.keys():
            
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False
        else:
            
            continue

    return not stack


if __name__ == "__main__":
    input_string1 = "()[]{}"
    print(is_valid(input_string1))  # Output: True

    input_string2 = "([)]"
    print(is_valid(input_string2))  # Output: False

    input_string3 = "{[]}"
    print(is_valid(input_string3))  # Output: True
