# from flask import Flask, render_templete

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return '''

# <h1> Student Score Prediction </h1>


# '''



from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/test')
def test():
    return "<h2>Flask Server Running Successfully!</h2>"


@app.route('/predict', methods=['POST'])
def predict():

    student_id = request.form['student_id']
    hours_studied = float(request.form['hours_studied'])
    previous_score = float(request.form['previous_score'])
    attendance = float(request.form['attendance'])
    sleep_hours = float(request.form['sleep_hours'])
    extracurricular = int(request.form['extracurricular'])
    parent_education = int(request.form['parent_education'])
    internet_access = int(request.form['internet_access'])

    # Simple prediction formula
    predicted_score = (
        previous_score * 0.5 +
        hours_studied * 2 +
        attendance * 0.2 +
        sleep_hours * 1.5 +
        extracurricular * 3 +
        parent_education * 2 +
        internet_access * 2
    )

    predicted_score = min(round(predicted_score, 2), 100)

    return render_template(
        'result.html',
        student_id=student_id,
        score=predicted_score
    )


if __name__ == '__main__':
    app.run(debug=True)