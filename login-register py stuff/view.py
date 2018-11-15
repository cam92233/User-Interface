from mako.template import Template
from acc_handler import *
import cart_handler as ch
import book_handler as bh
from flask import request,redirect,make_response


from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['GET'])
def bookview():
    if request.cookies.get('username') != None:
        template = Template(filename=r'D:\bookworm\templates\home.htm')
        p = bh.handle_book('home','')
        resp = make_response(template.render(presidents=p,user=request.cookies.get('username'),count=request.cookies.get('count')))
        #if the request has cookies will load this
    else:
        template = Template(filename=r'D:\bookworm\static\index.html')
        resp = make_response(template.render())
    return resp

@app.route('/register', methods=['GET','POST'])
def register():
    output = open(r'D:\bookworm\static\registrationConfirmation.htm')
    output = output.read()
    acc = handle_acc('register',request.form.copy())
    output += '<h1>' + acc  + '</h1>'
    if request.method == 'POST':
        return output
    else:
        return output

@app.route('/login', methods=['GET','POST'])
def login():
    valid = handle_acc('login',request.form.copy())
    #valid = True
    if(request.method == 'POST'):
        if valid:
            template = Template(filename = r'D:\bookworm\templates\index.htm')
            #resp = make_response(template.render(user=request.form['user']))
            #resp = make_response(template.render())
            #resp = request.form['user']
            resp = redirect("/",code=302)
            resp.set_cookie('username',request.form['user'])
            num = ch.handle_cart('count',request.form['user'])
            resp.set_cookie('count',str(num))
        else:
            resp = redirect("static/loginerr.htm")
        return resp
        #load home page template 
    else:
        return redirect("localhost/static/login.htm")

@app.route('/signout')
def signout():
    resp = redirect('/')
    resp.set_cookie('username', '', expires=0)
    return resp
    
@app.route('/cart',methods=['GET','POST'])
def viewcart():
    if request.method == 'POST':
        #if they change quantity in cart
        data = request.form.copy()
        data['user'] = request.cookies.get('username')
        ch.handle_cart('quantity',data)
        resp = redirect("/cart")
        resp.set_cookie('count',str(data['qty']))#update count cookie if they entirely remove item from cart
       # resp = make_response("HELLO????")
    else:
        if int(request.cookies.get('count')) != 0:
            item,sub = ch.handle_cart('view',request.cookies.get('username'))
        #generate template
            template = Template(filename=r'D:\bookworm\templates\cart.htm')
            resp = make_response(template.render(count=request.cookies.get('count'),items=item,subtotal=sub))
        else:
            resp = redirect("static/cartproto.htm")
        #if no items in cart
        #display message 'No items in cart' or smt
    return resp

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method == 'POST':
        dictlist = bh.handle_book('search',request.form.copy())
        resp = ''
        template = Template(filename=r'D:\bookworm\templates\search.htm')
        resp = make_response(template.render(items=dictlist,acct_name=request.cookies.get('username')))
    return resp

@app.route('/b/')
def selBook():
    isbn = request.args.get('book')
    info = bh.handle_book('view',isbn)

    if request.cookies.get('username') != None:
            template = Template(filename=r'D:\bookworm\templates\book.htm')
            resp = make_response(template.render(details=info[0],count=request.cookies.get('count')))
        #if the request has cookies will load this
    else:
        y=2
        #template = Template(filename=r'D:\bookworm\templates\index.html')
        #resp = make_response(template.render())
    #isbn = request.args.get('book')
    #resp = make_response(isbn)
    #info = bh.handle_book('view',isbn)
    #template = Template(filename=r'D:\bookworm\templates\book.htm')
    #resp = make_response(template.render(details=info[0],count=request.cookies.get('count'))
    return resp

if __name__ == '__main__':
    app.run()



