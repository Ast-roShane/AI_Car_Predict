from flask import Flask, redirect, render_template, url_for, request, escape
import pandas as pd
import joblib


app = Flask(__name__)


@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route("/")
def home():
    return render_template("base.html")

@app.route('/about')
def projectwriteup():
    return render_template("project_writeup.html")

@app.route('/alec')
def alec():
    return render_template("resume_alec.html")

@app.route('/roshane')
def roshane():
    return render_template("resume_shane.html")

@app.route('/isaac')
def isaac():
    return render_template("resume_isaac.html")

@app.route('/sean')
def sean():
    return render_template("resume_sean.html")

#-------------------------------------------------------------------------------------#
#--------------------------- ML Model Code -------------------------------------------#
#-------------------------------------------------------------------------------------#


@app.route('/usedCarPredictor')
def usedCarPredictor():
    return render_template("usedCarPredictor.html")

def preprocessDataAndPredict(year, cylinders, odometer, manufacturer, condition, fuel, transmission, drive, vehicle_type, paint_color):
    # create a Data Frame
    data = pd.DataFrame({'Make_year': [year], 'Cylinders': [cylinders], 'Mileage': [odometer], 'Manufacturer': [manufacturer],
                         'Condition': [condition], 'Fuel_type': [fuel], 'Transmission_type': [transmission], 'Drivetrain': [drive],
                         'Vehicle_type': [vehicle_type], 'Paint_color': [paint_color]})

    # open the file
    file = open("final_used_cars_model.pkl", "rb")

    # load trained model
    trained_model = joblib.load(file)

    # prediction
    prediction = trained_model.predict(data)

    return round(prediction[0],)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        # get the data from user
        year = request.form.get('year')
        cylinders = request.form.get('cylinders')
        odometer = request.form.get('odometer')
        manufacturer = request.form.get('manufacturer')
        condition = request.form.get('condition')
        fuel = request.form.get('fuel')
        transmission = request.form.get('transmission')
        drive = request.form.get('drive')
        vehicle_type = request.form.get('vehicle_type')
        paint_color = request.form.get('paint_color')

        # call the preprocessDataAndPredict function and pass the inputs from user
        try:
            prediction = preprocessDataAndPredict(year, cylinders, odometer, manufacturer, condition, fuel, transmission, drive, vehicle_type, paint_color)
            # pass the prediction to the template
            return render_template('predict.html', prediction=prediction)

        except ValueError:
            return "Please Enter Valid Values"

        pass
    pass


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
#change homepage.html to the html file in your templates folder