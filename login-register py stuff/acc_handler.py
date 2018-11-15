from objects import Account #import account class objects.py
import acc_persist as ap

def handle_acc(case,data):
    if case == 'register':
        acc = Account(data)
        query = ap.register(acc)
        return query
    elif case == 'login':
        if ap.login(data) == 1:
            return True
        else:
            return False

