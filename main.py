import serial
from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['GET', 'POST'])
def process():
    ard = serial.Serial(port="com17", baudrate=9600)
    time.sleep(1.5)
    on_but_value = request.form.get('ON_But')
    off_but_value = request.form.get('OFF_But')
    if on_but_value == "ON":
        print("ON")
        ard.write(on_but_value.encode('utf-8'))
    elif off_but_value == "OFF":
        print("OFF")
        ard.write(off_but_value.encode('utf-8'))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="192.168.100.112", port=1234, debug=True)
