import streamlit as st
import mysql.connector
import pandas as pd

# Function to connect to MySQL
def connect_to_mysql():
    mydb = {
        'host': 'localhost',
        'user': 'root',
        'password': 'bhavika20',
        'database': 'rental'
    }
    try:
        conn = mysql.connector.connect(**mydb)
        return conn
    except mysql.connector.Error as err:
        st.error(f"Error connecting to MySQL: {err}")
        return None

# Function to fetch data from MySQL and display it
def fetch_and_display_data(table_name):
    conn = connect_to_mysql()
    if conn:
        query = f"SELECT * FROM {table_name};"
        try:
            df = pd.read_sql(query, conn)
            st.write(f"Displaying data from {table_name} table:")
            st.write(df)
        except mysql.connector.Error as err:
            st.error(f"Error executing query: {err}")
        finally:
            conn.close()

# Function to delete a record from the selected table
def delete_from_table(table_name, primary_key_column, primary_key_value):
    conn = connect_to_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            query = f"DELETE FROM {table_name} WHERE {primary_key_column} = '{primary_key_value}';"
            cursor.execute(query)
            conn.commit()
            st.success("Record deleted successfully!")
        except mysql.connector.Error as err:
            st.error(f"Error deleting record: {err}")
        finally:
            conn.close()

# Function to get table attributes
def get_table_attributes(table_name):
    conn = connect_to_mysql()
    attributes = []
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(f"DESC {table_name};")
            attributes = [row[0] for row in cursor.fetchall()]
        except mysql.connector.Error as err:
            st.error(f"Error getting table attributes: {err}")
        finally:
            conn.close()
    return attributes

# Function to insert a record into the selected table
def insert_into_table(table_name, **kwargs):
    conn = connect_to_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            columns = ', '.join(kwargs.keys())
            values = ', '.join([f"'{value}'" if value != '' else 'NULL' for value in kwargs.values()])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
            cursor.execute(query)
            conn.commit()
            st.success("Record inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"Error inserting record: {err}")
        finally:
            conn.close()

# Function to update a record in the selected table
def update_table(table_name, primary_key_column, primary_key_value, **kwargs):
    conn = connect_to_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            updates = ', '.join([f"{key} = '{value}'" for key, value in kwargs.items() if key != primary_key_column])
            query = f"UPDATE {table_name} SET {updates} WHERE {primary_key_column} = '{primary_key_value}';"
            cursor.execute(query)
            conn.commit()
            st.success("Record updated successfully!")
        except mysql.connector.Error as err:
            st.error(f"Error updating record: {err}")
        finally:
            conn.close()

# Function to check login credentials
def check_login(username, password):
    return (username == 'admin' and password == 'adminpassword') or (username == 'user' and password == 'user1')

# Function to set custom CSS styles
def set_custom_css():
    st.markdown(
        """
        <style>
            body {
                background-color: #f7caa8;  /* Set background color to #f7caa8 */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main Streamlit app
def main():
    set_custom_css()
    
    st.title("Rental Property Management System")

    # Login Section
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.sidebar.button("Login"):
        # Check if the login credentials are correct
        if check_login(username, password):
            st.sidebar.success("Login successful!")
            st.session_state["logged_in"] = True
            if username == 'admin':
                st.sidebar.write("Welcome Admin")
            else:
                st.sidebar.write("Welcome User")
        else:
            st.sidebar.error("Invalid username or password.")
            st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        st.sidebar.title("Options")
        if username == 'admin':
            tables = ['Roles', 'Permissions', 'User', 'Sellers', 'Buyers', 'Property', 'Registrations']
        else:
            tables = ['Property', 'Sellers']
        selected_table = st.sidebar.selectbox("Select table", tables)

        operation = st.sidebar.selectbox("Select operation", ("View", "Insert", "Delete", "Update"), index=0)

        if operation == "View":
            if selected_table in tables:
                fetch_and_display_data(selected_table)
            else:
                st.error("Invalid table selected.")
        elif operation == "Delete":
            if selected_table in tables and username == 'admin':
                st.write(f"Deleting record from the {selected_table} table:")
                primary_key_column = st.selectbox("Select primary key column", get_table_attributes(selected_table))
                primary_key_value = st.text_input(f"Enter value for {primary_key_column}:")
                delete_button = st.button("Delete")
                if delete_button:
                    delete_from_table(selected_table, primary_key_column, primary_key_value)
            else:
                st.error("Invalid table selected or you don't have permission to delete records.")
        elif operation == "Insert":
            if selected_table in tables:
                st.write(f"Inserting record into the {selected_table} table:")
                attributes = get_table_attributes(selected_table)
                values = {}
                for attribute in attributes:
                    if attribute != "Date":
                        values[attribute] = st.text_input(f"Enter {attribute}:")
                    else:
                        values[attribute] = st.date_input(f"Enter {attribute}:")
                insert_button = st.button("Insert")
                if insert_button:
                    insert_into_table(selected_table, **values)
            else:
                st.error("Invalid table selected.")
        elif operation == "Update":
            if selected_table in tables and username == 'admin':
                st.write(f"Updating record in the {selected_table} table:")
                primary_key_column = st.selectbox("Select primary key column", get_table_attributes(selected_table))
                primary_key_value = st.text_input(f"Enter value for {primary_key_column}:")
                attributes = get_table_attributes(selected_table)
                values = {}
                for attribute in attributes:
                    if attribute != primary_key_column and attribute != "Date":
                        values[attribute] = st.text_input(f"Enter new value for {attribute}:")
                    elif attribute != primary_key_column:
                        values[attribute] = st.date_input(f"Enter new value for {attribute}:")
                update_button = st.button("Update")
                if update_button:
                    update_table(selected_table, primary_key_column, primary_key_value, **values)
            else:
                st.error("Invalid table selected or you don't have permission to update records.")
        else:
            st.warning("Only 'View', 'Insert', 'Update', and 'Delete' operations are supported currently.")

if __name__ == "__main__":
    main()







