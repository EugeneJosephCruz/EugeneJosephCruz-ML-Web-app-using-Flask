from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from pickle import load

#app = Flask(__name__)
app = Flask(__name__, template_folder='./templates')

# Load the model
model = load(open('../models/model.sav','rb'))

@app.route('/')
def home():
    print("Home page accessed")  # Debug print
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print("Predict route accessed")  # Debug print
    try:
        features = [int(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f'Predicted Total Payment: ${output}')
    except Exception as e:
        print("An error occurred: ", e)  # Debug print
        return render_template('index.html', prediction_text='An error occurred.')


if __name__ == "__main__":
    app.run(debug=True)

