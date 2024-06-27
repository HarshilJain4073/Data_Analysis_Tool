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
   git clone https://github.com/yourusername/data-analysis-tool.git
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
Please enter your command (1-7): 1
Enter the path to your dataset file (e.g., data.csv): data.csv
Dataset loaded successfully.
Please enter your command (2-7): 2

Displaying Dataset:

| ID | Name  | Age | Salary |
|----|-------|-----|--------|
| 1  | John  | 25  | 50000  |
| 2  | Alice | 30  | 60000  |
| 3  | Bob   | 28  | 55000  |
| ...| ...   | ... | ...    |

Please enter your command (2-7): 5

Calculating Statistics:

1. Average salary
2. Maximum age
3. Minimum salary

Enter your choice (1-3): 1

Average salary: $55000

Please enter your command (2-7): 6

Generating Visualization:

1. Histogram of ages
2. Box plot of salaries

Enter your choice (1-2): 1

Visualization generated: Histogram of ages displayed.

Please enter your command (2-7): 7

Exiting Data Analysis Tool. Goodbye!
