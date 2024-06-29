# Data Analysis Tool

Welcome to the Data Analysis Tool repository! This tool allows you to perform various data analysis tasks on a dataset loaded from a CSV file.

## Features

- Load the dataset from a CSV file.
- View dataset summary and initial rows.
- Sort data by column values or index.
- Filter data based on column values.
- Calculate basic statistics of the dataset.
- Generate visualizations (Histograms and Box plots) for numerical data columns.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries:
  - pandas
  - matplotlib

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HarshilJain4073/data-analysis-tool.git
   cd data-analysis-tool
2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt

## Usage

1. **Run the analysis_tool.py script:**

   ```bash
   python analysis_tool.py

Follow the on-screen instructions to interact with the Data Analysis Tool:

1. **Load dataset:**
   - Enter the path to your dataset file (e.g., data.csv).

2. **View dataset:**
   - Display the first 5 rows of the loaded dataset.

3. **Sort data:**
   - Choose between sorting by column values or index.

4. **Filter data:**
   - Filter rows based on a specified condition (e.g., column > value).

5. **Calculate statistics:**
   - View basic statistical summaries of the dataset.

6. **Generate visualization:**
   - Choose between Histogram or Box plot for numerical columns.

7. **Exit:**
   - Terminate the program.

```bash
$ python data_analysis_tool.py
Welcome to the Data Analysis Tool
Available Commands:
1. Load dataset
2. View dataset
3. Sort data
4. Filter data
5. Calculate statistics
6. Generate visualization
7. Exit
Please enter your command (1-7): 1
Enter the path to your dataset file(e.g., data.csv)data.csv
Dataset loaded successfully.

Available Commands:
1. Load dataset
2. View dataset
3. Sort data
4. Filter data
5. Calculate statistics
6. Generate visualization
7. Exit
Please enter your command (1-7): 2

Displaying Dataset:
   ID   Name  Age  Salary
0   1   John   25   50000
1   2  Alice   30   60000
2   3    Bob   28   55000
3   4   Jane   27   52000
4   5   Mark   32   58000

Available Commands:
1. Default sort by values
2. Sort by index
Please select a column to sort: Age

   ID   Name  Age  Salary
0   1   John   25   50000
2   3    Bob   28   55000
3   4   Jane   27   52000
1   2  Alice   30   60000
4   5   Mark   32   58000

Enter the column to filter: Salary
Enter the condition (<,>,<=,>=,==): >=
Enter the value for condition: 55000

   ID   Name  Age  Salary
1   2  Alice   30   60000
4   5   Mark   32   58000

Available Commands:
1. Load dataset
2. View dataset
3. Sort data
4. Filter data
5. Calculate statistics
6. Generate visualization
7. Exit
Please enter your command (1-7): 5

       ID        Age        Salary
count  5.0   5.000000      5.000000
mean   3.0  28.400000  54600.000000
std    1.581139   2.701851   3768.496102
min    1.0  25.000000  50000.000000
25%    2.0  27.000000  52000.000000
50%    3.0  28.000000  55000.000000
75%    4.0  30.000000  58000.000000
max    5.0  32.000000  60000.000000

Available Commands:
1. Histogram
2. Box plot
Enter your choice(1-2): 1
Enter the column: Age

Histogram is being generated.

Available Commands:
1. Load dataset
2. View dataset
3. Sort data
4. Filter data
5. Calculate statistics
6. Generate visualization
7. Exit
Please enter your command (1-7): 7

Thank you for using analyzer.
