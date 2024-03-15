
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def attendance_tracker():
    # Load JSON data
    with open('attendance.json', 'r') as file:
        attendance_data = json.load(file)

    return render_template('index.html', attendance_data=attendance_data)




# if __name__ == '__main__':
#     app.run(host="0.0.0.0",port=5000)
