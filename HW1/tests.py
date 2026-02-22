import unittest
from problems import (
    hello_name,
    calculate_area,
    sum_to_n,
    list_sum,
    filter_even,
    count_vowels,
    reverse_string,
    is_palindrome,
    max_value,
    merge_dicts,
    two_sum,
    valid_parentheses,
    max_subarray_sum,
    longest_substring_without_repeating,
    group_anagrams,
)

class TestHW1(unittest.TestCase):

    # 1. Hello Name
    def test_hello_name_basic(self):
        self.assertEqual(hello_name("Alice"), "Hello, Alice!")
        self.assertEqual(hello_name("Bob"), "Hello, Bob!")

    def test_hello_name_complex(self):
        self.assertEqual(hello_name("Christopher"), "Hello, Christopher!")

    def test_hello_name_edge(self):
        # Taking "World" as a generic edge case from examples
        self.assertEqual(hello_name("World"), "Hello, World!")
        # Test with spaces
        self.assertEqual(hello_name("Mr. Smith"), "Hello, Mr. Smith!")

    # 2. Calculate Area
    def test_calculate_area_basic(self):
        self.assertEqual(calculate_area(5, 3), 15)
        self.assertEqual(calculate_area(10, 10), 100)

    def test_calculate_area_float(self):
        self.assertAlmostEqual(calculate_area(2.5, 4.0), 10.0)
        self.assertAlmostEqual(calculate_area(2, 0.5), 1.0)

    def test_calculate_area_large(self):
        self.assertEqual(calculate_area(1000, 2000), 2000000)

    # 3. Sum to N
    def test_sum_to_n_basic(self):
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(3), 6)

    def test_sum_to_n_edge(self):
        self.assertEqual(sum_to_n(1), 1)

    def test_sum_to_n_large(self):
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(10), 55)

    # 4. List Sum
    def test_list_sum_basic(self):
        self.assertEqual(list_sum([1, 2, 3]), 6)
        self.assertEqual(list_sum([10, 20, 30]), 60)

    def test_list_sum_negative(self):
        self.assertEqual(list_sum([-1, 0, 1]), 0)
        self.assertEqual(list_sum([-5, -5]), -10)

    def test_list_sum_empty(self):
        self.assertEqual(list_sum([]), 0)

    # 5. Filter Even
    def test_filter_even_basic(self):
        self.assertEqual(filter_even([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_even([10, 20, 30]), [10, 20, 30])

    def test_filter_even_none(self):
        self.assertEqual(filter_even([1, 3, 5]), [])

    def test_filter_even_mixed_negative(self):
        self.assertEqual(filter_even([-2, -1, 0, 1, 2]), [-2, 0, 2])

    def test_filter_even_empty(self):
        self.assertEqual(filter_even([]), [])

    # 6. Count Vowels
    def test_count_vowels_basic(self):
        self.assertEqual(count_vowels("Hello"), 2)
        self.assertEqual(count_vowels("Python"), 1)

    def test_count_vowels_case_insensitive(self):
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("aEiOu"), 5)

    def test_count_vowels_none(self):
        self.assertEqual(count_vowels("Crypt"), 0)
        self.assertEqual(count_vowels("123"), 0)

    def test_count_vowels_empty(self):
        self.assertEqual(count_vowels(""), 0)

    # 7. Reverse String
    def test_reverse_string_basic(self):
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_string_capitalized(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_reverse_string_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")

    # 8. Is Palindrome
    def test_is_palindrome_basic(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))

    def test_is_palindrome_case_punctuation(self):
        self.assertTrue(is_palindrome("Race car"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_is_palindrome_empty(self):
        # An empty string reads the same forwards and backwards
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_single_char(self):
        self.assertTrue(is_palindrome("a"))

    # 9. Max Value
    def test_max_value_basic(self):
        self.assertEqual(max_value([1, 2, 3]), 3)
        self.assertEqual(max_value([10, 5, 8, 3]), 10)

    def test_max_value_negative(self):
        self.assertEqual(max_value([-5, -1, -10]), -1)
        self.assertEqual(max_value([-10, -20, -30]), -10)

    def test_max_value_single(self):
        self.assertEqual(max_value([42]), 42)

    def test_max_value_duplicates(self):
        self.assertEqual(max_value([5, 5, 5]), 5)

    # 10. Merge Dicts
    def test_merge_dicts_basic(self):
        d1 = {"a": 1, "b": 2}
        d2 = {"c": 3, "d": 4}
        expected = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.assertEqual(merge_dicts(d1, d2), expected)

    def test_merge_dicts_overlap(self):
        d1 = {"a": 1, "b": 2}
        d2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 3, "c": 4}
        self.assertEqual(merge_dicts(d1, d2), expected)

    def test_merge_dicts_empty(self):
        self.assertEqual(merge_dicts({}, {"a": 1}), {"a": 1})
        self.assertEqual(merge_dicts({"a": 1}, {}), {"a": 1})
        self.assertEqual(merge_dicts({}, {}), {})

    # 11. Two Sum
    def test_two_sum_basic(self):
        self.assertEqual(sorted(two_sum([2, 7, 11, 15], 9)), [0, 1])
        self.assertEqual(sorted(two_sum([3, 2, 4], 6)), [1, 2])

    def test_two_sum_duplicate_values(self):
        # Requires picking two different indices even if values are same
        self.assertEqual(sorted(two_sum([3, 3], 6)), [0, 1])

    def test_two_sum_negative(self):
        self.assertEqual(sorted(two_sum([-1, -2, -3, -4, -5], -8)), [2, 4])

    # 12. Valid Parentheses
    def test_valid_parentheses_basic(self):
        self.assertTrue(valid_parentheses("()"))
        self.assertTrue(valid_parentheses("()[]{}"))
        self.assertTrue(valid_parentheses("{[]}"))

    def test_valid_parentheses_invalid(self):
        self.assertFalse(valid_parentheses("(]"))
        self.assertFalse(valid_parentheses("([)]"))
        self.assertFalse(valid_parentheses("]"))

    def test_valid_parentheses_empty(self):
        self.assertTrue(valid_parentheses(""))

    def test_valid_parentheses_nested(self):
        self.assertTrue(valid_parentheses("((()))"))
        self.assertTrue(valid_parentheses("({[]})"))

    # 13. Max Subarray Sum
    def test_max_subarray_sum_basic(self):
        self.assertEqual(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(max_subarray_sum([1]), 1)

    def test_max_subarray_sum_all_positive(self):
        self.assertEqual(max_subarray_sum([5, 4, 1, 7, 8]), 25)

    def test_max_subarray_sum_all_negative(self):
        # Should pick the single largest element (least negative)
        self.assertEqual(max_subarray_sum([-5, -2, -9, -1, -8]), -1)

    def test_max_subarray_sum_mixed(self):
        self.assertEqual(max_subarray_sum([1, -2, 3, 4, -1, 2, 1, -5, 4]), 9)

    # 14. Longest Substring Without Repeating
    def test_longest_substring_basic(self):
        self.assertEqual(longest_substring_without_repeating("abcabcbb"), 3)
        self.assertEqual(longest_substring_without_repeating("bbbbb"), 1)
        self.assertEqual(longest_substring_without_repeating("pwwkew"), 3)

    def test_longest_substring_empty(self):
        self.assertEqual(longest_substring_without_repeating(""), 0)

    def test_longest_substring_full_unique(self):
        self.assertEqual(longest_substring_without_repeating("abcdef"), 6)

    def test_longest_substring_spaces(self):
        self.assertEqual(longest_substring_without_repeating("a b c"), 3) # "a b" or "b c"

    # 15. Group Anagrams
    def test_group_anagrams_basic(self):
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        # We need to sort to compare because order doesn't matter
        result = group_anagrams(input_strs)
        
        # Sort inner lists and outer list for comparison
        sorted_result = sorted([sorted(x) for x in result])
        sorted_expected = sorted([sorted(x) for x in expected])
        
        self.assertEqual(sorted_result, sorted_expected)

    def test_group_anagrams_empty_string(self):
        self.assertEqual(group_anagrams([""]), [[""]])

    def test_group_anagrams_single_char(self):
        self.assertEqual(group_anagrams(["a"]), [["a"]])

    def test_group_anagrams_no_anagrams(self):
        input_strs = ["abc", "def", "ghi"]
        res = group_anagrams(input_strs)
        # Should be 3 groups of 1
        self.assertEqual(len(res), 3)

if __name__ == '__main__':
    # Define ANSI color codes
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Mapping of test method prefixes to Problem Names
    problem_map = {
        "hello_name": "1. Hello Name",
        "calculate_area": "2. Calculate Area",
        "sum_to_n": "3. Sum to N",
        "list_sum": "4. List Sum",
        "filter_even": "5. Filter Even",
        "count_vowels": "6. Count Vowels",
        "reverse_string": "7. Reverse String",
        "is_palindrome": "8. Is Palindrome",
        "max_value": "9. Max Value",
        "merge_dicts": "10. Merge Dictionaries",
        "two_sum": "11. Two Sum",
        "valid_parentheses": "12. Valid Parentheses",
        "max_subarray_sum": "13. Max Subarray Sum",
        "longest_substring": "14. Longest Substring",
        "group_anagrams": "15. Group Anagrams"
    }

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHW1)
    
    # Organize tests by problem
    problem_tests = {name: [] for name in problem_map.values()}
    
    for test in suite:
        method_name = test._testMethodName
        # Extract the problem key from test_problem_name_...
        # We skip 'test_' (5 chars) and try to match with keys
        name_part = method_name[5:]
        
        assigned_problem = "Unknown Problem"
        # Find the longest matching prefix to handle overlapping names if any
        best_match_len = 0
        
        for key, problem_name in problem_map.items():
            if name_part.startswith(key):
                if len(key) > best_match_len:
                    best_match_len = len(key)
                    assigned_problem = problem_name
        
        if assigned_problem != "Unknown Problem":
            problem_tests[assigned_problem].append(test)

    # Run tests and collect results
    print(f"\n{BOLD}Running HW1 Tests...{RESET}\n")
    
    total_passed_overall = 0
    total_tests_overall = 0
    
    # Store summaries to print at the end
    problem_summaries = []

    for problem_key, problem_display_name in problem_map.items():
        relevant_tests = []
        for test in suite:
            method_name = test._testMethodName
            if method_name.startswith("test_" + problem_key):
                 relevant_tests.append(test)
                 
        if not relevant_tests:
            continue
            
        passed = 0
        total = len(relevant_tests)
        problem_failures = []
        
        for test in relevant_tests:
            result = unittest.TestResult()
            test.run(result)
            if result.wasSuccessful():
                passed += 1
            else:
                failures = result.failures + result.errors
                for test_case, trace in failures:
                    problem_failures.append((test_case, trace))
        
        # Print failures as they happen
        if problem_failures:
            print(f"{BOLD}{problem_display_name} Failures:{RESET}")
            for test_case, trace in problem_failures:
                 print(f"  {RED}FAIL: {test_case._testMethodName}{RESET}")
                 # Indent the traceback
                 indented_trace = "\n".join("    " + line for line in trace.splitlines())
                 print(indented_trace)
                 print()
        
        # Store summary for later
        problem_summaries.append((problem_display_name, passed, total))

        total_passed_overall += passed
        total_tests_overall += total

    print("-" * 40)
    print(f"{BOLD}Summary:{RESET}")
    for name, passed, total in problem_summaries:
        if passed == total:
            color = GREEN
        elif passed == 0:
            color = RED
        else:
            color = RED 
            
        print(f"{name:<30} {color}[{passed}/{total}]{RESET}")

    print("-" * 40)
    final_color = GREEN if total_passed_overall == total_tests_overall else RED
    print(f"{BOLD}Total Progress:{RESET} {final_color}[{total_passed_overall}/{total_tests_overall}]{RESET}")
