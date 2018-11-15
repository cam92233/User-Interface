import cart_persist as cp

def handle_cart(case,data):
    if case == 'count':
        return cp.getNumItems(data)
    if case == 'view':
        books = cp.getItems(data)
        subtotal = 0
        for i in books:
            subtotal += i['total']
        return books,subtotal
    if case == 'quantity':
        cp.updateItem(data['user'],data['isbn'],data['qty'])
    if case == 'add':
        cp.addItem(data['user'],data['isbn'])
