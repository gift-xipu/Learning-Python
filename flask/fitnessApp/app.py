from flask import Flask, render_template, request
from classes.bmr import BMRClass
from classes.bmi import BMIClass
from classes.tdee import TDEEClass

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = 0
    bmr = 0
    if request.method == 'POST':
        gender = request.form['gender']
        age = float(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])

        bmiObj = BMIClass(age, weight, height)
        bmrObj = BMRClass(gender, age, weight, height)

        bmi = bmiObj.calculate()
        bmr = bmrObj.calculate()

        # To add TDEE later:
        # activity_level = float(request.form['activity_level'])
        # tdee = TDEEClass.calculate(bmr, activity_level)

    return render_template('index.html', bmi=bmi, bmr=bmr)

if __name__ == "__main__":
    app.run(debug=True)
