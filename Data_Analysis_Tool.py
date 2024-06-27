import pandas as pd
import matplotlib.pyplot as plt

def analysis_tool():
    print("Welcome to the Data Analysis Tool")
    path = ""
    data = pd.DataFrame()
    while True:
        print("Available Commands","1. Load dataset","2. View dataset","3. Sort data","4. Filter data","5. Calculate statistics","6. Generate visualization","7. Exit",sep = "\n")
        try:
            ans = int(input("Please enter your command (1-7):"))
            if ans not in [1,2,3,4,5,6,7]:
                print("Please enter a valid number(1-7).")
                continue
            match ans:
                case 1:
                    path = input("Enter the path to your dataset file(e.g., data.csv)")
                    try:
                        data = pd.read_csv(path)
                        print("Dataset loaded succesfully.")
                    except FileNotFoundError as e:
                        print(f"File not found on {path}.Please enter a valid path")
                    except Exception as e:
                        print(f"Error Found:{e}")
                case 2:
                    if data.empty:
                        print("Dataset is empty. Load a dataset.")
                        continue
                    print("Displaying Dataset:",data.head(5),sep = "\n")
                case 3:
                    if data.empty:
                        print("Dataset is empty. Load a dataset.")
                        continue
                    print("The type of sorting requried:","1. Default sort by values","2. Sort by index",sep = "\n")
                    inner_ans = int(input())
                    if inner_ans not in [1,2]:
                        print("Please enter a valid number(1-2).")
                        continue
                    match inner_ans:
                        case 1:
                            col = input("Please select a column to sort:")
                            if col not in data.columns:
                                print("Enter a valid column")
                                continue
                            data = data.sort_values(by=col)
                            print(data.head(5))
                        case 2:
                            data = data.sort_index()
                            print(data.head(5))
                case 4:
                    if data.empty:
                        print("Dataset is empty. Load a dataset.")
                        continue
                    col = input("Enter the column to filter:")
                    if col not in data.columns:
                        print("Enter a valid column")
                        continue
                    cond = input("Enter the condition (<,>,<=,>=,==):")
                    if cond not in ['<','>','<=','>=','==']:
                        print("Enter a valid condition")
                        continue
                    val = input("Enter the value for condition:")
                    try:
                        val = float(val)
                        if cond == '>':
                            print(data[data[col] > val])
                        elif cond == '<':
                            print(data[data[col] < val])
                        elif cond == '<=':
                            print(data[data[col] <= val])
                        elif cond == '>=':
                            print(data[data[col] >= val])
                        else:
                            print(data[data[col] == val])
                    except ValueError:
                        print(data[data[col] == val])
                case 5:
                    if data.empty:
                        print("Dataset is empty. Load a dataset.")
                        continue
                    print(data.describe())
                case 6:
                    if data.empty:
                        print("Dataset is empty. Load a dataset.")
                        continue
                    print('1. Histogram','2. Box plot',sep = '\n')
                    cho = int(input("Enter your choice(1-2):"))
                    if cho not in [1,2]:
                        print("Enter a valid choice(1-2).")
                        continue
                    col = input("Enter the column")
                    if col not in data.columns:
                        print("Enter a valid column")
                        continue
                    match cho:
                        case 1:
                            plt.hist(data[col])
                            plt.xlabel(col)
                            plt.ylabel("Frequency")
                            plt.title(f"Histogram of {col}")
                            plt.show()
                        case 2:
                            plt.boxplot(data[col])
                            plt.xlabel(col)
                            plt.ylabel("Frequency")
                            plt.title(f"Histogram of {col}")
                            plt.show()
                case 7:
                    print("Thank you for using analyzer.")
                    break
        except Exception as e:
            print(f"Error found: {e}")

if __name__ == "__main__":
    analysis_tool()