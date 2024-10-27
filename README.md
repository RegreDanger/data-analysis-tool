# Data Analysis Tool

This is a script that generates images of charts and PDFs quickly from a CSV file.

## Technologies Used
- Python
- PyInstaller
- Pandas
- Matplotlib

## Requirements
- Python 3.x
  - If you don’t have Python, download it from: [Python Download](https://www.python.org/downloads/)

## Installation
1. Download the .zip file and unzip it.
2. Open cmd and navigate to the directory of the folder. Example: `cd C:\Users\User\YourFolder\data-analysis-tool`
3. Install the dependencies by executing: `pip install -r requirements.txt`
4. You can execute the file with: `python analyzer.py` or create an executable with: `pyinstaller --onefile analyzer.py`

## Usage
You need to input the path of your CSV file, like: `YourFolder\Example.csv`. The Script will create a folder in the location of the executable/Python file named "Images-NameOfTheCSV", where all the image charts will be stored. the generated pdf will be stored in the location of the executable/Python file.
