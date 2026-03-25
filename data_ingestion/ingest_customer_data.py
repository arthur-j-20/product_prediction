from mssql_python import connect
import pandas as pd
import os


def connect_to_db():
    conn = connect(
    "Server=localhost;"
    "Database=insurance;"
    "Uid=sys_santo;"
    "Pwd=NewPassword;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)
    cursor = conn.cursor()
    return conn, cursor

def read_customer_data():
    return pd.read_csv('data\customer_data.csv')

def get_query_data(customer_data):
    data_dict = customer_data.to_dict('records')
    print(data_dict)
    return data_dict


def insert_data(cursor, query_data):
    try:
        sql = "INSERT INTO products.customers ([name], [age]) VALUES (?, ?)"
        for record in query_data:
            cursor.execute(sql, (record['Name'], record['Age']))
        return "Data inserted successfully"
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Error occurred while inserting data"


def ingest_customer_data():
    customer_data = read_customer_data()
    query_data = get_query_data(customer_data)
    # Connect to the SQL Server database
    conn, cursor = connect_to_db()
    # Insert data into the database
    response = insert_data(cursor, query_data)
    conn.commit()
    conn.close()
    return response
    


data = ingest_customer_data()
print(data)