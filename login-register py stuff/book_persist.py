import DB_access as db

def getSearch(data):
    query = 'select * from books where ' + data['cat'] + ' = \'' + data['search'] + '\''
    return db.select(query)[0]
        
def getBook(isbn):
    query = 'select * from books where isbn = \'' + isbn + '\''
    return db.select(query)[0]

def getAll():
    query= 'select * from books'
    return db.select(query)[0]
