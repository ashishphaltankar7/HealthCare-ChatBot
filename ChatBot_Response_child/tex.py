from flask import Flask,render_template,request,jsonify
from ChatBot_Response import chatbot_response

import json
app = Flask(__name__,template_folder='template/')
t=""
@app.route("/")
def index_get():
    return render_template("ChatBot_full_page.html")
@app.route("/predict",methods=['POST'])
def predict():
    text=request.get_json().get("message")
    
    res= chatbot_response(text)
    
    message={"answer":res}
    return jsonify(message)

# @app.route("/pre",methods=['POST'])
# def pre():
#     text=request.get_json().get("message")
    
#     res= chatbot_response(text)
    
#     message={"answer":res}
#     return jsonify(message)
# print(chatbot_response("hi"))

if __name__=='__main__':
    app.run(debug=True)