# coding=utf8
'''
Created on 07.12.2018

@author: zobov
'''
from flask import Flask, render_template, request
import subprocess

PAGE_TITLE = "Управление TrueConf Weathervane"
# application path 
WV_PATH = '"c:\Program Files (x86)\TrueConf\WeatherVane\WeatherVane.exe"'
# html
HTML_FILE = 'preset.html'
# for flask
FLASK_HOST = '192.168.62.149'
FLASK_PORT = 5000
# row count in TrueConf Weathervane
PRESET_COUNT = 12

app = Flask(__name__)

@app.route('/')
def default() -> 'html':
    return render_template(HTML_FILE,
                           the_title=PAGE_TITLE,
                           the_current=-1,
                           the_presets=range(PRESET_COUNT),)


@app.route('/', methods=['POST'])
def set_preset() -> 'html':
    # try to get a preset number
    try:
        preset = int(request.form['submit_button'])
    except:
        preset = -1

    # command line
    if preset >= 0:    
        cmd = WV_PATH + ' -p ' + str(preset)
        print(cmd)
        subprocess.Popen(cmd, shell=True)
        return render_template(HTML_FILE,
                               the_title=PAGE_TITLE,
                               the_current=preset,
                               the_presets=range(PRESET_COUNT),)


if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=True)
