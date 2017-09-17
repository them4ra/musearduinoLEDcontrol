/*
  Physical Pixel
 An example of using the Arduino board to receive data from the
 computer.  In this case, the Arduino boards turns on an LED when
 it receives the character 'H', and turns off the LED when it
 receives the character 'L'.
 The data can be sent from the Arduino serial monitor, or another
 program like Processing (see code below), Flash (via a serial-net
 proxy), PD, or Max/MSP.
 The circuit:
 * LED connected from digital pin 13 to ground
 created 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe and Scott Fitzgerald
 This example code is in the public domain.
 http://www.arduino.cc/en/Tutorial/PhysicalPixel
 */

//Setup- connect a LED to pin 11 and 13
const int ledPin = 13; // the pin that the LED is attached to
const int led2Pin = 11; //the pin that the other LED is attached to

int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  pinMode(led2Pin, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital C, turn on the LED:
    if (incomingByte == 'C') {
      Serial.println('C');
      for (int i=0; i < 1; i++){
      //Serial.println("Concentrating ");
      digitalWrite(ledPin, HIGH);
      delay(300);
      digitalWrite(ledPin, LOW);
      delay(300);
      digitalWrite(led2Pin, LOW);
      }
    }
    // this is for mellow
    if (incomingByte == 'M') {
      Serial.println('M');
      for (int i=0; i < 1; i++){
      //Serial.println("Mellow ");
      digitalWrite(led2Pin, HIGH);
      delay(300);
      digitalWrite(led2Pin, LOW);
      delay(300);
      digitalWrite(ledPin, LOW);
      }
    }

  }
}

void serialFlush(){
  while(Serial.available() > 0) {
    incomingByte = Serial.read();
    delay(100000);
  }
}   
