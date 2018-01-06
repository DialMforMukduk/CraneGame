
/* 
This is a test sketch for the Adafruit assembled Motor Shield for Arduino v2
It won't work with v1.x motor shields! Only for the v2's with built in PWM
control

For use with the Adafruit Motor Shield v2 
---->	http://www.adafruit.com/products/1438
*/


#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

int steps = 0;
int cranedrop = 0;
int packetEnded = 0;
boolean backward = false;

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMStop = Adafruit_MotorShield(0x60);
Adafruit_MotorShield AFMSbot = Adafruit_MotorShield(0x61);  
// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61); 

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor1 = AFMStop.getStepper(200, 1);
Adafruit_StepperMotor *myMotor2 = AFMSbot.getStepper(200, 1);
Adafruit_StepperMotor *myMotor3 = AFMSbot.getStepper(200, 2);


void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("hi");

  AFMStop.begin();  // create with the default frequency 1.6KHz
  AFMSbot.begin();
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  
  myMotor1->setSpeed(1500);  // 100 rpm 
  myMotor2->setSpeed(1500);  // 100 rpm    
  myMotor3->setSpeed(1500);  // 100 rpm

  
}

void loop() {

  while (Serial.available() > 0) {
    //Read each character, check if negative, end of command or
    //digit, and adjust step value accordingly
    char aChar = Serial.read();
    if (aChar == '-') {
      backward = true;
    }
    else if (aChar == ';') {  //if ; run x axis value
      packetEnded = 1;
    }
    else if (aChar == 'x') {  //if , run y axis value
      packetEnded = 2;
    }
    else if (aChar == 'y') {  //if , run y axis value
      packetEnded = 3;
    }
    else if (aChar == ',') {  //if , run x axis value
      packetEnded = 4;
    }
    else if (aChar == 'z') {  //if , run z axis value
      packetEnded = 5;
    }
    else if (aChar == '/') {  //if , run z axis value
      packetEnded = 6;
    }
    else if (aChar >= '0' && aChar <= '9') {
      steps *= 10;
      steps += aChar - '0';
    }
  }

if (packetEnded == 1) {
      
      myMotor2->step(steps, BACKWARD, DOUBLE); //move x-axis stepper "steps';'" times
      
      Serial.print(steps);
      Serial.println(" Steps Forward");
    
      packetEnded = 0; 
      steps = 0;  //reset loop values to take input
      }

if (packetEnded == 2) {

      myMotor3->step(steps, FORWARD, DOUBLE); //move y-axis stepper "steps','" times
      
      Serial.print(steps);
      Serial.println(" Steps Forward");

      packetEnded = 0;
      steps = 0;
      cranedrop++; //reset loop values for input
      }

if (packetEnded == 3) {
      myMotor2->step(steps, FORWARD, DOUBLE); //return x-axis stepper to original position
      
      packetEnded = 0;
      steps = 0;
      cranedrop++;//reset loop values for input
      }
      
if (packetEnded == 4) {
      myMotor3->step(steps, BACKWARD, DOUBLE); //reset y-axis stepper to original position
      
      packetEnded = 0;
      steps = 0; //reset loop values for input
      }

if (packetEnded == 5) {
      myMotor1->step(steps, BACKWARD, DOUBLE); //reset y-axis stepper to original position
      
      packetEnded = 0;
      steps = 0; //reset loop values for input
      }


if (packetEnded == 6) {
      myMotor1->step(steps, FORWARD, DOUBLE); //reset y-axis stepper to original position
      
      packetEnded = 0;
      steps = 0; //reset loop values for input
      }

if (cranedrop == 2) {
      myMotor1->step(1000, FORWARD, DOUBLE); //reset y-axis stepper to original position
      delay(500);
      myMotor1->step(1000, BACKWARD, DOUBLE);
      
      
      packetEnded = 0;
      steps = 0; //reset loop values for input
      cranedrop = 0;
      }
  
}
