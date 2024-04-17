
### Overview
This project aims to analyze credit card transactions in various cities of India to identify trends and patterns in credit card usage. The dataset used in this analysis provides detailed information about each transaction, including the city, date, card type, expense type, gender, and amount.

### Project Structure
- **database.py**: Contains functions to create a SQLite database, insert data into the database, and retrieve data from the database.
- **app.py**: Flask application that serves the web interface for the project.
- **templates**: Folder containing HTML templates for different pages (home, project description, about, dataset).
- **static**: Folder containing static files (CSS, images) for the web interface.

### Setup Instructions
1. Install the required Python packages: `pip install pandas Flask`.
2. Run the `create_table()` function in `database.py` to create the SQLite database.
3. Run the `insert_data()` function in `database.py` to insert data from the CSV file into the database.
4. Run the Flask application using `python app.py` and navigate to `http://localhost:5000` in your web browser to access the web interface.

The relative path of the CSV file in website.py and database.py files in the project folder, you need to update the file paths to correctly point to the CSV file. Here's how you can do it:

Open website.py and database.py files in your project folder.
Locate the lines where the CSV file path is specified.
Update the file path to reflect the correct relative path to your CSV file. For example, if your CSV file is located in a folder named data within your project folder, you would update the path to something like 'data/your_csv_file.csv'.

For website.py:
# Specify the path to your CSV file
csv_file_path = 'data/your_csv_file.csv'

# Use the updated path to read the CSV file
df = pd.read_csv(csv_file_path)

For database.py:
# Specify the path to your CSV file
csv_file_path = 'data/your_csv_file.csv'

# Use the updated path to insert data into the database
def insert_data_into_database():
    # Read CSV file
    df = pd.read_csv(csv_file_path)
    # Insert data into database
    ...



### Packages Used
- **pandas**: Used for data manipulation and analysis.
- **sqlite3**: Used for interacting with SQLite databases.
- **Flask**: Used for creating the web application.

### Contributors
- **Nithin Arumbakam (W0852014)**: Responsible for designing the website layout.
- **Murali Manthena (W0858309)**: Tasked with creating the database.
- **Efe Nicholas Okoh (W0857500)**: Implemented data cleaning and created project documentation.
- **Sonnaa Fokwang Nyonglima (W0862617)**: Conducted data analysis on the dataset.

### Dataset Description
The dataset includes the following columns:
- `id`: Unique identifier for each transaction.
- `city`: The city where the transaction took place, including the country name.
- `date`: The date of the transaction.
- `card_type`: The type of credit card used for the transaction (Gold, Platinum, Silver, Signature, etc.).
- `exp_type`: The type of expense (e.g., Bills, Entertainment, Food, etc.).
- `gender`: The gender of the credit card holder (M for male, F for female).
- `amount`: The amount of the transaction.

### Objectives
1. Analyze credit card transactions in various cities of India.
2. Identify trends and patterns in credit card usage.
3. Provide insights into consumer behavior and spending habits.

### Methodology
1. Data Collection: Obtain the dataset containing credit card transaction information.
2. Data Cleaning: Clean the dataset by handling missing values, converting data types, and ensuring data consistency.
3. Data Analysis: Analyze the dataset to identify trends and patterns in credit card usage, such as spending habits across different cities, card types, expense types, and genders.
4. Data Visualization: Visualize the analysis results using charts and graphs to make them easier to understand.
5. Interpretation: Interpret the findings to draw meaningful conclusions and insights into credit card usage in India.

### Usage
1. Clone the repository containing the project files to your local machine.
2. Install the required Python packages: `pip install pandas Flask`.
3. Run the `create_table()` function in `database.py` to create the SQLite database.
4. Run the `insert_data()` function in `database.py` to insert data from the CSV file into the database.
5. Run the Flask application using `python app.py` and navigate to `http://localhost:5000` in your web browser to access the web interface.
6. Explore the web interface to view the analysis results, including charts and graphs depicting credit card usage trends in India.
