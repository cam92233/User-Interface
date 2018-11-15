import book_persist as bp

def handle_book(case,data):
    if case == 'search':
        return bp.getSearch(data)
    elif case == 'view':
        return bp.getBook(data)
    elif case == 'home':
        return bp.getAll()


res = handle_book('home','')
for i in res:
    print(i)
