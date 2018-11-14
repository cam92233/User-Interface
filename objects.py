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

def query_books(mysql_connection):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("SELECT * FROM books")
    books = mysql_cursor.fetchall()
    pprint(books)
    return books

def deleteBook(isbn,mysql_connection):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("DELETE * FROM books WHERE isbn='{}'".format(isbn))
    bookInfo = mysql_cursor.fetchall()
    pprint(bookInfo)
    return bookInfo

def updateBookStock(isbn,mysql_connection,orderAmount):
    mysql_cursor = mysql_connection.cursor(dictionary = True)
    mysql_cursor.execute("SELECT amount FROM books WHERE isbn='{}'".format(isbn))
    bookInfo = mysql_cursor.fetchall()
    amount = bookInfo - 1
    pprint(bookInfo)
    return bookInfo

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
       'books': query_books(mysql_connection)
    } # html_dict
    response = html_template.render(**html_dict)
    mysql_connection.close()
    return response.encode()


class Book:
    def __init__(self, title=None, author=None, isbn=None, publisher=None, vendor=None, stock=None, genre=None, address=None):
        self.attributes = dict()
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.vendor = vendor
        self.stock = stock
        self.genre = genre
        self.address = address
        self.attributes["Title"] = self.title
        self.attributes["Author"] = self.author
        self.attributes["ISBN"] = self.isbn
        self.attributes["Publisher"] = self.publisher
        self.attributes["Vendor"] = self.vendor
        self.attributes["Stock"] = self.stock
        self.attributes["Genre"] = self.genre
        self.attributes["Address"] = self.address
    def returnBookAttributesDict(self):
        return self.attributes
class Account:
    def __init__(self, name, email, birthdate, username, password, uid):
        # INSERT INTO `accounts` VALUES ('Matt', 'mdchap@uga.edu', '1995-02-02', mdchap, 00000000, admin, 0);
        pass
class Admin(Account):
    def __init__(self):
        pass
class Vendor(Account):
    def __init__(self):
        pass
class Customer(Account):
    def __init__(self):
        pass
class Address:
    def __init__(self):
        self.street = None
        self.street_n = None
        self.apt = None
        self.apt_n = None
        self.zip_code = None
        self.country = None
        self.state = None
        self.city = None
class Order:
    def __init__(self):
        self.items = list()
        self.sale_amt = None
        self.tax = None
        self.total = None
class Report:
    def __init__(self):
        pass
class VendorBookList:
    pass
class BookList:
    def __init__(self):
        self.books = list()
    def addBook(self, book):
        self.books.append(book)
class AccountList:
    def __init__(self):
        self.accounts = list()
    def addAccount(self, account):
        self.accounts.append(account)
class OrderList:
    def __init__(self):
        self.orders = list()
class ReportList:
    def __init__(self):
        self.reports = list()
class Database:
    def __init__(self):
        self.books = BookList()
        self.accounts = AccountList()
        self.orders = OrderList()
        self.reports = ReportList()
class ShoppingCart:
    pass
class Payment:
    pass
class Cash(Payment):
    pass
class Check(Payment):
    pass
class CreditCard(Payment):
    pass
class Promotion:
    pass
#class Guest:
#controllers/handlers

if __name__ == "__main__":
    pass
