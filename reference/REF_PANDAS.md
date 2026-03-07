# Pandas Reference Sheet: AIRC 201

This reference sheet covers the essential Pandas functions and concepts introduced in **AIRC 201: Data Handling**.

---

### Core Data Structures
Pandas is a library used for data manipulation and analysis, often called the "Excel of Python".

* **DataFrame**: Represents a whole spreadsheet.
    * **Rows**: Individual data entries.
    * **Columns**: Input features.
* **Series**: Represents one single column.
* **Index**: Row labels.

---

### Loading and Inspecting Data
Data is typically provided in **comma-separated values (CSV)** format.

| Function | Description |
| :--- | :--- |
| `df = pd.read_csv('file.csv')` | Loads data from a CSV file into a DataFrame. |
| `df.head()` | Prints out data in the first 5 rows. |
| `df.info()` | Prints out column names, types, and null/non-null counts. |
| `df.describe()` | Prints out basic stats for all numerical columns. |
| `df.shape` | Returns a tuple of the number of rows and columns. |
| `df.columns` | Returns an index containing the names of columns. |

---

### Selection and Filtering
You can extract specific data using direct selection or conditional filtering.

* **Column Selection**: Select a column directly with square brackets (e.g., `df['column_name']`).
* **Row Selection**: Select a row with `.iloc` ("integer location").
* **Boolean Masking**: Creating a conditional expression to filter rows.
    * *Basic condition*: `df[df['age'] > 25]`.
    * *Multiple conditions*: `df[(df['age'] > 25) & (df['city'] == 'NY')]`.
    * *List membership*: `df[df['color'].isin(['red', 'blue'])]`.

---

### Basic Data Cleaning
Real-world data is often messy and requires cleaning based on the use case.

* **Handling Null Values**:
    * `df.dropna()`: Drops all null/missing values (can specify row or column).
    * `df.fillna(0)`: Replaces all null/missing values with a specific value, such as 0.
* **Type Conversion**:
    * `df.astype()`: Forces columns to change data types.
* **Duplicates**:
    * `df.drop_duplicates()`: Removes duplicate rows from the DataFrame.
