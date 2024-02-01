from flask import Flask,render_template,request,jsonify
from ChatBot_Response import chatbot_response
from ChatBot_Response_child import chatbot_response1
from women import chatbot_response2

import json
app = Flask(__name__,template_folder='template/')
t=""
@app.route("/")
def index_get():
    return render_template("index.html")
@app.route("/predict",methods=['POST'])
def predict():
    text=request.get_json().get("message")
    
    res= chatbot_response(text)
    
    message={"answer":res}
    return jsonify(message)
@app.route('/ChatBot_full_page/')
def register():
    return render_template('ChatBot_full_page.html')
# @app.route("/pre",methods=['POST'])
# def pre():
#     text=request.get_json().get("message")
    
#     res= chatbot_response(text)
    
#     message={"answer":res}
#     return jsonify(message)
# print(chatbot_response("hi"))
@app.route('/ChatBot_child/')
def register1():
    return render_template('ChatBot_child.html')

@app.route('/ChatBot_female/')
def register2():
    return render_template('ChatBot_female.html')

# Child ChatBot Response
@app.route("/predict1",methods=['POST'])
def predict1():
    text=request.get_json().get("message")
    
    res= chatbot_response1(text)
    
    message={"answer":res}
    return jsonify(message)

@app.route("/predict2",methods=['POST'])
def predict2():
    text=request.get_json().get("message")
    
    res= chatbot_response2(text)
    
    message={"answer":res}
    return jsonify(message)

if __name__=='__main__':
    app.run(debug=True)