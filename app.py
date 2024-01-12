from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/api/v1/<station>/<date>')
def about(station, date):  # put application's code here
    temperature = 23
    return {
        'station': station,
        'date': date,
        'temperature': temperature
    }


if __name__ == '__main__':
    app.run(debug=True)
