import mysql.connector

# setup mysql connection information
mysql_connection_info = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'INSERT PASS',
    'database': 'DB NAME',
    'auth_plugin': 'mysql_native_password'
}

def update(query):
    mysql_connection = mysql.connector.connect(**mysql_connection_info)
    mysql_cursor = mysql_connection.cursor()
    mysql_cursor.execute(query)
    mysql_connection.commit()
    mysql_connection.close()
    #for inserting new tuples and updating/deleting old ones
    return "hello?"

def select(query): #for retrieving info
    mysql_connection = mysql.connector.connect(**mysql_connection_info)
    mysql_cursor = mysql_connection.cursor()
    mysql_cursor.execute(query)
    rows = mysql_cursor.fetchall()
    numrows = len(rows)
    mysql_connection.close()
    return [rows,numrows]
    
    
