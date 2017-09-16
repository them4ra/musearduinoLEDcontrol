# musearduinoLEDcontrol
Control 2 LED lights with a Muse 2014 headband sending serial commands to an Arduino.

This project uses a Python script to get data from a Muse 2014 headset an then send commands through the serial port to an Arduino that will light up LED lights connected to pins 11 and 13. The LED on pin 11 will light up when the concentration value is above 0.7 and the LED will light up on pin 13 when the mellow value is above 0.7. You can change the threshold values within the Python script. Concentration is commented out to ease getting the whole thing running. Once it works remove the comment dashes to get the other light working as well. 

This project is based upon a project by jnaulty: https://github.com/jnaulty/muse-blink-lights-demo
You'll need to pip install python-osc on a version of Python 3.4+ and the some other libraries you'll find at the beginning of the script. 
You can read through the step by step instructions on jnaulty's project, it'll likely work with this project as well. 
