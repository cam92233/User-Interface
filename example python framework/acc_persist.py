import DB_access as db
import Account from objects

def register(data):
    query = 'insert into accounts(name,email,birthdate,username,password,acct_type) values (' + data.allbutaddress + ')'
    #likely loop thru data but this pseudo
    db.update(query)
    #also need to separate address at this point
    #and get cust_id from newly inserted tuple
    #actually why do we have id when usernames must be unique
    id = db.select('select id from accounts where username = ' + data[username]) #pseudocode as hell 
    query = 'insert into address(add_line_1,add_line_2,state,zip,cust_id) values (' + data.addr + ')'
    db.insert(query)

def login(data):
    #check matching pass for user in db

def delete(username):
    #del account

def update(data):
    #change account info

def retrieve(username):
    #retrieve tuple (and tuple from address) via username and make account object
