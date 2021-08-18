import os
import time
import clr # the pythonnet module.
from flask import Flask, render_template, url_for, flash, redirect
#from forms import RegistrationForm, LoginForm
currentPath = os.path.dirname(os.path.abspath(__file__))
print(currentPath)
clr.AddReference(currentPath + "\OpenHardwareMonitorLib.dll")
from OpenHardwareMonitor.Hardware import Computer
from apscheduler.schedulers.background import BackgroundScheduler


c = Computer()
c.CPUEnabled = True  # get the Info about CPU
c.GPUEnabled = True  # get the Info about GPU
c.Open()

sensorToPoll = 0
intervalInSeconds = 0.5


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

for a in range(0, len(c.Hardware[0].Sensors)):
    print(c.Hardware[0].Sensors[a].Identifier)  # use to see sensor identifiers
    if "temperature" in str(c.Hardware[0].Sensors[a].Identifier):
        sensorToPoll = a



posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }


]


@ app.route('/')
@ app.route('/home')
def home():
    return render_template('home.html', posts=posts)




@ app.route('/about')
def about():
    temp = str(c.Hardware[0].Sensors[sensorToPoll].get_Value()) + "C"
    c.Hardware[0].Update()
    time.sleep(intervalInSeconds)
    return render_template('about.html', cpu_temp=temp)



if __name__ == "__main__":
    app.run(debug=True)
