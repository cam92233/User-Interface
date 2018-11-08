from mako.template import Template
from contextlib import closing
from pprint import pprint
import mysql.connector
import cgi
from cgi import parse_qs, escape

# setup mysql connection information
mysql_connection_info = {
    'host': 'localhost',
    'user': 'web',
    'passwd': 'WebProject1!',
    'database': 'web',
    'auth_plugin': 'mysql_native_password'
}


def query_presidents(mysql_connection):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("SELECT * FROM books")
    presidents = mysql_cursor.fetchall()
    pprint(presidents)
    return presidents

def application(env, start_response):
    mysql_connection = mysql.connector.connect(**mysql_connection_info)
    start_response('200 OK', [('Content-Type', 'text/html')])
    pprint(env)
<<<<<<< HEAD
    html_template = Template(filename = 'templates/home.html')
=======
    html_template = Template(filename = 'static/index.html')
>>>>>>> 134c8975fbdb9433b808aa758a3fe857a8313dd3
    html_dict = {
       'presidents': query_presidents(mysql_connection)
    } # html_dict
    response = html_template.render(**html_dict)
    mysql_connection.close()
    return response.encode()