import DB_access as db

def getNumItems(user):
    query = 'select count(cust_id) from cart where cust_id=\''+user+'\' group by cust_id'
    inf = db.select(query)
    if inf[1] != 0: #check if any tuples were returned
        return inf[0][0]['count(cust_id)']
    else:
        return 0 #if no items in cart

def addItem(user):
    query = ''

def getItems(user):
    query = 'select isbn,qty from cart where cust_id=\''+user+'\''
    isbns = db.select(query)[0]
    info = []
    j = 0
    for i in isbns:
        query = 'select title,author,price,pic_url,isbn from books where isbn=\'' + i['isbn']+'\''
        dict = db.select(query)[0][0]
        dict['qty'] = i['qty']
        dict['total'] = float(dict['qty'])*float(dict['price'])
        info.append(dict)
        j=j+1
    #assigns list of dicts with information of books in the cart
    return info

