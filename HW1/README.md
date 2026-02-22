# HW1 - Python Fundamentals

This assignment contains a series of Python coding problems designed to test your understanding of basic concepts as well as some more advanced algorithmic thinking.

## Instructions

1. Open `HW1/problems.py`.
2. Implement each function, replacing the `raise NotImplementedError` with your code.
3. Ensure your functions return the expected values.

---

## 1. Hello Name

Implement a function `hello_name(name)` that returns a greeting string "Hello, {name}!".

**Difficulty:** Easy

**Input:** A string `name`.

**Output:** A string "Hello, {name}!".

**Constraints:** `name` will be a non-empty string.

**Examples:**
1. `hello_name("Alice")` -> `"Hello, Alice!"`
2. `hello_name("Bob")` -> `"Hello, Bob!"`
3. `hello_name("World")` -> `"Hello, World!"`

---

## 2. Calculate Area

Implement a function `calculate_area(length, width)` that returns the area of a rectangle given its length and width.

**Difficulty:** Easy

**Input:** Two numbers, `length` and `width`.

**Output:** The product of `length` and `width`.

**Constraints:** `length` and `width` will be positive numbers.

**Examples:**
1. `calculate_area(5, 3)` -> `15`
2. `calculate_area(10, 10)` -> `100`
3. `calculate_area(2, 0.5)` -> `1.0`

---

## 3. Sum to N

Implement a function `sum_to_n(n)` that returns the sum of all integers from 1 to `n` (inclusive).

**Difficulty:** Easy

**Input:** An integer `n`.

**Output:** The sum of integers from 1 to `n`.

**Constraints:** `n` will be a positive integer.

**Examples:**
1. `sum_to_n(5)` -> `15`
2. `sum_to_n(1)` -> `1`
3. `sum_to_n(10)` -> `55`

---

## 4. List Sum

Implement a function `list_sum(numbers)` that returns the sum of all elements in the given list.

**Difficulty:** Easy

**Input:** A list of integers.

**Output:** The sum of all elements in the list.

**Constraints:** The list can contain positive or negative integers. The list may be empty (sum is 0).

**Examples:**
1. `list_sum([1, 2, 3])` -> `6`
2. `list_sum([-1, 0, 1])` -> `0`
3. `list_sum([])` -> `0`

---

## 5. Filter Even

Implement a function `filter_even(numbers)` that returns a new list containing only the even numbers from the input list.

**Difficulty:** Easy

**Input:** A list of integers.

**Output:** A new list containing only the even integers from the input.

**Constraints:** The input list can contain any integers.

**Examples:**
1. `filter_even([1, 2, 3, 4, 5, 6])` -> `[2, 4, 6]`
2. `filter_even([1, 3, 5])` -> `[]`
3. `filter_even([10, 20, 30])` -> `[10, 20, 30]`

---

## 6. Count Vowels

Implement a function `count_vowels(text)` that returns the count of vowels (a, e, i, o, u) in the given text (case-insensitive).

**Difficulty:** Easy

**Input:** A string.

**Output:** The count of vowels ('a', 'e', 'i', 'o', 'u') in the string.

**Constraints:** Input string may contain letters, numbers, and symbols.

**Examples:**
1. `count_vowels("Hello")` -> `2`
2. `count_vowels("Python")` -> `1`
3. `count_vowels("AEIOU")` -> `5`

---

## 7. Reverse String

Implement a function `reverse_string(text)` that returns the reversed version of the input string.

**Difficulty:** Easy

**Input:** A string.

**Output:** The string in reverse order.

**Constraints:** Input string may be empty.

**Examples:**
1. `reverse_string("abc")` -> `"cba"`
2. `reverse_string("Python")` -> `"nohtyP"`
3. `reverse_string("")` -> `""`

---

## 8. Is Palindrome

Implement a function `is_palindrome(text)` that returns True if the input text is a palindrome, False otherwise. A palindrome reads the same forwards and backwards. You should ignore case and non-alphanumeric characters.

**Difficulty:** Medium

**Input:** A string.

**Output:** `True` if the string is a palindrome, `False` otherwise.

**Constraints:** Input string may contain any characters.

**Examples:**
1. `is_palindrome("Race car")` -> `True`
2. `is_palindrome("hello")` -> `False`
3. `is_palindrome("A man, a plan, a canal: Panama")` -> `True`

---

## 9. Max Value

Implement a function `max_value(numbers)` that finds the maximum value in the list without using the built-in `max()` function.

**Difficulty:** Easy

**Input:** A list of integers.

**Output:** The largest integer in the list.

**Constraints:** The list will contain at least one integer.

**Examples:**
1. `max_value([10, 5, 8, 3])` -> `10`
2. `max_value([-5, -1, -10])` -> `-1`
3. `max_value([42])` -> `42`

---

## 10. Merge Dictionaries

Implement a function `merge_dicts(d1, d2)` that merges two dictionaries. If a key exists in both, the value from `d2` should be used.

**Difficulty:** Easy

**Input:** Two dictionaries, `d1` and `d2`.

**Output:** A new dictionary containing all keys from both.

**Constraints:** Keys can be strings or numbers. Values can be any type.

**Examples:**
1. `merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})` -> `{"a": 1, "b": 3, "c": 4}`
2. `merge_dicts({"x": 10}, {"y": 20})` -> `{"x": 10, "y": 20}`
3. `merge_dicts({}, {"a": 1})` -> `{"a": 1}`

---

## 11. Two Sum

This is a classic algorithmic problem. Implement a function `two_sum(nums, target)` that returns indices of the two numbers in the array `nums` such that they add up to `target`.

**Difficulty:** Medium

**Input:** An array of integers `nums` and an integer `target`.

**Output:** A list containing two integers representing the indices of the solution.

**Constraints:** Each input will have exactly one solution.
You may not use the same element twice.
Time complexity should ideally be O(n).

**Examples:**
1. `two_sum([2, 7, 11, 15], 9)` -> `[0, 1]`
2. `two_sum([3, 2, 4], 6)` -> `[1, 2]`
3. `two_sum([3, 3], 6)` -> `[0, 1]`

---

## 12. Valid Parentheses

Implement a function `valid_parentheses(s)` that determines if the input string is valid. The string contains characters '(', ')', '{', '}', '[' and ']'.
Validity means:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Difficulty:** Medium

**Input:** A string `s` containing just the characters '(', ')', '{', '}', '[' and ']'.

**Output:** `True` if the string is valid, `False` otherwise.

**Constraints:** The string contains only parentheses characters.
String length <= 10^4.

**Examples:**
1. `valid_parentheses("()[]{}")` -> `True`
2. `valid_parentheses("(]")` -> `False`
3. `valid_parentheses("{[]}")` -> `True`

---

## 13. Maximum Subarray Sum

Implement a function `max_subarray_sum(nums)` that finds the contiguous subarray (containing at least one number) which has the largest sum and returns its sum. This problem is often solved using Kadane's Algorithm.

**Difficulty:** Medium

**Input:** An integer array `nums`.

**Output:** The largest sum of a contiguous subarray.

**Constraints:** Array length >= 1.
Can contain negative numbers.
Time complexity should ideally be O(n).

**Examples:**
1. `max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])` -> `6`
2. `max_subarray_sum([1])` -> `1`
3. `max_subarray_sum([5,4,-1,7,8])` -> `23`

---

## 14. Longest Substring Without Repeating Characters

Implement a function `longest_substring_without_repeating(s)` that finds the length of the longest substring without repeating characters.

**Difficulty:** Medium

**Input:** A string `s`.

**Output:** The length of the longest substring without repeating characters.

**Constraints:** String consists of English letters, digits, symbols and spaces.
String length <= 5 * 10^4.

**Examples:**
1. `longest_substring_without_repeating("abcabcbb")` -> `3`
2. `longest_substring_without_repeating("bbbbb")` -> `1`
3. `longest_substring_without_repeating("pwwkew")` -> `3`

---

## 15. Group Anagrams

Implement a function `group_anagrams(strs)` that groups an array of strings into anagrams. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Difficulty:** Medium

**Input:** An array of strings `strs`.

**Output:** A list of lists of strings, where each inner list contains words that are anagrams of each other.

**Constraints:** All inputs will be lowercase English letters.
The order of the output groups does not matter.

**Examples:**
1. `group_anagrams(["eat","tea","tan","ate","nat","bat"])` -> `[["bat"],["nat","tan"],["ate","eat","tea"]]`
2. `group_anagrams([""])` -> `[[""]]`
3. `group_anagrams(["a"])` -> `[["a"]]`
