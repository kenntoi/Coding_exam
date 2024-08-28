def lengthOfLIS(nums: list[int]) -> int:
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Test cases
if __name__ == "__main__":
    # Test Case 1: Basic Case
    input_numbers = [10, 9, 2, 5, 3, 7, 101, 18]
    result = lengthOfLIS(input_numbers)
    print(f"Test Case 1: {result}")  #  Expected Output: 4

    input_numbers = [1, 2, 3, 4, 5]
    result = lengthOfLIS(input_numbers)
    print(f"Test Case 2: {result}")  # Expected Output: 5
 
    input_numbers = [5, 5, 5, 5, 5]
    result = lengthOfLIS(input_numbers)
    print(f"Test Case 3: {result}")  # Expected Output: 1

    input_numbers = [10]
    result = lengthOfLIS(input_numbers)
    print(f"Test Case 4: {result}")  # Expected Output: 1

    input_numbers = [5, 4, 3, 2, 1]
    result = lengthOfLIS(input_numbers)
    print(f"Test Case 5: {result}")  # Expected Output: 1

    input_numbers = []
    result = lengthOfLIS(input_numbers)
    print(f"Test Case 6: {result}")  # Expected Output: 0

    input_numbers = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    result = lengthOfLIS(input_numbers)
    print(f"Test Case 7: {result}")  # Expected Output: 6

    input_numbers = [3, 10, 2, 1, 20]
    result = lengthOfLIS(input_numbers)
    print(f"Test Case 8: {result}")  # ExpectedOutput: 3

    input_numbers = [1, 3, 2, 4, 3, 5]
    result = lengthOfLIS(input_numbers)
    print(f"Test Case 9: {result}")  # Expected Output: 4

    input_numbers = [2, 2, 2, 2, 2, 2, 3]
    result = lengthOfLIS(input_numbers)
    print(f"Test Case 10: {result}")  # Expected Output: 2