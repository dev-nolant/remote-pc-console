from flask import Flask, request, render_template, Response, redirect
import time
from datetime import datetime
import subprocess
import os

app = Flask(__name__)

now = datetime.now()


@app.route('/')
def my_form():
    return render_template('main.html')


@app.route('/', methods=['POST'])
def index():
    text = request.form['text']
    processed_text = text.lower()

    def inner():
        proc = subprocess.Popen(
            [processed_text],
            shell=True,
            stdout=subprocess.PIPE
        )
        os.system(processed_text)
        for line in iter(proc.stdout.readline, b''):
            time.sleep(.1)

            yield str(line.decode('utf-8')) + '<br/>\n'

    return Response(inner(), mimetype='text/html')


@app.route('/shutdown')
def my_form_shutdown():
    os.system('shutdown /t 300 /s')
    return redirect('/')


@app.route('/logout')
def my_form_logout():
    os.system('shutdown /l')
    return redirect('/')


@app.route('/cshut')
def my_form_cshut():
    os.system('shutdown /a')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6969)
