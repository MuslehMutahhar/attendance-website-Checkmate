
# from flask import Flask, render_template
# import json

# app = Flask(__name__)

# @app.route('/')
# def attendance_tracker():
#     # Load JSON data
#     with open('attendance.json', 'r') as file:
#         attendance_data = json.load(file)

#     return render_template('index.html', attendance_data=attendance_data)

# if __name__ == '__main__':
#     app.run(host="0.0.0.0",port=5000)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def attendance_tracker():
    # Static attendance data
    attendance_data = [
        {"ID": "21BD1A1266", "Name": "A BHARATH"},
        {"ID": "21BD1A1267", "Name": "AFSHEEN KAUSAR"},
        {"ID": "21BD1A1268", "Name": "AKUL JAISWAL"},
        {"ID": "21BD1A1269", "Name": "ALLADI BENJAMIN"},
        {"ID": "21BD1A1270", "Name": "BAJJURI OM SWAROOP"},
        {"ID": "21BD1A1271", "Name": "BANJALLU PRASHANTH"},
        {"ID": "21BD1A1272", "Name": "BENDE MEENAKSHI"},
        {"ID": "21BD1A1273", "Name": "KOMMA JAGAN"},
        {"ID": "21BD1A1274", "Name": "BHUKYA NIKHIL"},
        {"ID": "21BD1A1275", "Name": "BINGI AKANKSHA"},
        {"ID": "21BD1A1276", "Name": "BOLLAPALLI ANIL KUMAR"},
        {"ID": "21BD1A1277", "Name": "CH GAURAV"},
        {"ID": "21BD1A1278", "Name": "CH N V VISHWANATHA SAI"},
        {"ID": "21BD1A1279", "Name": "CHILUMULA MANASA"},
        {"ID": "21BD1A1280", "Name": "DASARI SANDEEP"},
        {"ID": "21BD1A1281", "Name": "DASARI SRI RAM"},
        {"ID": "21BD1A1282", "Name": "DAVULURI CHETANA RUPA"},
        {"ID": "21BD1A1283", "Name": "DUDUKA NIKHIL"},
        {"ID": "21BD1A1284", "Name": "GUNDABATTINA SHIVAJI"},
        {"ID": "21BD1A1285", "Name": "HARSHITH PARISA"},
        {"ID": "21BD1A1286", "Name": "JAGATHAP SRIYA"},
        {"ID": "21BD1A1287", "Name": "JAMBOJU ESHWAR"},
        {"ID": "21BD1A1288", "Name": "KALLU PREETHAM PRASAD"},
        {"ID": "21BD1A1289", "Name": "KALMANOOR SRIVATSA"},
        {"ID": "21BD1A1290", "Name": "KAMBLE TANUPRIYA"},
        {"ID": "21BD1A1291", "Name": "KAPARTHI SHRAVANI"},
        {"ID": "21BD1A1292", "Name": "KARLA KEERTHI"},
        {"ID": "21BD1A1293", "Name": "KATAKAM SHREYA"},
        {"ID": "21BD1A1294", "Name": "KATEPALLY DIKSHIT"},
        {"ID": "21BD1A1295", "Name": "KEESARI SUMA REDDY"},
        {"ID": "21BD1A1296", "Name": "KODA ADITYA VARDHAN"},
        {"ID": "21BD1A1297", "Name": "KOLICHELIME GOUTHAM RAJ"},
        {"ID": "21BD1A1298", "Name": "KONDA VANI"},
        {"ID": "21BD1A1299", "Name": "KONDAMADUGU AKSHITHA"},
        {"ID": "21BD1A12A0", "Name": "KONDAMADUGU ANVITHA"},
        {"ID": "21BD1A12A1", "Name": "KONGARI AKHILA"},
        {"ID": "21BD1A12A2", "Name": "KOYA SATHWIK"},
        {"ID": "21BD1A12A3", "Name": "MADISHETTY SRIJAN"},
        {"ID": "21BD1A12A4", "Name": "MAHENDRA SRINIVAS SHREYAS"},
        {"ID": "21BD1A12A5", "Name": "MANIMALA ASHISH RAJ"},
        {"ID": "21BD1A12A6", "Name": "MOHAMMED SAIF UDDIN"},
        {"ID": "21BD1A12A7", "Name": "MOHD MUSLEHUDDIN"},
        {"ID": "21BD1A12A8", "Name": "MUDIMADUGULA SAI MANIKANTA"},
        {"ID": "21BD1A12A9", "Name": "N AISHWARYA"},
        {"ID": "21BD1A12B0", "Name": "NIMMALA BHANU PRASAD"},
        {"ID": "21BD1A12B1", "Name": "NUTHULAKANTI NISHCHAL"},
        {"ID": "21BD1A12B2", "Name": "P BHAVIKA"},
        {"ID": "21BD1A12B3", "Name": "PARVATHAM VAMSHI"},
        {"ID": "21BD1A12B4", "Name": "POTTI NITIN"},
        {"ID": "21BD1A12B5", "Name": "R N LAKSHITH KUMAR"},
        {"ID": "21BD1A12B6", "Name": "RATHLA SANTHOSH"},
        {"ID": "21BD1A12B7", "Name": "RIDDHI BHATNAGAR"},
        {"ID": "21BD1A12B8", "Name": "SAKETH KASINADHUNI"},
        {"ID": "21BD1A12B9", "Name": "SANJAY SRIVATSAV RAYALA"},
        {"ID": "21BD1A12C0", "Name": "SHAIK MOHAMMAD ASEEL"},
        {"ID": "21BD1A12C1", "Name": "TANKARI ADARSH"},
        {"ID": "21BD1A12C2", "Name": "TATIKONDA SHREYA"},
        {"ID": "21BD1A12C3", "Name": "THOGUTA VENKATESH"},
        {"ID": "21BD1A12C4", "Name": "THUMPALLY SANJANA"},
        {"ID": "21BD1A12C5", "Name": "UPPALA SRIVATSAVA"},
        {"ID": "21BD1A12C6", "Name": "VADDEPELLI VIVEK PREETHAM"},
        {"ID": "21BD1A12C7", "Name": "VADLA SAI TEJA"},
        {"ID": "21BD1A12C8", "Name": "VANAM SPOORTHI"},
        {"ID": "21BD1A12C9", "Name": "VED NITIN PADMAWAR"},
        {"ID": "21BD1A12D0", "Name": "VENKATA HIMAVARSHA"},
        {"ID": "22BD5A1208", "Name": "jagadeesh (specs)"},
        {"ID": "22BD5A1209", "Name": "Mani sai"},
        {"ID": "22BD5A1210", "Name": "Priya sai anshu"},
        {"ID": "22BD5A1211", "Name": "jagadish"},
        {"ID": "22BD5A1212", "Name": "sneha"},
        {"ID": "22BD5A1213", "Name": "umesh"},
        {"ID": "22BD5A1214", "Name": "shanti"}
    ]

    return render_template('index.html', attendance_data=attendance_data)

