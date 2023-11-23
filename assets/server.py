from flask import Flask, jsonify,render_template, request 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import pandas as pd
from tensorflow import keras
import numpy as np
app = Flask(__name__,template_folder="templates", static_url_path='/static') 
model = keras.models.load_model('assets/saved_model/')

@app.route("/") 
def hello(): 
    return render_template('index.html') 
  
@app.route('/process', methods=['POST']) 
def process(): 
    data = request.get_json() # retrieve the data sent from JavaScript 
    # process the data using Python code 
    X = data['value']
    X = np.array(pd.Series(X).map(lambda x: list(map(int, x))).to_list()).reshape(-1,9,9,1)
    X = X/9
    X -= 0.5
    for i in range(5):
        y = model.predict(X).argmax(-1)+1
    ans = y[0]
    res = ''
    for i in ans:
        res += "".join(str(x) for x in i)
    return jsonify(result=res) # return the result to JavaScript 
  
if __name__ == '__main__': 
    app.run(debug=True) 
