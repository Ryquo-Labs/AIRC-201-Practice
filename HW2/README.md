# HW2 - Data Manipulation with Pandas and NumPy

This assignment focuses on two of the most critical libraries used in data science and machine learning: **Pandas** and **NumPy**. You will be practicing dataframe manipulation and writing core linear algebra operations that form the backbone of many ML models.

## Instructions

For this homework, you have to complete the problems in two separate files:
1. `HW2/problems_pandas.py`
2. `HW2/problems_numpy.py`

Replace the `raise NotImplementedError` in each function with your solution.
You can use `tests_pandas.py` and `tests_numpy.py` to check your work.

---

## Part 1: Pandas

These functions will be operating on data similar to the `starbucks_customer_ordering_patterns.csv` dataset.

### 1. Get Dataset Shape
Implement `get_dataset_shape(df)` that returns the shape of the dataframe as a tuple of `(number of rows, number of columns)`.

**Difficulty:** Easy

### 2. Get Column Names
Implement `get_column_names(df)` that returns a list of all column names in the given dataframe.

**Difficulty:** Easy

### 3. Get Summary Statistics
Implement `get_summary_statistics(df, column_name)` that returns the summary statistics (using `.describe()`) for the specified column in the dataframe.

**Difficulty:** Easy

### 4. Get Nth Row
Implement `get_nth_row(df, n)` that returns the n-th row of the dataframe, using standard integer-based indexing.

**Difficulty:** Easy

### 5. Filter by Drink Category
Implement `filter_by_drink_category(df, category)` that returns a dataframe containing only the rows where the `"drink_category"` matches the given category string.

**Difficulty:** Medium

### 6. Get High Spenders
Implement `get_high_spenders(df, min_spend)` that returns a dataframe containing only the rows where the `"total_spend"` is strictly greater than `min_spend`.

**Difficulty:** Medium

### 7. Get Mobile Rewards Members
Implement `get_mobile_rewards_members(df)` that returns a dataframe containing only the rows where `"order_channel"` is `'Mobile App'` **AND** `"is_rewards_member"` is `True`.

**Difficulty:** Medium

### 8. Get Specific Regions
Implement `get_specific_regions(df, regions)` that returns a dataframe containing only the rows where the `"region"` is one of the strings in the given list of `regions`.

**Difficulty:** Medium

---

## Part 2: NumPy

For these problems, you are expected to use NumPy functions. Focus on vectorization rather than using Python `for` loops whenever possible.

### 1. ReLU Activation
Implement `relu_activation(arr)` to apply the Rectified Linear Unit element-wise. Replace all negative values with 0.
$$f(x) = \max(0, x)$$
- **Inputs**: 
  - `arr`: Input array of any shape.
- **Outputs**:
  - A new array with the exact same shape as the input `arr`.
- **Difficulty:** Easy

### 2. Euclidean Distance
Implement `calculate_euclidean_distance(v1, v2)` to compute the Euclidean distance between two 1D array vectors.
$$d(p, q) = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2}$$
- **Inputs**: 
  - `v1`: 1D array of shape `(features,)`.
  - `v2`: 1D array of shape `(features,)`.
- **Outputs**:
  - A single float value representing the distance.
- **Difficulty:** Easy

### 3. Matrix Multiplication
Implement `matrix_multiplication(A, B)` that computes the dot product of 2D arrays A and B.
$$C_{i,j} = \sum_{k=1}^{n} A_{i,k} B_{k,j}$$
- **Inputs**: 
  - `A`: 2D array of shape `(M, N)`.
  - `B`: 2D array of shape `(N, P)`.
- **Outputs**:
  - A 2D array of shape `(M, P)`.
- **Difficulty:** Easy

### 4. Normalize Data
Implement `normalize_data(X)` to perform Z-score normalization on a 2D array. Each column should be normalized to have a mean of 0 and standard deviation of 1. If a column has 0 standard deviation, its normalized values should be 0.
$$z = \frac{x - \mu}{\sigma}$$
- **Inputs**: 
  - `X`: 2D array of shape `(samples, features)`.
- **Outputs**:
  - A 2D array of shape `(samples, features)`.
- **Difficulty:** Medium

### 5. One Hot Encode
Implement `one_hot_encode(labels, num_classes)` that converts a 1D array of integer class labels (0 to num_classes-1) to an $N \times C$ one-hot encoding matrix.
- **Inputs**: 
  - `labels`: 1D array of shape `(samples,)`.
  - `num_classes`: Integer representing the number of classes `C`.
- **Outputs**:
  - A 2D array of shape `(samples, num_classes)` consisting of 1s and 0s.
- **Difficulty:** Medium

### 6. Softmax Activation
Implement `softmax_activation(logits)` that applies the softmax function to a 2D array of logits. For numerical stability, subtract the maximum logit of each row before taking the exponent.
$$P(y=j|x) = \frac{e^{x_j - \max(x)}}{\sum_{k=1}^{K} e^{x_k - \max(x)}}$$
- **Inputs**: 
  - `logits`: 2D array of shape `(samples, classes)` representing raw unnormalized scores.
- **Outputs**:
  - A 2D array of shape `(samples, classes)` containing probabilities.
- **Difficulty:** Medium

### 7. K-Nearest Neighbors
Implement `find_k_nearest_neighbors(data, query, k)` to return the indices of the `k` closest points in `data` to a `query` point using Euclidean distance.
- **Inputs**: 
  - `data`: 2D array of shape `(samples, features)`.
  - `query`: 1D array of shape `(features,)`.
  - `k`: Integer number of neighbors to find.
- **Outputs**:
  - A 1D array of integer indices of shape `(k,)`.
- **Difficulty:** Medium

### 8. Confusion Matrix
Implement `compute_confusion_matrix(y_true, y_pred, num_classes)` to compute a $C \times C$ confusion matrix given arrays of true and predicted integer labels. Element $C_{i,j}$ should be the count of observations known to be in group $i$ and predicted to be in group $j$.
- **Inputs**: 
  - `y_true`: 1D array of shape `(samples,)`.
  - `y_pred`: 1D array of shape `(samples,)`.
  - `num_classes`: Integer representing the total number of classes.
- **Outputs**:
  - A 2D array of shape `(num_classes, num_classes)`.
- **Difficulty:** Medium

### 9. Class Centroids
Implement `calculate_class_centroids(X, labels, num_classes)` to compute the mean vector for each class. If a class has zero instances, its centroid should be an array of all zeros.
$$\mu_k = \frac{1}{|C_k|} \sum_{x \in C_k} x$$
- **Inputs**: 
  - `X`: 2D array of shape `(samples, features)`.
  - `labels`: 1D array of shape `(samples,)`.
  - `num_classes`: Integer representing the total number of classes.
- **Outputs**:
  - A 2D array of shape `(num_classes, features)`.
- **Difficulty:** Medium