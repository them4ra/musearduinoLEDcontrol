# Muse to Arduino LED control
Control 2 LED lights with a Muse 2014 headband sending serial commands to an Arduino.

This project uses a Python script to get data from a Muse 2014 headset and then sends commands through the serial port to an Arduino that will light up LED lights connected to pins 11 and 13. The LED on pin 11 will light up when the concentration value is above 0.7 and the LED will light up on pin 13 when the mellow value is above 0.7. You can change the threshold values within the Python script. Concentration is commented out to ease getting the whole thing running. Once it works remove the comment dashes to get the other light working as well. 

This project is based upon a project by jnaulty: https://github.com/jnaulty/muse-blink-lights-demo
You'll need to pip install python-osc on a version of Python 3.4+ and the some other libraries you'll find at the beginning of the script. 
You can read through the step by step instructions on jnaulty's project, it'll likely work with this project as well. 

# What to do 
Get a version of Python up and running, be sure it's 3.4+ so python-osc works the right way. Go and pip install python-osc and some other libraries that you might not have installed.

Upload the Arduino sketch to the board and connect the LED lights with some resistors to the right pins. Connect the Muse headset with Bluetooth to the computer and run Muse-IO to stream to port 5005 and then run the Python script. Make sure the Arduino is already connected via serial connection before running the script or you'll get an error. 

The values you'll be interested in tweeking are:

1) concentration and mellow: these are set to 0.7 and will be the threshold at which the LED lights will light up. Look at the Muse     documentation for more info on the two.

2) concounter and melcounter: these values are there to allow the serial commands to come in at a nice steady pace and not flood into the board. Adjust these to adjust how quickly or slowly the board responds to brain activity. 
