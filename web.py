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

def getBookInfo(title,mysql_connection):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("SELECT * FROM books WHERE isbn='{}'".format(title))
    bookInfo = mysql_cursor.fetchall()
    pprint(bookInfo)
    return bookInfo

def query_presidents(mysql_connection):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("SELECT * FROM books")
    presidents = mysql_cursor.fetchall()
    pprint(presidents)
    return presidents

def application(env, start_response):
    mysql_connection = mysql.connector.connect(**mysql_connection_info)
    start_response('200 OK', [('Content-Type', 'text/html')])
    qs = parse_qs(env['QUERY_STRING'])
    if len(qs) > 0:
      detailedBook = cgi.escape(str(qs.get("book","")[0]))
      if len(detailedBook) > 0:
        html_template = Template(filename = 'templates/detailedTemplate.html')
        html_dict = {
           'bookInfo': getBookInfo(detailedBook,mysql_connection)
        }
        response = html_template.render(**html_dict)
        mysql_connection.close()
        return response.encode()
    pprint(env)
    html_template = Template(filename = 'templates/home.html')
    html_dict = {
       'presidents': query_presidents(mysql_connection)
    } # html_dict
    response = html_template.render(**html_dict)
    mysql_connection.close()
    return response.encode()