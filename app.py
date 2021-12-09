from flask import Flask, json, jsonify
import json

app = Flask(__name__)

temp = open('data.json')  
data = json.load(temp)

# home route
@app.route('/')
def welcome():
    return jsonify({"Name":"Arun Bang","Reg No":"19BBS0006"})

    
@app.route('/get_average/<brand_name>/<attribute>')
def return_area(brand_name,attribute):
    car_variants = data[brand_name]
    value1=data[brand_name][attribute]
    print(car_variants)
    print(value1)
    average = 0
    print(car_variants.items())
    for i in car_variants.values():
        average+=i
    average = average / (len(car_variants))
    return jsonify({'Average Price':average})

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)