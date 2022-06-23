from flask import Flask,render_template, request 
import pickle
import numpy as np


filename = 'predictionFinal.pkl'
regressor = pickle.load(open(filename, 'rb'))
 
app = Flask(__name__)



# @app.route("/<name>")
# def hello_world(name):
#      return "<p>Hello, World!{}</p>".format(name)

# def Index():
#      return "Hello Flask APP"
@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'ACCENTURE':
            temp_array = temp_array + [1,0]
        elif batting_team == 'ROYAL ENFIELD':
            temp_array = temp_array + [0,1]

        bowling_team = request.form['bowling-team']
        if batting_team == 'ACCENTURE':
            temp_array = temp_array + [1,0]
        elif batting_team == 'ROYAL ENFIELD':
            temp_array = temp_array + [0,1]


        overs = float(request.form['overs'])
        #runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        # runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        # wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
        temp_array = temp_array + [overs, wickets]

        # vector = np.vectorize(np.float)

        
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0][0])
        my_prediction1 = float(regressor.predict(data)[0][1])

              
        # return render_template('predict.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)
        
        return render_template('predict.html',limit = my_prediction , rr = my_prediction1 )


if __name__ == "__main__":
    app.run(debug=True)