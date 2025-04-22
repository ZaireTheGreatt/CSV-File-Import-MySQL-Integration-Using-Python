📄 CSV File Import and MySQL Integration Using Python
Hey! I'm new to README files, so bear with me 😅

This project demonstrates how to use Python to import data from a CSV file into a MySQL database. The CSV acts as the bridge, and Python handles everything—connecting to the database, creating a table, and inserting data automatically based on the CSV's structure.

🧠 What’s Happening?
Python connects to your MySQL database.
It reads a CSV file containing simulated global COVID-19 case reports.
It then creates a new table and inserts the CSV data into the database.

📂 Files Included
main.py – Entry point of the program.
data_processing.py – Handles data cleaning and manipulation.
data_visualization.py – (Optional) For plotting/graphing data.
database_connector.py – Handles the MySQL connection.

🛠️ Setup Instructions
Make sure you have XAMPP installed and running (MySQL service).
Create a MySQL database named: covid_data.
Clone this repository or download the files.

Run the Python scripts in this order:
main.py

⚠️ Your MySQL database name must match what’s used in the Python files (covid_data).