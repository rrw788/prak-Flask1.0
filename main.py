from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def helloword():
    return render_template("home.html")

@app.route("/get_data")
def getdata():
    data = {
        'name': 'Rizky Rifaldi Wahab',
        'url': 'https://github.com/rrw788'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
