#GET        Used for object retrieval
#POST       Used for object creation and object actions
#PUT        Used for object update
#DELETE     Used for object deletion
import os

# let's import the flask

from flask import Flask,  Response
import json

app = Flask(__name__)

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    student_list = [
        {
            'name':'AR',
            'country':'BD',
            'city':'DHAKA',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'ATIK',
            'country':'BD',
            'city':'DH',
            'skills':['Python','MongoDB']
        },
        {
            'name':'Israt Jahan',
            'country':'DB',
            'city':'Faridpur',
            'skills':['Java','C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)