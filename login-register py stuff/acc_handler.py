from objects import Account #import account class objects.py
import acc_persist as ap

def handle_acc(case,data):
    if case == 'register':
        acc = Account(data)
        query = ap.register(acc)
        return query
    elif case == 'login':
        return ap.login(data)
    elif case == 'type':
        return ap.verify_type
    elif case == 'profile':
        return ap.get_info(data)
