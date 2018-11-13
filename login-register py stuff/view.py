from mako.template import Template
from acc_handler import *
from flask import request,redirect,make_response


from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['GET'])
def bookview():
    if request.cookies.get('username') != None:
        template = Template(filename=r'D:\bookworm\templates\index.htm')
        resp = make_response(template.render(user=request.cookies.get('username')))
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
        else:
            resp = redirect("static/loginerr.htm",code=302)
        return resp
        #load home page template 
    else:
        return redirect("localhost/static/login.htm", code=302)

@app.route('/signout')
def signout():
    resp = redirect('/', code=302)
    resp.set_cookie('username', '', expires=0)
    return resp
    

if __name__ == '__main__':
    app.run()



