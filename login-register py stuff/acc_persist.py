import DB_access as db

def register(acc):
    query = 'insert into accounts(name,email,birthdate,username,password,acct_type) values (\'' + acc.name+'\',\''+acc.email+'\','+acc.date+',\''+acc.user+'\',\''+acc.passw+'\',\''+acc.type+'\')'
    db.update(query)
    query = 'insert into address(add_line_1,add_line_2,state,zip,cust_id,city) values (\''+acc.addr.ad1+'\',\''+acc.addr.ad2+'\',\''+acc.addr.st+'\',\''+acc.addr.zip+'\',\''+acc.user+'\',\''+acc.addr.city+'\')'
    db.update(query)
    return query
#worthless if ur not using the domain classes
#can also be called by an admin who is adding a user

def login(creds):
    query = 'select * from accounts where username=\''+creds['user']+'\' and password=\''+creds['pass']+'\''
    num = db.select(query)[1]#returns number of tuples found by query
    if num == 0:
        return False
    else:
        return True
#returns true or false depending on if user credentials are found in database
    
def verify_type(creds): 
    return db.select('SELECT acct_type FROM accounts WHERE username=\''+creds['user']+'\'')[0][0]['acct_type']

def give_perm(user,level):
    query = 'update accounts set acct_type = \''+level+'\' where username = \'' + user + '\''
    db.update(query)
#used by admin to set user permissions: vendor, admin, owner, or cust (demoted..)

def rmv_user(user):
    query = 'delete from accounts where username = \'' + user + '\''
    db.update(query)
#called by admin to delete accounts

def update_user(data): #contains dict of all user attributes?
    y = 2
    #act not sure how this'll be implemented atm
    #a dict with only the attributes to be changed, then get the keys for the dict in a list and iterate thru tht in the update statement
    #i guess

def get_info(data):
    query = 'select * from accounts where username=\'' + data 
#if promos are one time use for user maybe there should be something here...
