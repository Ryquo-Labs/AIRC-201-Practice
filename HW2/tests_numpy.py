import unittest
import numpy as np
import sys
import os

# Ensure HW2 is in path to import problems_numpy properly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from problems_numpy import (
    relu_activation,
    calculate_euclidean_distance,
    matrix_multiplication,
    normalize_data,
    one_hot_encode,
    softmax_activation,
    find_k_nearest_neighbors,
    compute_confusion_matrix,
    calculate_class_centroids,
)

class TestNumpyProblems(unittest.TestCase):
    def test_relu_activation(self):
        arr = np.array([-1, 0, 1, -5, 5])
        expected = np.array([0, 0, 1, 0, 5])
        np.testing.assert_array_equal(relu_activation(arr), expected)

    def test_calculate_euclidean_distance(self):
        v1 = np.array([1, 2, 3])
        v2 = np.array([4, 5, 6])
        expected = np.sqrt(27)
        self.assertAlmostEqual(calculate_euclidean_distance(v1, v2), expected)

    def test_matrix_multiplication(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        expected = A @ B
        np.testing.assert_array_equal(matrix_multiplication(A, B), expected)

    def test_normalize_data(self):
        X = np.array([[1.0, 2.0, 10.0],
                      [3.0, 2.0, 20.0],
                      [2.0, 2.0, 30.0]])
        X_norm = normalize_data(X)
        np.testing.assert_allclose(X_norm.mean(axis=0), [0, 0, 0], atol=1e-7)
        self.assertTrue(np.all(X_norm[:, 1] == 0))
        self.assertAlmostEqual(X_norm[:, 0].std(), 1.0, places=5)
        self.assertAlmostEqual(X_norm[:, 2].std(), 1.0, places=5)

    def test_one_hot_encode(self):
        labels = np.array([0, 2, 1, 2])
        expected = np.array([[1, 0, 0],
                             [0, 0, 1],
                             [0, 1, 0],
                             [0, 0, 1]])
        np.testing.assert_array_equal(one_hot_encode(labels, 3), expected)

    def test_softmax_activation(self):
        logits = np.array([[1.0, 2.0, 3.0],
                           [1000.0, 1000.0, 1000.0]])
        probs = softmax_activation(logits)
        np.testing.assert_allclose(probs.sum(axis=1), [1.0, 1.0])
        self.assertTrue((probs[0, 0] < probs[0, 1]) and (probs[0, 1] < probs[0, 2]))
        np.testing.assert_allclose(probs[1], [1/3, 1/3, 1/3])

    def test_find_k_nearest_neighbors(self):
        data = np.array([[0, 0], [1, 1], [0.1, 0.1], [5, 5]])
        query = np.array([0, 0])
        indices = find_k_nearest_neighbors(data, query, k=2)
        # Verify length and contents
        self.assertEqual(len(indices), 2)
        self.assertEqual(set(indices), {0, 2})

    def test_compute_confusion_matrix(self):
        y_true = np.array([0, 1, 2, 0, 1, 2, 0, 2, 2])
        y_pred = np.array([0, 2, 2, 0, 1, 1, 0, 2, 2])
        expected = np.array([[3, 0, 0],
                             [0, 1, 1],
                             [0, 1, 3]])
        np.testing.assert_array_equal(compute_confusion_matrix(y_true, y_pred, 3), expected)

    def test_calculate_class_centroids(self):
        X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [1.0, 1.0]])
        labels = np.array([0, 1, 1, 0])
        centroids = calculate_class_centroids(X, labels, num_classes=3)
        
        self.assertEqual(centroids.shape, (3, 2))
        np.testing.assert_array_equal(centroids[0], [1.0, 1.5])
        np.testing.assert_array_equal(centroids[1], [4.0, 5.0])
        np.testing.assert_array_equal(centroids[2], [0.0, 0.0])

if __name__ == '__main__':
    # Define ANSI color codes
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Mapping of test method prefixes to Problem Names
    problem_map = {
        "relu_activation": "1. ReLU Activation",
        "calculate_euclidean_distance": "2. Euclidean Distance",
        "matrix_multiplication": "3. Matrix Multiplication",
        "normalize_data": "4. Normalize Data",
        "one_hot_encode": "5. One Hot Encode",
        "softmax_activation": "6. Softmax Activation",
        "find_k_nearest_neighbors": "7. K-Nearest Neighbors",
        "compute_confusion_matrix": "8. Confusion Matrix",
        "calculate_class_centroids": "9. Class Centroids"
    }

    print(f"\n{BOLD}Running HW2 numpy Tests...{RESET}\n")
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestNumpyProblems)
    
    total_passed_overall = 0
    total_tests_overall = 0
    
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
        
        if problem_failures:
            print(f"{BOLD}{problem_display_name} Failures:{RESET}")
            for test_case, trace in problem_failures:
                 print(f"  {RED}FAIL: {test_case.id()}{RESET}")
                 indented_trace = "\n".join("    " + line for line in trace.splitlines())
                 print(indented_trace)
                 print()
        
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