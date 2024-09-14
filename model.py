from flask import Flask, render_template, request, redirect
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict', methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        return brain()
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    try:
        Nitrogen = float(request.form['Nitrogen'])
        Phosphorus = float(request.form['Phosphorus'])
        Potassium = float(request.form['Potassium'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        Ph = float(request.form['ph'])
        Rainfall = float(request.form['Rainfall'])
    except ValueError:
        return "Error: Please enter valid numbers in all fields."

    values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]

    if 0 < Ph <= 14 and Temperature < 100 and Humidity > 0:
        model = joblib.load('cropapp.pkl')
        arr = [values]
        prediction = model.predict(arr)
        return render_template('prediction.html', prediction=str(prediction[0]))
    else:
        return "Error: Invalid values entered. Please check the form and try again."

if __name__ == '__main__':
    app.run(debug=True)