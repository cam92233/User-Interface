from objects import account #import account class objects.py
import user_persist as up

def handle_acc(case,data):
    if case == 'register':
        acc = Account(data)#create account object
        up.register(acc) #method in persist class, which connects to DB
    #if elses n' shit = other cases handled as well
    #this method will be called from the view layer for all user related garbage
    return acc #not relevant for much except when need to retrieve user info

