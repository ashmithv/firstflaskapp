from flask import Flask,request,render_template,make_response,session

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/sign.html', methods=['GET' , 'POST'] )
def login():
    if not request.cookies.get('tour'):
        if request.method == 'POST':
            fname=request.form.get('fname')
            lastname=request.form.get('lname')
            address=request.form.get('address')
            passwrd=request.form.get('password')
            cpasswrd=request.form.get('cpassword')
            fav = str(request.form['favourite'])
            response=make_response("Kindly refresh the page")
            response.set_cookie('tour' , fav)
            return response

    else:
        response=make_response(render_template('welcome.html' , cookie = str(request.cookies.get('tour') )))
        return response
       
    return render_template('sign.html')

if __name__=='__main__':
    app.run(debug = True)
