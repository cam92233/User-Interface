import mysql.connector

# setup mysql connection information
mysql_connection_info = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '^What4said',
    'database': 'bookworm',
    'auth_plugin': 'mysql_native_password'
}

def update(query):
    mysql_connection = mysql.connector.connect(**mysql_connection_info)
    mysql_cursor = mysql_connection.cursor()
    mysql_cursor.execute(query)
    mysql_connection.commit()
    mysql_connection.close()
    #for inserting new tuples and updating/deleting old ones

def select(query): #for retrieving info
    mysql_connection = mysql.connector.connect(**mysql_connection_info)
    mysql_cursor = mysql_connection.cursor(dictionary=True)
    mysql_cursor.execute(query)
    rows = mysql_cursor.fetchall()
    numrows = len(rows)
    mysql_connection.close()
    return [rows,numrows]
    
    
