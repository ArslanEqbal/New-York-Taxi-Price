# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 01:10:06 2020

@author: AASHU
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
#from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model_rfr.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        passenger_count = int(request.form['passenger_count'])
        distance =float(request.form['distance'])
        
        prediction=model.predict([[passenger_count , distance]])
        output=round(prediction[0],2)
        
            
        return render_template('index.html',prediction_text="Net Charge  {} $".format(output))
    

if __name__=="__main__":
    app.run(debug=True)
