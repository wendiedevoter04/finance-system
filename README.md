Personal Finance System (CLI Application)

A simple command-line application built in Python to track personal expenses and understand spending patterns. The system stores data locally using JSON, making it lightweight and easy to run without any external database setup.

This project was built to explore how data persistence works in real applications and how users can interact with structured systems through the terminal.

What this project does

The application allows users to add, view and organize expenses directly from the terminal. Each expense is stored with a category, making it possible to see how money is distributed across different spending areas.

All data is saved locally in a JSON file, ensuring persistence even after the program is closed.

Key features

Add new expenses with amount and category
Store data persistently using JSON
View all recorded expenses
Group and analyze spending by category
Simple interactive command-line interface

Tech stack

Python
JSON for data storage
Built-in file handling

How it works

The system runs in a continuous loop in the terminal. The user interacts with a menu to add or view expenses. Each entry is stored in a structured JSON format.

When data is retrieved, it is parsed and displayed in a readable format, allowing the user to understand their spending behavior over time.

What I learned

This project helped me understand how data persistence works outside of databases. I learned how to structure data using JSON and how to manage file reading and writing in Python.

It also improved my understanding of building simple interactive systems that respond to user input in real time.

Possible improvements

Add editing and deleting of expenses
Introduce data visualization for spending trends
Add export options (CSV or Excel)
Improve input validation and error handling
Upgrade into a web-based version using Flask or FastAPI

Project summary

A Python-based command-line finance tracker that stores and manages personal expenses using JSON. The project demonstrates practical understanding of file handling, structured data storage and basic system design in Python.
