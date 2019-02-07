# import re
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


@app.route('/_calculate')
def calculate():
    salary = float(request.args.get('salary', '0'))
    otherincome = float(request.args.get('otherincome', '0'))
    prime = float(request.args.get('prime', '0'))
    netflix = float(request.args.get('netflix', '0'))
    cable = float(request.args.get('cable', '0'))
    others = float(request.args.get('others', '0'))
    rent = float(request.args.get('rent', '0'))
    groceries = float(request.args.get('groceries', '0'))
    gas = float(request.args.get('gas', '0'))
    electricity = float(request.args.get('electricity', '0'))
    wifi = float(request.args.get('wifi', '0'))
    phone = float(request.args.get('phone', '0'))

   
    
    output=0
    totalincome=salary+otherincome
    totalexpense=prime+netflix+cable+others+rent+groceries+gas+electricity+wifi+phone
    output=totalincome-totalexpense
  
            
         

    return jsonify(result=output)


@app.route('/')
def index():
    return render_template('calc_saving.html')


if __name__ == '__main__':
    app.run()