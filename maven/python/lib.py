"""
Python Libraries Program: NumPy, Pandas, Matplotlib, Seaborn
==============================================================
This program demonstrates and explains four essential Python libraries
for data science and visualization.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 80)
print("PYTHON DATA SCIENCE LIBRARIES: NumPy, Pandas, Matplotlib, Seaborn")
print("=" * 80)

# =====================================================
# 1. NumPy - Numerical Computing
# =====================================================
print("\n" + "=" * 80)
print("1. NumPy - Numerical Computing Library")
print("=" * 80)

print("""
NumPy (Numerical Python):
- Foundation for numerical computing in Python
- Provides support for arrays and matrices
- Enables mathematical and logical operations on large datasets
- Much faster than Python lists for numerical operations
- Used by almost all data science libraries
""")

print("\n--- Example 1: Creating NumPy Arrays ---")
# Output: --- Example 1: Creating NumPy Arrays ---
# Create arrays from Python lists
array_1d = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {array_1d}")
# Output: 1D Array: [1 2 3 4 5]
print(f"Array shape: {array_1d.shape}")
# Output: Array shape: (5,)
print(f"Array dtype: {array_1d.dtype}")
# Output: Array dtype: int64

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D Array:\n{array_2d}")
# Output: 
# 2D Array:
# [[1 2 3]
#  [4 5 6]]
print(f"Array shape: {array_2d.shape}")
# Output: Array shape: (2, 3)

print("\n--- Example 2: Creating Arrays with Built-in Functions ---")
# Output: --- Example 2: Creating Arrays with Built-in Functions ---
zeros = np.zeros(5)
print(f"Zeros array: {zeros}")
# Output: Zeros array: [0. 0. 0. 0. 0.]

ones = np.ones((2, 3))
print(f"Ones array (2x3):\n{ones}")
# Output: Ones array (2x3):
# [[1. 1. 1.]
#  [1. 1. 1.]]

range_arr = np.arange(0, 10, 2)
print(f"Range array (0 to 10, step 2): {range_arr}")
# Output: Range array (0 to 10, step 2): [0 2 4 6 8]

linspace = np.linspace(0, 1, 5)
print(f"Linspace (0 to 1, 5 elements): {linspace}")
# Output: Linspace (0 to 1, 5 elements): [0.   0.25 0.5  0.75 1.  ]

print("\n--- Example 3: Array Operations ---")
# Output: --- Example 3: Array Operations ---
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(f"Array a: {a}")
# Output: Array a: [1 2 3 4 5]
print(f"Array b: {b}")
# Output: Array b: [10 20 30 40 50]
print(f"Addition (a + b): {a + b}")
# Output: Addition (a + b): [11 22 33 44 55]
print(f"Subtraction (a - b): {a - b}")
# Output: Subtraction (a - b): [-9 -18 -27 -36 -45]
print(f"Multiplication (a * b): {a * b}")
# Output: Multiplication (a * b): [10 40 90 160 250]
print(f"Division (b / a): {b / a}")
# Output: Division (b / a): [10. 10. 10. 10. 10.]

print("\n--- Example 4: Statistical Operations ---")
# Output: --- Example 4: Statistical Operations ---
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Data: {data}")
# Output: Data: [ 10  20  30  40  50  60  70  80  90 100]
print(f"Mean: {np.mean(data)}")
# Output: Mean: 55.0
print(f"Median: {np.median(data)}")
# Output: Median: 55.0
print(f"Std Dev: {np.std(data)}")
# Output: Std Dev: 28.866070047722118
print(f"Min: {np.min(data)}")
# Output: Min: 10
print(f"Max: {np.max(data)}")
# Output: Max: 100
print(f"Sum: {np.sum(data)}")
# Output: Sum: 550

print("\n--- Example 5: Array Indexing and Slicing ---")
# Output: --- Example 5: Array Indexing and Slicing ---
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2D Array:\n{arr}")
# Output: 2D Array:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(f"Element at [0, 1]: {arr[0, 1]}")
# Output: Element at [0, 1]: 2
print(f"First row: {arr[0, :]}")
# Output: First row: [1 2 3]
print(f"First column: {arr[:, 0]}")
# Output: First column: [1 4 7]
print(f"2x2 subarray:\n{arr[0:2, 0:2]}")
# Output: 2x2 subarray:
# [[1 2]
#  [4 5]]

# =====================================================
# 2. Pandas - Data Manipulation and Analysis
# =====================================================
print("\n" + "=" * 80)
print("2. Pandas - Data Manipulation and Analysis Library")
print("=" * 80)

print("""
Pandas:
- Built on top of NumPy
- Provides data structures: Series (1D) and DataFrame (2D)
- Excellent for data cleaning, transformation, and analysis
- Handles missing data
- Supports multiple data formats (CSV, Excel, SQL, etc.)
- Essential for data preprocessing and exploration
""")

print("\n--- Example 1: Creating a Series ---")
# Output: --- Example 1: Creating a Series ---
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(f"Series:\n{series}")
# Output: Series:
# a    10
# b    20
# c    30
# d    40
# e    50
# dtype: int64
print(f"\nAccess element 'c': {series['c']}")
# Output: Access element 'c': 30

print("\n--- Example 2: Creating a DataFrame ---")
# Output: --- Example 2: Creating a DataFrame ---
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'IT'],
    'Salary': [50000, 60000, 75000, 55000, 65000]
}
df = pd.DataFrame(data)
print(f"DataFrame:\n{df}")
# Output: DataFrame:
#       Name  Age Department  Salary
# 0    Alice   25         IT   50000
# 1      Bob   30         HR   60000
# 2  Charlie   35    Finance   75000
# 3    David   28         IT   55000
# 4      Eve   32         IT   65000

print("\n--- Example 3: DataFrame Operations ---")
# Output: --- Example 3: DataFrame Operations ---
print(f"\nDataFrame shape: {df.shape}")
# Output: DataFrame shape: (5, 4)
print(f"Column names: {list(df.columns)}")
# Output: Column names: ['Name', 'Age', 'Department', 'Salary']
print(f"\nFirst 3 rows:\n{df.head(3)}")
# Output: First 3 rows:
#       Name  Age Department  Salary
# 0    Alice   25         IT   50000
# 1      Bob   30         HR   60000
# 2  Charlie   35    Finance   75000
print(f"\nDataFrame info:")
# Output: DataFrame info:
print(df.info())
# Output: <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
# ... (detailed info)

print("\n--- Example 4: DataFrame Statistics ---")
# Output: --- Example 4: DataFrame Statistics ---
print(f"\nBasic statistics:\n{df.describe()}")
# Output: Basic statistics:
#         Age      Salary
# count   5.0      5.0
# mean   30.0  61000.0
# std     4.2   9830.8
# min    25.0  50000.0
# 25%    28.0  55000.0
# 50%    30.0  60000.0
# 75%    32.0  65000.0
# max    35.0  75000.0
print(f"\nMean age: {df['Age'].mean()}")
# Output: Mean age: 30.0
print(f"Average salary: {df['Salary'].mean()}")
# Output: Average salary: 61000.0

print("\n--- Example 5: DataFrame Filtering ---")
# Output: --- Example 5: DataFrame Filtering ---
it_employees = df[df['Department'] == 'IT']
print(f"IT Department Employees:\n{it_employees}")
# Output: IT Department Employees:
#      Name  Age Department  Salary
# 0   Alice   25         IT   50000
# 3   David   28         IT   55000
# 4     Eve   32         IT   65000

high_earners = df[df['Salary'] > 60000]
print(f"\nEmployees earning > $60,000:\n{high_earners}")
# Output: Employees earning > $60,000:
#       Name  Age Department  Salary
# 1      Bob   30         HR   60000
# 2  Charlie   35    Finance   75000
# 4      Eve   32         IT   65000

print("\n--- Example 6: Data Manipulation ---")
# Output: --- Example 6: Data Manipulation ---
df_copy = df.copy()
df_copy['Bonus'] = df_copy['Salary'] * 0.1
print(f"Added Bonus column:\n{df_copy}")
# Output: Added Bonus column:
#       Name  Age Department  Salary  Bonus
# 0    Alice   25         IT   50000    5000.0
# 1      Bob   30         HR   60000    6000.0
# 2  Charlie   35    Finance   75000    7500.0
# 3    David   28         IT   55000    5500.0
# 4      Eve   32         IT   65000    6500.0

print("\n--- Example 7: Sorting ---")
# Output: --- Example 7: Sorting ---
sorted_df = df.sort_values('Salary', ascending=False)
print(f"Employees sorted by salary (highest to lowest):\n{sorted_df}")
# Output: Employees sorted by salary (highest to lowest):
#       Name  Age Department  Salary
# 2  Charlie   35    Finance   75000
# 4      Eve   32         IT   65000
# 1      Bob   30         HR   60000
# 3    David   28         IT   55000
# 0    Alice   25         IT   50000

print("\n--- Example 8: Grouping ---")
# Output: --- Example 8: Grouping ---
group_by_dept = df.groupby('Department')['Salary'].mean()
print(f"Average salary by department:\n{group_by_dept}")
# Output: Average salary by department:
# Department
# Finance    75000.0
# HR         60000.0
# IT         56666.7
# dtype: float64

# =====================================================
# 3. Matplotlib - Data Visualization
# =====================================================
print("\n" + "=" * 80)
print("3. Matplotlib - Data Visualization Library")
print("=" * 80)

print("""
Matplotlib:
- Comprehensive library for creating static, animated, and interactive plots
- Provides MATLAB-like plotting interface
- Highly customizable and extensible
- Supports multiple output formats (PNG, PDF, SVG, etc.)
- Foundation for other visualization libraries (Seaborn, Plotly)
""")

print("\n--- Example 1: Line Plot ---")
# Output: --- Example 1: Line Plot ---
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linewidth=2)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.grid(True, alpha=0.3)
print("\nLine plot created: SineCosine.png")
# Output: Line plot created: SineCosine.png
plt.savefig('SineCosine.png')
plt.close()

print("\n--- Example 2: Bar Plot ---")
# Output: --- Example 2: Bar Plot ---
categories = ['Q1', 'Q2', 'Q3', 'Q4']
sales = [100, 150, 120, 200]

plt.figure(figsize=(8, 5))
plt.bar(categories, sales, color='green', alpha=0.7, edgecolor='black')
plt.xlabel('Quarters')
plt.ylabel('Sales (in thousands)')
plt.title('Quarterly Sales')
for i, v in enumerate(sales):
    plt.text(i, v + 5, str(v), ha='center', fontweight='bold')
print("\nBar plot created: BarPlot.png")
# Output: Bar plot created: BarPlot.png
plt.savefig('BarPlot.png')
plt.close()

print("\n--- Example 3: Histogram ---")
# Output: --- Example 3: Histogram ---
data = np.random.normal(100, 15, 1000)  # Generate random data

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='purple', alpha=0.7, edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Distribution of Values')
print("\nHistogram created: Histogram.png")
# Output: Histogram created: Histogram.png
plt.savefig('Histogram.png')
plt.close()

print("\n--- Example 4: Scatter Plot ---")
# Output: --- Example 4: Scatter Plot ---
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, cmap='viridis', s=100, alpha=0.6, edgecolors='black')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot with Color Map')
plt.colorbar(label='Color intensity')
print("\nScatter plot created: ScatterPlot.png")
# Output: Scatter plot created: ScatterPlot.png
plt.savefig('ScatterPlot.png')
plt.close()

# =====================================================
# 4. Seaborn - Statistical Data Visualization
# =====================================================
print("\n" + "=" * 80)
print("4. Seaborn - Statistical Data Visualization Library")
print("=" * 80)

print("""
Seaborn:
- Built on top of Matplotlib
- Provides high-level interface for statistical graphics
- Makes it easier to create attractive plots with less code
- Better default styles and color palettes
- Integrates well with Pandas DataFrames
- Great for exploratory data analysis (EDA)
""")

print("\n--- Example 1: Distribution Plot ---")
# Output: --- Example 1: Distribution Plot ---
sns.set_theme()
data = np.random.randn(1000)

plt.figure(figsize=(8, 5))
sns.histplot(data, kde=True, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution with KDE')
print("\nSeaborn distribution plot created: DistPlot.png")
# Output: Seaborn distribution plot created: DistPlot.png
plt.savefig('DistPlot.png')
plt.close()

print("\n--- Example 2: Box Plot ---")
# Output: --- Example 2: Box Plot ---
box_data = pd.DataFrame({
    'Value': np.random.randn(200),
    'Group': np.random.choice(['A', 'B', 'C', 'D'], 200)
})

plt.figure(figsize=(8, 5))
sns.boxplot(data=box_data, x='Group', y='Value', palette='Set2')
plt.title('Box Plot by Group')
print("\nBox plot created: BoxPlot.png")
# Output: Box plot created: BoxPlot.png
plt.savefig('BoxPlot.png')
plt.close()

print("\n--- Example 3: Violin Plot ---")
# Output: --- Example 3: Violin Plot ---
plt.figure(figsize=(8, 5))
sns.violinplot(data=box_data, x='Group', y='Value', palette='muted')
plt.title('Violin Plot by Group')
print("\nViolin plot created: ViolinPlot.png")
# Output: Violin plot created: ViolinPlot.png
plt.savefig('ViolinPlot.png')
plt.close()

print("\n--- Example 4: Heatmap (Correlation Matrix) ---")
# Output: --- Example 4: Heatmap (Correlation Matrix) ---
data = np.random.randn(10, 4)
df_corr = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
correlation = df_corr.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Heatmap')
print("\nHeatmap created: Heatmap.png")
# Output: Heatmap created: Heatmap.png
plt.savefig('Heatmap.png')
plt.close()

print("\n--- Example 5: Scatter Plot with Regression Line ---")
# Output: --- Example 5: Scatter Plot with Regression Line ---
scatter_data = pd.DataFrame({
    'X': np.random.randn(100),
    'Y': np.random.randn(100)
})
scatter_data['Y'] = scatter_data['Y'] + scatter_data['X'] * 0.5  # Add correlation

plt.figure(figsize=(8, 6))
sns.regplot(data=scatter_data, x='X', y='Y', scatter_kws={'s': 50, 'alpha': 0.6})
plt.title('Scatter Plot with Regression Line')
print("\nRegression plot created: RegressionPlot.png")
# Output: Regression plot created: RegressionPlot.png
plt.savefig('RegressionPlot.png')
plt.close()

# =====================================================
# 5. COMPARISON AND USE CASES
# =====================================================
print("\n" + "=" * 80)
print("5. LIBRARY COMPARISON AND USE CASES")
print("=" * 80)

print("""
NumPy:
✓ Fast numerical operations on arrays
✓ Mathematical functions
✓ Linear algebra operations
✓ Random number generation
Use Cases: Scientific computing, data processing, mathematical calculations

Pandas:
✓ Data loading and cleaning
✓ Missing data handling
✓ Data grouping and aggregation
✓ Time series analysis
✓ Merging and joining datasets
Use Cases: Data preprocessing, exploratory data analysis, data transformation

Matplotlib:
✓ Complete control over plot customization
✓ Multiple plot types (line, bar, scatter, histogram, etc.)
✓ Publication-quality figures
✓ Works with NumPy arrays and Pandas DataFrames
Use Cases: Scientific visualization, research papers, custom plots

Seaborn:
✓ Beautiful default styling (less code for same result)
✓ Statistical visualizations
✓ Better Pandas integration
✓ Color palettes
✓ Handles missing data gracefully
Use Cases: Quick exploratory analysis, statistical summaries, presentations

TYPICAL WORKFLOW:
1. Load data → Pandas
2. Clean & process data → Pandas + NumPy
3. Statistical analysis → NumPy/Pandas
4. Visualization → Matplotlib/Seaborn
""")

print("\n" + "=" * 80)
print("SUMMARY OF EXAMPLES")
print("=" * 80)
print("""
NumPy Examples:
- Creating arrays (1D, 2D, zeros, ones, arange, linspace)
- Array operations (arithmetic, aggregation)
- Statistical functions (mean, median, std dev, min, max)
- Array indexing and slicing

Pandas Examples:
- Series and DataFrame creation
- Data filtering and selection
- Statistical summaries
- Grouping and aggregation
- Sorting and manipulation

Matplotlib Examples:
- Line plots
- Bar plots
- Histograms
- Scatter plots

Seaborn Examples:
- Distribution plots with KDE
- Box plots
- Violin plots
- Heatmaps (correlation)
- Regression plots
""")

print("\n" + "=" * 80)
print("Program Complete! All visualizations saved as PNG files.")
print("=" * 80)
# Output: ================================================================================
# Output: Program Complete! All visualizations saved as PNG files.
# Output: ================================================================================
