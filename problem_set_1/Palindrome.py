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
    print(result)  # Output: [[1, 0], [0, 1]]
