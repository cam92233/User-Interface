import DB_access as db

def getNumItems(user): #used to set number in cookie to show beside the cart link in nav bar
    query = 'select count(cust_id) from cart where cust_id=\''+user+'\' group by cust_id'
    inf = db.select(query)
    if inf[1] != 0: #check if any tuples were returned
        return inf[0][0]['count(cust_id)']
    else:
        return 0 #if no items in cart
#returns number of items in cart

def addItem(user,isbn): #or just send both in dict or list
    #if first time putting item in cart
    query =  'insert into cart(cust_id,isbn,qty) values (\'' + user + '\',\'' + isbn + '\',1)'
    db.update(query)

def updateItem(user,isbn,qty): #update quantity of items
    #accessed from viewcart page
    if int(qty) != 0:
        query = 'update cart set qty =' + qty + ' where cust_id =\'' + user + '\' and isbn=\'' + isbn + '\''
    else: #if customer set quantity to zero, just remove from cart
        query = 'delete from cart where cust_id =\'' + user + '\' and isbn=\'' + isbn + '\''
    db.update(query)

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
        info.append(dict) #get the price totals for each book in cart
        j=j+1
    #assigns list of dicts with information of books in the cart
    return info #return the list

