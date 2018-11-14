from mako.template import Template

# setup mysql connection information
mysql_connection_info = {
    'host': 'localhost',
    'user': 'web',
    'passwd': 'WebProject1!',
    'database': 'web',
    'auth_plugin': 'mysql_native_password'
} 

def searchHandler(mysql_connection,field,search):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("SELECT * FROM books WHERE {}='{}'".format(field,search))
    presidents = mysql_cursor.fetchall()
    return presidents
    
def loginHandler(username,password,mysql_connection):
        response = ""
        if(verifyLoginType(username,password,mysql_connection) == 0):
          filename = 'templates/home.html'
          html_template = Template(filename)
          html_dict = {
           'presidents': query_presidents(mysql_connection),
           'username': username
          } # html_dict
          response = html_template.render(**html_dict)
          mysql_connection.close()
          return response.encode()
        elif(verifyLoginType(username,password,mysql_connection) == 1):
          html_template = Template(filename = 'templates/ownerMainPage.htm')
          response = html_template.render()
        elif(verifyLoginType(username,password,mysql_connection) == 2):
          filename = 'templates/ownerMainPage.htm'                                # Change later
          html_template = Template(filename)
          response = html_template.render()    
        elif(verifyLoginType(username,password,mysql_connection) == 3):
          html_template = Template(filename = 'templates/adminMainPage.htm')
          response = html_template.render()
        mysql_connection.close()
        return response.encode()
        
def verifyLoginType(username,password,mysql_connection,):
    if(verifyLogin(username,password,mysql_connection)):
       mysql_cursor = mysql_connection.cursor(dictionary = True)
       mysql_cursor.execute("SELECT acct_type FROM accounts WHERE username='{}'".format(username))
       userType = mysql_cursor.fetchall()
       if(userType[0].get("acct_type") == "owner"):
         return 1
       elif(userType[0].get("acct_type") == "vendor"):
         return 2
       elif(userType[0].get("acct_type") == "admin"):
         return 3
       return 0
    else:
      return 4

def verifyLogin(username,password,mysql_connection):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("SELECT password, acct_type FROM accounts WHERE username='{}'".format(username))
    storedPassword = mysql_cursor.fetchall()
    if(storedPassword[0].get("password") == password):
      return True
    return False