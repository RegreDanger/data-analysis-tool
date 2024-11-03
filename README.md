# Data Analysis Tool

This project is a Python-based script that quickly generates images of charts and PDFs from a CSV file. It is designed for efficient data visualization, making it easy to analyze and present data insights.

## Technologies Used
- **Python**
- **PyInstaller**: For creating standalone executables.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating static, animated, and interactive visualizations in Python.

## Requirements
- **Python 3.x**: If you don’t have Python installed, download it from: [Python Download](https://www.python.org/downloads/).

## Installation
1. **Clone the Repository**:
   - Download the project as a ZIP file and extract it, or clone the repository using:
     ```
     git clone https://github.com/RegreDanger/data-analysis-tool.git
     ```
   
2. **Navigate to the Project Directory**:
   - Open your command prompt (cmd) and navigate to the project folder:
     ```
     cd C:\Users\User\YourFolder\data-analysis-tool
     ```

3. **Install Dependencies**:
   - Execute the following command to install required libraries:
     ```
     pip install -r requirements.txt
     ```

4. **Run the Script**:
   - You can execute the tool with:
     ```
     python analyzer.py
     ```
   - Alternatively, create a standalone executable using:
     ```
     pyinstaller --onefile analyzer.py
     ```

## Usage
1. **Input CSV File**:
   - When prompted, enter the path of your CSV file, for example: `YourFolder\Example.csv`.

2. **Output**:
   - The script will create a folder in the same location as the executable or Python script named **"Images-NameOfTheCSV"**, where all generated chart images will be stored.
   - The resulting PDF will also be saved in the same directory as the executable or Python file.

## Example
To run the tool on a CSV file named "data.csv" located in `C:\Users\User\Documents`, you would enter:
```
C:\Users\User\Documents\data.csv
