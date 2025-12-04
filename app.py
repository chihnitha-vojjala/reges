from flask import flask,render_template,request
app_flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
def submit():
    fname request.from['fname']
    lname request.from['lname']
    return render_template("greeting.html:fname:fname,lname:lname")
if(__name__"__main__")
    app.run(debug==true)
    
