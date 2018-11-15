import DB_access as db
from datetime import date
#table for low inventory notices? then print them when owner visits page?

def checkInventory(isbn):
    #whenever items are checked out and stock of items changes, check to see if
    #below certain threshold...guess like 5
    query = 'select amount from books where isbn = \'' + isbn +'\''
    if db.select(query)[0][0]['amount'] < 5:
        #put low inventory notice in table...
        #or however do

def salesReport():
    query = 'select * from orders'
    orders = db.select(query)[0]
    totalmoneys = 0
    for i in orders:
        totalmoneys += i['total']
    return orders,totalmoneys
    

def dayReport():
    today = str(date.today())
    query = 'select * from orders where order_date ='  + today
    orders = db.select(query)[0]
    totalmoneys = 0
    for i in orders:
        totalmoneys += i['total']
    return orders, totalmoneys
    
    
