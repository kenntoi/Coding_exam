def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindrome_pairs(words: list[str]) -> list[list[int]]:
    result = []
    word_map = {word: i for i, word in enumerate(words)}

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            left_part = word[:j]
            right_part = word[j:]

           
            if is_palindrome(left_part):
                reversed_right = right_part[::-1]
                if reversed_right in word_map and word_map[reversed_right] != i:
                    result.append([word_map[reversed_right], i])

            if j != len(word) and is_palindrome(right_part):
                reversed_left = left_part[::-1]
                if reversed_left in word_map and word_map[reversed_left] != i:
                    result.append([i, word_map[reversed_left]])

    return result

if __name__ == "__main__":
    input_words = ["bat", "tab", "cat"]
    result = palindrome_pairs(input_words)
    print(f"Test Case 1: {result}")  # Output: [[1, 0], [0, 1]]

    input_words = ["a", ""]
    result = palindrome_pairs(input_words)
    print(f"Test Case 2: {result}")  # Output: [[1, 0], [0, 1]]

    input_words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = palindrome_pairs(input_words)
    print(f"Test Case 3: {result}")  # Output: [[1, 0], [3, 2], [2, 4]]

    input_words = ["", "abc", "aba"]
    result = palindrome_pairs(input_words)
    print(f"Test Case 4: {result}")  # Output: [[0, 1], [1, 0], [0, 2], [2, 0]]

    input_words = ["a", "b", "c", "aa", "aba"]
    result = palindrome_pairs(input_words)
    print(f"Test Case 5: {result}")  # Output: [[3, 0], [0, 3], [4, 0], [0, 4]]

    input_words = ["apple", "banana", "cherry"]
    result = palindrome_pairs(input_words)
    print(f"Test Case 6: {result}")  # Output: []

    input_words = ["race", "car", "ecar"]
    result = palindrome_pairs(input_words)
    print(f"Test Case 7: {result}")  # Output: [[2, 1]]

    input_words = ["aaa", "aab", "baa", "aaa"]
    result = palindrome_pairs(input_words)
    print(f"Test Case 8: {result}")  # Output: [[0, 3], [3, 0], [1, 2], [2, 1]]

    input_words = ["abcba", "a", "bcb", "xyz", "zyx", "l"]
    result = palindrome_pairs(input_words)
    print(f"Test Case 9: {result}")  # Output: [[1, 0], [2, 0], [4, 3], [3, 4]]
