from flask import Flask, render_template , request
import requests
#pip install requests, pip install flask
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")



@app.route('/city', methods=['POST'])
def weather():
    result = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r_json = result.json()
    time=r_json['time']['updated']
    USD =r_json['bpi']['USD']['code']
    USD_des =r_json['bpi']['USD']['description']
    USD_value =r_json['bpi']['USD']['rate_float']


    return render_template("city.html", time=time, usd = USD , usd_des =USD_des ,  usd_val = USD_value  )
       # return render_template("city.html", city_name=name , data=r_json)



if __name__ =='__main__':
    app.run(debug=True)