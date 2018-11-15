from mako.template import Template
from contextlib import closing
from handlers import *
from pprint import pprint
import mysql.connector
import cgi
import uwsgi
from cgi import parse_qs, escape
  
def registrationCheck(mysql_connection,username):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("SELECT username FROM accounts WHERE username='{}'".format(username))
    storedPassword = mysql_cursor.fetchall()
    if(len(storedPassword)==0):
      return True
    return False
    
def getBookInfo(title,mysql_connection):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("SELECT * FROM books WHERE isbn='{}'".format(title))
    bookInfo = mysql_cursor.fetchall()
    return bookInfo

def registerUserAdmin(mysql_connection,name,email,address,birthdate,username,password,acct_type):
    if(registrationCheck(mysql_connection,username)):
      mysql_cursor = mysql_connection.cursor(dictionary = True)
      mysql_cursor.execute("INSERT INTO accounts (name,email,birthdate,username,password,acct_type) values('{}','{}','{}','{}','{}','{}')".format(name,email,birthdate,username,password,acct_type))
      mysql_connection.commit()

def registerUser(mysql_connection,name,email,address,birthdate,username,password):
    if(registrationCheck(mysql_connection,username)):
      mysql_cursor = mysql_connection.cursor(dictionary = True)
      mysql_cursor.execute("INSERT INTO accounts (name,email,birthdate,username,password,acct_type) values('{}','{}','{}','{}','{}','{}')".format(name,email,birthdate,username,password,"customer"))
      mysql_connection.commit()
      
def updateBook(mysql_connection):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("UPDATE books SET price=price-1.0 WHERE title='Test Title'")
    mysql_connection.commit()
    pprint("UpdateBook")   
          
def application(env, start_response):
    mysql_connection = mysql.connector.connect(**mysql_connection_info)
    start_response('200 OK', [('Content-Type', 'text/html')])
    username = "Account"
    qs = parse_qs(env['QUERY_STRING'])
    if len(qs) > 0:
      # if(len(qs) == 1)
      # page = qs.get("page","")
      action = qs.get("update",0)
      if(action !=0):
        action = action[0]
        action = int(action)
      if(action == 1):
        updateBook(mysql_connection)
        html_template = Template(filename = 'templates/home.html')
        html_dict = {
         'presidents': query_presidents(mysql_connection),
         'username': username
        } # html_dict
        response = html_template.render(**html_dict)
        mysql_connection.close()
        return response.encode()
      else:
        searchText = qs.get("search","")
        if len(searchText) > 0:
          searchText = str(searchText[0])
        searchType = qs.get("radiobutton","")
        if len(searchType) > 0:
          searchType = str(searchType[0])
        if not len(searchText) > 0:
          detailedBook = qs.get("book","")
          if(str(detailedBook) != ""):
            detailedBook = cgi.escape(str(detailedBook[0]))
          if len(detailedBook) > 0:
            html_template = Template(filename = 'templates/detailedTemplate.html')
            html_dict = {
               'bookInfo': getBookInfo(detailedBook,mysql_connection)
            }
            response = html_template.render(**html_dict)
            mysql_connection.close()
            return response.encode()
        if len(searchText) > 0:
          html_template = Template(filename = 'templates/home.html')
          html_dict = {
           'presidents': searchHandler(mysql_connection,searchType,searchText),
           'username': username
          } # html_dict
          response = html_template.render(**html_dict)
          mysql_connection.close()
          return response.encode()
    if env['REQUEST_METHOD'] == 'POST':
      content_length = int(env.get('CONTENT_LENGTH', 0))
      post_data = env['wsgi.input'].read(content_length)
      qs = parse_qs(post_data)
      if(len(qs) == 2):
        username = qs.get("username".encode(),"")[0].decode('ASCII')
        password = qs.get("password".encode(),"")[0].decode('ASCII')
        return loginHandler(username,password,mysql_connection)
      if(len(qs) == 7):
        username = qs.get("username".encode(),"")[0].decode('ASCII')
        password = qs.get("password".encode(),"")[0].decode('ASCII')
        email = qs.get("email".encode(),"")[0].decode('ASCII')
        name = qs.get("name".encode(),"")[0].decode('ASCII')
        address = qs.get("address".encode(),"")[0].decode('ASCII')
        birthdate = qs.get("birthdate".encode(),"")[0].decode('ASCII')
        acct_type =  qs.get("acct_type".encode(),"")[0].decode('ASCII')
        registerUserAdmin(mysql_connection,name,email,address,birthdate,username,password,acct_type)
        html_template = Template(filename = 'static/manageUsers.htm')
        html_dict = {
           'accounts': showAccounts(mysql_connection)
        } # html_dict
        response = html_template.render(**html_dict)
        mysql_connection.close()
        return response.encode()
      else:
        username = qs.get("username".encode(),"")[0].decode('ASCII')
        password = qs.get("password".encode(),"")[0].decode('ASCII')
        email = qs.get("email".encode(),"")[0].decode('ASCII')
        name = qs.get("name".encode(),"")[0].decode('ASCII')
        address = qs.get("address".encode(),"")[0].decode('ASCII')
        birthdate = qs.get("birthdate".encode(),"")[0].decode('ASCII')
        registerUser(mysql_connection,name,email,address,birthdate,username,password)
    html_template = Template(filename = 'templates/home.html')
    username = "Account"
    html_dict = {
       'presidents': query_presidents(mysql_connection),
       'username': username
    } # html_dict
    response = html_template.render(**html_dict)
    mysql_connection.close()
    return response.encode()
