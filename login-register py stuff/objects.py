class Address:
    def __init__(self,ad1,ad2,st,zip,city):
        self.ad1 = ad1
        self.ad2 = ad2
        self.st = st
        self.zip = zip
        self.city = city

class Account:
    def __init__(self,data):
        self.addr = Address(data['ad1'],data['ad2'],data['st'],data['zip'],data['city'])
        self.name = data['name']
        self.email = data['email']
        self.date = data['date']
        self.user = data['user']
        self.passw = data['pass']
        self.type = 'cust'
        
#other domain classes not included for simplicity
