from flask import Flask,request
from flask import Flask, render_template
import requests
import json
with open('data.json','r')as f:
    data=json.load(f)
app = Flask(__name__)

@app.route("/")
def hello_world():
    # data=json.load('../data.json')
    return render_template('index.html',data=data)

@app.route("/view/<int:id>")
@app.route('/view/')
def about(id=None):
    if id==None:
        return data
    if id>len(data):
        return '<p>doesnt exist</p>'
    else:
        return data[id]


@app.route("/adduser", methods=['POST','GET'])
def adduser():
    if request.method=='POST':
        form_data={}
        form_data['name']=request.form['nm']
        form_data['number']=request.form['num']
        form_data['email']=request.form['mail']
        data.append(form_data)
    with open('data.json','w')as f:
        json.dump(data,f,indent=4)
    return render_template('add_form.html')


@app.route("/removeuser", methods=["GET","POST"])
def removeuser():
    if request.method=="POST":
        for i in range(len(data)-1):
            if data[i]['name']==request.form['nm']:
                del data[i]
    with open('data.json','w')as f:
        json.dump(data,f,indent=4)
    return render_template('remove.html')
    
   
app.run(debug=True)