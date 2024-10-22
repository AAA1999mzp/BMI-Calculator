from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    if request.method == 'POST':
        height = float(request.form['height']) / 100  # Convert cm to meters
        weight = float(request.form['weight'])
        bmi = weight / (height * height)
    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
