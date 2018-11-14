import DB_access as db

def register(acc):
    query = 'insert into accounts(name,email,birthdate,username,password,acct_type) values (\'' + acc.name+'\',\''+acc.email+'\','+acc.date+',\''+acc.user+'\',\''+acc.passw+'\',\''+acc.type+'\')'
    db.update(query)
    query = 'insert into address(add_line_1,add_line_2,state,zip,cust_id,city) values (\''+acc.addr.ad1+'\',\''+acc.addr.ad2+'\',\''+acc.addr.st+'\',\''+acc.addr.zip+'\',\''+acc.user+'\',\''+acc.addr.city+'\')'
    db.update(query)
    return query

def login(creds):
    query = 'select * from accounts where username=\''+creds['user']+'\' and password=\''+creds['pass']+'\''
    return db.select(query)
