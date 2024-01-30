import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, render_template
import joblib
     

app = Flask(__name__)
model = joblib.load(r"C:\Users\paruc\OneDrive\Desktop\Deploy\Fraud_Detection.pkl")
#model = pickle.load(open('Fraud_Detection.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    
    Account_Age_Days = request.form.get('AccountAgeDays')
    num_items = request.form.get('numItems')
    local_time = request.form.get('localTime')
    payment_method = request.form.get('paymentMethod')
    
    if payment_method == 'creditcard':
        numerical_payment_method = 0
    elif payment_method == 'paypal':
        numerical_payment_method = 1
    else:
        numerical_payment_method = 2
    
    payment_method_age_days = request.form.get('MethodAgeDays')
    
    #prediction = model.predict([[Account_Age_Days, num_items, local_time, numerical_payment_method, payment_method_age_days]])
    
    
    
    
    try:
        Account_Age_Days = float(Account_Age_Days)
        num_items = int(num_items)
        local_time = float(local_time)
        numerical_payment_method = int(numerical_payment_method)
        payment_method_age_days = float(payment_method_age_days)

    # Now you can use the numeric values in your prediction
        prediction = model.predict([[Account_Age_Days, num_items, local_time, numerical_payment_method, payment_method_age_days]])

    # Rest of your code...
    except ValueError as e:
    # Handle the case where conversion to numeric types fails
        print(f"Error converting values to numeric types: {e}")
    
    #prediction = model.predict([[request.form.get('AccountAgeDays')]])
    output = prediction[0]
    print(output)
    if output == 0:
        return render_template('index.html', prediction_text = f'Entered data is predicted as {output} so It is not Fraud data')
    else:
        return render_template('index.html', prediction_text = f'Entered data is predicted as {output} so It is Fraud')

if __name__ == '__main__':
    app.run(debug=True)