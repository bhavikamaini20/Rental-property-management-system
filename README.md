# Rental Property Management System

## Overview

The Rental Property Management System is a web application built using Streamlit that allows users to manage rental property data. Users can view, insert, delete, and update records in a MySQL database. The application includes role-based access, with different functionalities available for admin and regular users.

## Features

- **Role-based access control**: Different functionalities for admin and regular users.
- **CRUD operations**: Create, Read, Update, and Delete records in the MySQL database.
- **User authentication**: Simple login mechanism.
- **Custom CSS styling**: Personalized interface design.
- **Real-time data fetching**: Display data from the MySQL database in real-time.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Screenshots](#screenshots)
- [Contributing](#contributing)


## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/bhavika20/rental-property-management.git
   cd rental-property-management
   ```

2. **Create a virtual environment and activate it**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the MySQL database**:
   - Ensure you have MySQL installed and running on your machine.
   - Create a database named `rental` and set up the necessary tables.

5. **Configure database connection**:
   - Modify the `connect_to_mysql` function in `app.py` to match your MySQL server credentials.

## Usage

1. **Run the Streamlit application**:
   ```sh
   streamlit run app.py
   ```

2. **Login**:
   - Use the sidebar to enter your username and password.
   - The default credentials are:
     - Admin: `admin` / `adminpassword`
     - User: `user` / `user1`

3. **Select Operations**:
   - Use the sidebar to choose the table and operation (View, Insert, Delete, Update).

## Functions

### `connect_to_mysql()`
Connects to the MySQL database using the provided credentials.

### `fetch_and_display_data(table_name)`
Fetches and displays data from the specified table.

### `delete_from_table(table_name, primary_key_column, primary_key_value)`
Deletes a record from the specified table.

### `get_table_attributes(table_name)`
Gets the attributes (columns) of the specified table.

### `insert_into_table(table_name, **kwargs)`
Inserts a new record into the specified table.

### `update_table(table_name, primary_key_column, primary_key_value, **kwargs)`
Updates a record in the specified table.

### `check_login(username, password)`
Checks the login credentials.

### `set_custom_css()`
Sets custom CSS styles for the application.

### `main()`
Main function to run the Streamlit application.

## Screenshots

![image](https://github.com/bhavikamaini20/Rental-property-management-system/assets/121393411/dfba09aa-543d-4246-b170-3b8293c67a20)
![image](https://github.com/bhavikamaini20/Rental-property-management-system/assets/121393411/13bf3b49-1d83-47fa-9607-ee4a9fb81c61)
![image](https://github.com/bhavikamaini20/Rental-property-management-system/assets/121393411/2240ad4c-06af-4680-b56d-954b5ee94a05)
![image](https://github.com/bhavikamaini20/Rental-property-management-system/assets/121393411/c8c19c2e-5776-4948-89a9-a090e9527ef0)

![image](https://github.com/bhavikamaini20/Rental-property-management-system/assets/121393411/cfa9792d-d3b9-43ee-9f8b-b8b1b1d87fbb)
![image](https://github.com/bhavikamaini20/Rental-property-management-system/assets/121393411/953fc344-4e22-4ef3-b9b3-d41dc8e519c5)

![image](https://github.com/bhavikamaini20/Rental-property-management-system/assets/121393411/8af688f6-84fe-4bbe-a304-022addc5f86b)


## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

