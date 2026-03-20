# HW4 - Machine Learning with Scikit-Learn

This assignment focuses on **Scikit-Learn**, a core library for machine learning in Python. You will implement training loops and basic data preprocessing for two common tasks: Regression and Clustering.

## Instructions

For this homework, you will test your scikit-learn and machine learning knowledge by fitting models on generated data.
Complete the problems in the following files:
1. `HW4/problems_regression.py`
2. `HW4/problems_clustering.py`

Write your machine learning code between the `# START STUDENT IMPLEMENTATION HERE` and `# END STUDENT IMPLEMENTATION HERE` comments. The script will automatically generate and save your plots to the `HW4/results/` folder.

### 1. Ridge Regression (`problems_regression.py`)
In this file, you must train ridge regression models to fit a slightly messy linear dataset.
- **Data Preprocessing**: Standardize the predictor variables before fitting your model using `StandardScaler`.
- **Model Training**: Fit a `Ridge` regression model using three different regularization coefficients (alphas): `0.01`, `1`, and `100`.
- **Predictions**: Generate predictions for each alpha value over the provided test inputs to be used in plotting.
- **Output**: The provided code will output your results as `regression.png` in the `results/` folder.

### 2. K-Means Clustering (`problems_clustering.py`)
In this file, you will use k-means clustering on data consisting of 4 distinct Gaussian distributions.
- **Data Preprocessing**: Standardize the features before clustering using `StandardScaler`.
- **Model Training**: Fit a `KMeans` clustering model with three different values for $k$: `3`, `4`, and `5`.
- **Predictions**: Retrieve the cluster assignments for each point in the dataset.
- **Output**: The provided code will output your results as `clustering.png` in the `results/` folder, which contains a subplot for each $k$.

*Note: Please ensure the random seeds stay set to 67 where indicated to prevent non-deterministic behavior and ensure accurate grading.*
