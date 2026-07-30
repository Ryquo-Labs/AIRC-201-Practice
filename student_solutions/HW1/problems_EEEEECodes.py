def hello_name(name: str) -> str:
    return "Hello, "+str(name)+"!"

def calculate_area(length: float, width: float) -> float:
    return length * width

def sum_to_n(n: int) -> int:
    return round(n * (n + 1) / 2)

def list_sum(numbers: list[int]) -> int:
    total = 0
    for i in numbers:
        total += i
    return total
# I lowk forgot abt sum() but I'll leave it rn

def filter_even(numbers: list[int]) -> list[int]:
    out = []
    for num in numbers:
        if num % 2 == 0:
            out.append(num)
    return out

def count_vowels(text: str) -> int:
    c = 0
    for char in text:
        if char in 'aeiouAEIOU':
            c += 1
    return c

def reverse_string(text: str) -> str:
    return text[::-1]

def is_palindrome(text: str) -> bool:
    """
    Returns True if the input text is a palindrome, False otherwise.
    Ignores case and non-alphanumeric characters.
    """
    imput = ''.join(c.lower() for c in text if c.isalnum())
    return imput == imput[::-1]

def max_value(numbers: list[int]) -> int:
    """
    Returns the maximum value in the list without using the built-in max() function.
    """
    if not numbers:
        raise ValueError("The list is empty")
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

def merge_dicts(d1: dict, d2: dict) -> dict:
    """
    Merges two dictionaries. Values from d2 overwrite d1 if keys overlap.
    Returns a new dictionary.
    """
    merged = d1.copy()
    merged.update(d2)
    return merged

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    raise ValueError("No two sum solution")

def valid_parentheses(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    """
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            return False
    return not stack

def max_subarray_sum(nums: list[int]) -> int:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    """
    if not nums:
        raise ValueError("The list is empty")
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def longest_substring_without_repeating(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """
    char_index = {}
    longest = 0
    start = 0
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        longest = max(longest, i - start + 1)
    return longest

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    """
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    return list(anagrams.values())
