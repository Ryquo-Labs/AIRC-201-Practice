import unittest
import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal
import sys
import os

# Ensure HW2 is in path to import problems_pandas properly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from problems_pandas import (
    get_dataset_shape,
    get_column_names,
    get_summary_statistics,
    get_nth_row,
    filter_by_drink_category,
    get_high_spenders,
    get_mobile_rewards_members,
    get_specific_regions,
)

# Load the whole dataset
csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'starbucks_customer_ordering_patterns.csv')
df_full = pd.read_csv(csv_path)

# Create cuts
datasets = {
    "1-100": df_full.head(100).copy(),
    "1-1000": df_full.head(1000).copy(),
    "1-10000": df_full.head(10000).copy(),
    "Full": df_full.copy()
}

class TestPandasProblems(unittest.TestCase):
    def test_get_dataset_shape(self):
        for name, df in datasets.items():
            with self.subTest(dataset=name):
                expected = df.shape
                self.assertEqual(get_dataset_shape(df), expected)

    def test_get_column_names(self):
        for name, df in datasets.items():
            with self.subTest(dataset=name):
                expected = list(df.columns)
                self.assertEqual(get_column_names(df), expected)

    def test_get_summary_statistics(self):
        for name, df in datasets.items():
            with self.subTest(dataset=name):
                expected = df['total_spend'].describe()
                result = get_summary_statistics(df, 'total_spend')
                assert_series_equal(result, expected)

    def test_get_nth_row(self):
        for name, df in datasets.items():
            with self.subTest(dataset=name):
                # Pick a valid index within bounds
                n = min(42, len(df) - 1)
                expected = df.iloc[n]
                result = get_nth_row(df, n)
                assert_series_equal(result, expected)

    def test_filter_by_drink_category(self):
        for name, df in datasets.items():
            with self.subTest(dataset=name):
                expected = df[df['drink_category'] == 'Brewed Coffee']
                result = filter_by_drink_category(df, 'Brewed Coffee')
                assert_frame_equal(result, expected)

    def test_get_high_spenders(self):
        for name, df in datasets.items():
            with self.subTest(dataset=name):
                expected = df[df['total_spend'] > 15.0]
                result = get_high_spenders(df, 15.0)
                assert_frame_equal(result, expected)

    def test_get_mobile_rewards_members(self):
        for name, df in datasets.items():
            with self.subTest(dataset=name):
                expected = df[(df['order_channel'] == 'Mobile App') & (df['is_rewards_member'] == True)]
                result = get_mobile_rewards_members(df)
                assert_frame_equal(result, expected)

    def test_get_specific_regions(self):
        for name, df in datasets.items():
            with self.subTest(dataset=name):
                regions = ["Northeast", "Southwest"]
                expected = df[df['region'].isin(regions)]
                result = get_specific_regions(df, regions)
                assert_frame_equal(result, expected)


if __name__ == '__main__':
    # Define ANSI color codes
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Mapping of test method prefixes to Problem Names
    problem_map = {
        "get_dataset_shape": "1. Get Dataset Shape",
        "get_column_names": "2. Get Column Names",
        "get_summary_statistics": "3. Get Summary Statistics",
        "get_nth_row": "4. Get Nth Row",
        "filter_by_drink_category": "5. Filter by Drink Category",
        "get_high_spenders": "6. Get High Spenders",
        "get_mobile_rewards_members": "7. Get Mobile Rewards Members",
        "get_specific_regions": "8. Get Specific Regions"
    }

    # Run tests and collect results
    print(f"\n{BOLD}Running HW2 pandas Tests...{RESET}\n")
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPandasProblems)
    
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
                 print(f"  {RED}FAIL: {test_case.id()}{RESET}")
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
            
        print(f"{name:<35} {color}[{passed}/{total}]{RESET}")

    print("-" * 40)
    final_color = GREEN if total_passed_overall == total_tests_overall else RED
    print(f"{BOLD}Total Progress:{RESET} {final_color}[{total_passed_overall}/{total_tests_overall}]{RESET}")

