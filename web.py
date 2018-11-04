from mako.template import Template
from pprint import pprint
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

def query_presidents():
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("SELECT * FROM presidents")
    presidents = mysql_cursor.fetchall()
    pprint(presidents)
    return presidents

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    pprint(env)
    html_template = Template(filename = 'static/index.html')
    html_dict = {
   #     'presidents': query_presidents()
    } # html_dict
    response = html_template.render(**html_dict)
    return response.encode()