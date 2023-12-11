# pip install psycopg2

import pandas as pd
import psycopg2

def get_dataframe(table='students', database='neem', host='localhost', user='neem_user', password='password'):

    # Connect to the PostgreSQL database
    connection = psycopg2.connect(host=host, user=user, password=password, database=database)

    # Create a cursor to execute queries
    cursor = connection.cursor()

    # Execute a SELECT query to fetch data from the table
    query = f"SELECT * FROM {table}"
    cursor.execute(query)

    # Fetch all rows from the result set
    data = cursor.fetchall()

    # Get column names from the cursor description
    columns = [column[0] for column in cursor.description]

    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    return df
