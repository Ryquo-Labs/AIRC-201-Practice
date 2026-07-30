import numpy as np

def relu_activation(arr: np.ndarray) -> np.ndarray:
    """
    Applies the Rectified Linear Unit (ReLU) activation element-wise.
    Returns a new array where all negative values are replaced with 0.
    """
    return np.maximum(arr, 0)

def calculate_euclidean_distance(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Given two 1D arrays (vectors) of the same length, return the Euclidean distance between them.
    """
    return np.linalg.norm(v1 - v2)

def matrix_multiplication(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Returns the matrix multiplication of 2D arrays A and B.
    """
    return np.dot(A, B)

def normalize_data(X: np.ndarray) -> np.ndarray:
    """
    Performs Z-score normalization on a 2D array X (samples x features).
    Returns a new array where each feature (column) has mean 0 and standard deviation 1.
    If a column has 0 standard deviation, its normalized values should be 0.
    """
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    # Avoid division by zero
    std = np.where(std == 0, 1, std)
    return (X - mean) / std

def one_hot_encode(labels: np.ndarray, num_classes: int) -> np.ndarray:
    """
    Converts a 1D array of integer class labels (0 to num_classes-1) to a 2D one-hot encoding matrix.
    Shape of output should be (len(labels), num_classes).
    """
    return np.eye(num_classes)[labels]

def softmax_activation(logits: np.ndarray) -> np.ndarray:
    """
    Applies the softmax function to a 2D array of logits (samples x classes).
    Subtract the maximum logit of each row for numerical stability.
    Returns a 2D array of probabilities where each row sums to 1.
    """
    # Subtract the maximum logit for numerical stability
    logits_shifted = logits - np.max(logits, axis=1, keepdims=True)
    exp_logits = np.exp(logits_shifted)
    return exp_logits / np.sum(exp_logits, axis=1, keepdims=True)

def find_k_nearest_neighbors(data: np.ndarray, query: np.ndarray, k: int) -> np.ndarray:
    """
    Given a 2D array of data points (samples x features) and a 1D query point (features),
    return the indices of the 'k' closest points in 'data' using Euclidean distance.
    """
    distances = np.linalg.norm(data - query, axis=1)
    return np.argpartition(distances, k)[:k]

def compute_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray, num_classes: int) -> np.ndarray:
    """
    Computes a confusion matrix C of shape (num_classes, num_classes) where 
    C[i, j] is the count of observations known to be in group i and predicted to be in group j.
    """
    confusion_matrix = np.zeros((num_classes, num_classes), dtype=int)
    for true_label, pred_label in zip(y_true, y_pred):
        confusion_matrix[true_label, pred_label] += 1
    return confusion_matrix

def calculate_class_centroids(X: np.ndarray, labels: np.ndarray, num_classes: int) -> np.ndarray:
    """
    Given a 2D array of data points X (samples x features) and a 1D array of labels (0 to num_classes-1),
    compute the centroid (mean vector) for each class.
    Returns a 2D array of shape (num_classes, features).
    If a class has no examples, its centroid should be an array of zeros.
    """
    centroids = np.zeros((num_classes, X.shape[1]))
    for i in range(num_classes):
        mask = labels == i
        if np.any(mask):
            centroids[i] = np.mean(X[mask], axis=0)
    return centroids
