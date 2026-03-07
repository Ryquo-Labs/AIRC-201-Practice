# NumPy Reference Sheet: AIRC 201

This reference sheet covers the essential NumPy functions and concepts introduced in **Part 2: NumPy Fundamentals**.

---

### What is NumPy?
NumPy is a library used for fast scientific computing in both research and industry. It is written mostly in C, allowing for fast vector operations.

* **CPU Only**: NumPy operations utilize the CPU and do not use the GPU.
* **Vectorization**: This technique replaces explicit loops with optimized, parallel operations on entire arrays.

---

### The n-dimensional array (ndarray)
The core structure in NumPy is a fixed-size multidimensional array.

| Function | Description |
| :--- | :--- |
| `np.array(my_list)` | Creates an array from a standard Python list. |
| `np.zeros(size)` | Creates an array filled with zeros. |
| `np.ones(size)` | Creates an array filled with ones. |
| `np.arange(start, stop, step)` | Creates an array for a specified range. |
| `np.random.normal(mean, std, size)` | Samples data from a normal distribution. |
| `np.random.rand(size)` | Samples data from a uniform distribution. |
| `arr.shape` | Property that returns the shape of the array. |
| `arr.dtype` | Property that returns the data type of the array elements. |

---

### Array Operations & Aggregation
Standard operations like `+`, `-`, `*`, and `/` work **element-wise** on arrays.

* **Universal Functions**: Work element-wise (e.g., `np.sin()`, `np.exp()`, `np.sqrt()`).
* **Aggregation**: Condenses array information (e.g., `np.sum()`, `np.mean()`, `np.max()`).
* **Axis**: You can specify the direction of an operation using the `axis` parameter.

---

### Linear Algebra
NumPy treats 1D arrays as vectors and 2D arrays as matrices.

* **Matrix Multiplication**: Use the `@` symbol (e.g., `X @ Y`). 
    * This performs a dot product if both are vectors.
    * It performs matrix multiplication if both are matrices.
* **Transpose**: Use the `.T` property to transpose a matrix (e.g., `X.T`).
