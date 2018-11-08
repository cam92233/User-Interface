import mysql.connector

# setup mysql connection information
mysql_connection_info = {
    'host': 'localhost',
    'user': 'pj03',
    'passwd': 'Project3!',
    'database': 'pj03',
    'auth_plugin': 'mysql_native_password'
}

mysql_connection = mysql.connector.connect(**mysql_connection_info)
mysql_cursor = mysql_connection.cursor()

def update(query):
    mysql_cursor.execute(query)
    #for inserting new tuples and updating/deleting old ones

def select(query): #for retrieving info
    mysql_cursor.execute(query)
    return mysql_cursor.fetchall() 
    
    
