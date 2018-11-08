import user_persist as up
from address import address

class Address:
    def __init__(ad1,ad2,st,zip):
        self.ad1 = ad1
        self.ad2 = ad2
        self.st = st
        self.zip = zip

class Account:
    def __init__(self,name,email,date,user,addr,passw,acct_type):
        self.name = name
        self.user = user
        self.passw = passw
        self.date = date
        self.email = email
        self.acct_type = 'cust' #default val until permissions changed
        #kinda wanna put these in a dict instead or list...
        #then create address, parsed from data but i aint doin tht here rn
        self.addr = Address(addr)

        #getters,setters..


#other domain classes not included for simplicity
