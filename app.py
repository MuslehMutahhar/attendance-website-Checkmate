
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
        {"Roll Number": "21BD1A1266", "Name": "A BHARATH"},
        {"Roll Number": "21BD1A1267", "Name": "AFSHEEN KAUSAR"},
        {"Roll Number": "21BD1A1268", "Name": "AKUL JAISWAL"},
        {"Roll Number": "21BD1A1269", "Name": "ALLADI BENJAMIN"},
        {"Roll Number": "21BD1A1270", "Name": "BAJJURI OM SWAROOP"},
        {"Roll Number": "21BD1A1271", "Name": "BANJALLU PRASHANTH"},
        {"Roll Number": "21BD1A1272", "Name": "BENDE MEENAKSHI"},
        {"Roll Number": "21BD1A1273", "Name": "KOMMA JAGAN"},
        {"Roll Number": "21BD1A1274", "Name": "BHUKYA NIKHIL"},
        {"Roll Number": "21BD1A1275", "Name": "BINGI AKANKSHA"},
        {"Roll Number": "21BD1A1276", "Name": "BOLLAPALLI ANIL KUMAR"},
        {"Roll Number": "21BD1A1277", "Name": "CH GAURAV"},
        {"Roll Number": "21BD1A1278", "Name": "CH N V VISHWANATHA SAI"},
        {"Roll Number": "21BD1A1279", "Name": "CHILUMULA MANASA"},
        {"Roll Number": "21BD1A1280", "Name": "DASARI SANDEEP"},
        {"Roll Number": "21BD1A1281", "Name": "DASARI SRI RAM"},
        {"Roll Number": "21BD1A1282", "Name": "DAVULURI CHETANA RUPA"},
        {"Roll Number": "21BD1A1283", "Name": "DUDUKA NIKHIL"},
        {"Roll Number": "21BD1A1284", "Name": "GUNDABATTINA SHIVAJI"},
        {"Roll Number": "21BD1A1285", "Name": "HARSHITH PARISA"},
        {"Roll Number": "21BD1A1286", "Name": "JAGATHAP SRIYA"},
        {"Roll Number": "21BD1A1287", "Name": "JAMBOJU ESHWAR"},
        {"Roll Number": "21BD1A1288", "Name": "KALLU PREETHAM PRASAD"},
        {"Roll Number": "21BD1A1289", "Name": "KALMANOOR SRIVATSA"},
        {"Roll Number": "21BD1A1290", "Name": "KAMBLE TANUPRIYA"},
        {"Roll Number": "21BD1A1291", "Name": "KAPARTHI SHRAVANI"},
        {"Roll Number": "21BD1A1292", "Name": "KARLA KEERTHI"},
        {"Roll Number": "21BD1A1293", "Name": "KATAKAM SHREYA"},
        {"Roll Number": "21BD1A1294", "Name": "KATEPALLY DIKSHIT"},
        {"Roll Number": "21BD1A1295", "Name": "KEESARI SUMA REDDY"},
        {"Roll Number": "21BD1A1296", "Name": "KODA ADITYA VARDHAN"},
        {"Roll Number": "21BD1A1297", "Name": "KOLICHELIME GOUTHAM RAJ"},
        {"Roll Number": "21BD1A1298", "Name": "KONDA VANI"},
        {"Roll Number": "21BD1A1299", "Name": "KONDAMADUGU AKSHITHA"},
        {"Roll Number": "21BD1A12A0", "Name": "KONDAMADUGU ANVITHA"},
        {"Roll Number": "21BD1A12A1", "Name": "KONGARI AKHILA"},
        {"Roll Number": "21BD1A12A2", "Name": "KOYA SATHWIK"},
        {"Roll Number": "21BD1A12A3", "Name": "MADISHETTY SRIJAN"},
        {"Roll Number": "21BD1A12A4", "Name": "MAHENDRA SRINIVAS SHREYAS"},
        {"Roll Number": "21BD1A12A5", "Name": "MANIMALA ASHISH RAJ"},
        {"Roll Number": "21BD1A12A6", "Name": "MOHAMMED SAIF UDDIN"},
        {"Roll Number": "21BD1A12A7", "Name": "MOHD MUSLEHUDDIN"},
        {"Roll Number": "21BD1A12A8", "Name": "MUDIMADUGULA SAI MANIKANTA"},
        {"Roll Number": "21BD1A12A9", "Name": "N AISHWARYA"},
        {"Roll Number": "21BD1A12B0", "Name": "NIMMALA BHANU PRASAD"},
        {"Roll Number": "21BD1A12B1", "Name": "NUTHULAKANTI NISHCHAL"},
        {"Roll Number": "21BD1A12B2", "Name": "P BHAVIKA"},
        {"Roll Number": "21BD1A12B3", "Name": "PARVATHAM VAMSHI"},
        {"Roll Number": "21BD1A12B4", "Name": "POTTI NITIN"},
        {"Roll Number": "21BD1A12B5", "Name": "R N LAKSHITH KUMAR"},
        {"Roll Number": "21BD1A12B6", "Name": "RATHLA SANTHOSH"},
        {"Roll Number": "21BD1A12B7", "Name": "RRoll NumberDHI BHATNAGAR"},
        {"Roll Number": "21BD1A12B8", "Name": "SAKETH KASINADHUNI"},
        {"Roll Number": "21BD1A12B9", "Name": "SANJAY SRIVATSAV RAYALA"},
        {"Roll Number": "21BD1A12C0", "Name": "SHAIK MOHAMMAD ASEEL"},
        {"Roll Number": "21BD1A12C1", "Name": "TANKARI ADARSH"},
        {"Roll Number": "21BD1A12C2", "Name": "TATIKONDA SHREYA"},
        {"Roll Number": "21BD1A12C3", "Name": "THOGUTA VENKATESH"},
        {"Roll Number": "21BD1A12C4", "Name": "THUMPALLY SANJANA"},
        {"Roll Number": "21BD1A12C5", "Name": "UPPALA SRIVATSAVA"},
        {"Roll Number": "21BD1A12C6", "Name": "VADDEPELLI VIVEK PREETHAM"},
        {"Roll Number": "21BD1A12C7", "Name": "VADLA SAI TEJA"},
        {"Roll Number": "21BD1A12C8", "Name": "VANAM SPOORTHI"},
        {"Roll Number": "21BD1A12C9", "Name": "VED NITIN PADMAWAR"},
        {"Roll Number": "21BD1A12D0", "Name": "VENKATA HIMAVARSHA"},
        {"Roll Number": "22BD5A1208", "Name": "jagadeesh (specs)"},
        {"Roll Number": "22BD5A1209", "Name": "Mani sai"},
        {"Roll Number": "22BD5A1210", "Name": "Priya sai anshu"},
        {"Roll Number": "22BD5A1211", "Name": "jagadish"},
        {"Roll Number": "22BD5A1212", "Name": "sneha"},
        {"Roll Number": "22BD5A1213", "Name": "umesh"},
        {"Roll Number": "22BD5A1214", "Name": "shanti"}
    ]

    return render_template('index.html', attendance_data=attendance_data)

