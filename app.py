from flask import Flask, render_template, request, jsonify, make_response, after_this_request, Response
import pandas as pd
import pickle
import datetime
import json
from flask_cors import CORS, cross_origin


model = pickle.load(open('demo.pkl', 'rb'))

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/predict',methods=['GET'])
@cross_origin()
def predict():
#    print(request.form)
    
    predicted_demand = model.predict([[1437173180,2500,7000]])[0]


    response = jsonify({"demand": predicted_demand})
    # response.headers.add("Access-Control-Allow-Origin", 'http://localhost:3000')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
