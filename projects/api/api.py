import flask
from flask import request, jsonify
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

batch_4 = [
    {
        'id': 1,
        'roll_no': 1101701004,
        'name': 'Chhean Pisethpanha',
        'sex': 'Male',
        'date_of_birth': '06 April 2000',
        'email': 'chheanpisethpanha17@kit.edu.kh'
    },
    {
        'id': 2,
        'roll_no': 1101701035,
        'name': 'Thepanom Ratanawan',
        'sex': 'Female',
        'date_of_birth': '21 February 1999',
        'email': 'thepanomratanawan17@kit.edu.kh'
    },
    {
        'id': 3,
        'roll_no': 1101701036,
        'name': 'Thon Lynan',
        'sex': 'Female',
        'date_of_birth': '29 December 1999',
        'email': 'thonlynan17@kit.edu.kh'
    }
]

result = []

@app.route("/")
def index():
    return render_template("index.html" , result=result)

def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/batch4/all', methods=['GET'])
def get_all_students():
    return jsonify(batch_4)

@app.route('/batch4', methods=['GET'])
def batch4_name():
    if 'name' in request.args:
        name = request.args['name']
    else:
        return  "Woops! Sorry the name is not in the system yet :P"

    for i in range (0,len(batch_4)):
        if batch_4[i]['name'].lower() == name.lower():
            result.append(batch_4[i])

    return render_template('index.html', result=result)

if __name__ == "__main__":  
    app.run()