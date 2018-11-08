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
    def __init__(self):
        self.username = None
        self.password = None
        self.account_type = None
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
