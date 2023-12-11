from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd
from cassandra.query import SimpleStatement

def cassandra_to_pandas_dataframe(session, table_name, fetch_size=1000):
    # Select all rows from the Cassandra table
    select_query = f"SELECT * FROM {table_name}"
    statement = SimpleStatement(select_query, fetch_size=fetch_size)
    rows = session.execute(statement)

    # Convert the result set to a list of dictionaries
    data_records = [dict(row) for row in rows]

    # Create a Pandas DataFrame
    df = pd.DataFrame(data_records)

    return df


def create_cassandra_connection(
    contact_points=['localhost'],
    username='your_username',
    password='your_password',
    keyspace='your_keyspace'
):
    # Set up Cassandra authentication if needed
    auth_provider = PlainTextAuthProvider(username=username, password=password)

    # Connect to the Cassandra cluster
    cluster = Cluster(contact_points=contact_points, auth_provider=auth_provider)
    session = cluster.connect(keyspace)

    return session


def close_cassandra_connection(session):
    # Close the Cassandra session and cluster connection
    session.shutdown()

def create_table(session):
    # Define your table schema
    create_table_query = """
        CREATE TABLE IF NOT EXISTS your_table_name (
            column1_type data_type,
            column2_type data_type,
            ...
            PRIMARY KEY (primary_key_column)
        )
    """
    session.execute(create_table_query)

def pandas_dataframe_to_cassandra(session, dataframe, table_name):
    # Convert Pandas DataFrame to a list of dictionaries
    data_records = dataframe.to_dict(orient='records')

    # Insert data into Cassandra
    for record in data_records:
        insert_query = f"""
            INSERT INTO {table_name} (column1, column2, ...)
            VALUES ({record['column1']}, {record['column2']}, ...)
        """
        session.execute(insert_query)

if __name__ == "__main__":
    # Sample DataFrame
    data = {'column1': [1, 2, 3],
            'column2': ['A', 'B', 'C']}
    df = pd.DataFrame(data)

    # Cassandra connection
    cassandra_session = create_cassandra_connection()

    # Table creation (run this only once)
    create_table(cassandra_session)

    # Insert DataFrame into Cassandra table
    pandas_dataframe_to_cassandra(cassandra_session, df, 'your_table_name')

    # Close Cassandra connection
    close_cassandra_connection(cassandra_session)
