#include <MeMCore.h>
MeLineFollower lineFinder(PORT_2);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
MeDCMotor motor1(M1);
MeDCMotor motor2(M2);
MeRGBLed led(0,30);
int speed = 100;
void moveForward(int d) {
    motor1.run(-speed-5);
    motor2.run(speed);
    delay(d);
    motor1.stop();
    motor2.stop();
}
void moveBackward(int d) {
    motor1.run(speed);
    motor2.run(-speed);
    delay(d);
    motor1.stop();
    motor2.stop();
}
void turnLeft(int d) {
    motor1.run(speed);
    motor2.run(speed);
    delay(d);
    motor1.stop();
    motor2.stop();
}
void turnRight(int d) {
    motor1.run(-speed);
    motor2.run(-speed);
    delay(d);
    motor1.stop();
    motor2.stop();
}
void turnAround() {
    motor1.run(-speed);
    motor2.run(-speed);
    delay(1600);
    motor1.stop();
    motor2.stop();
}
int counter = 0;
void loop() {
  while(counter <200) {
    // put your main code here, to run repeatedly:
    if (lineFinder.readSensor1()==0 && lineFinder.readSensor2()==0) {
      Serial.println("Sensor 1 on black and Sensor 2 on black");
      moveForward(50);
    }
    else if (lineFinder.readSensor1()==1 && lineFinder.readSensor2()==0) {
      Serial.println("Sensor 1 on white and Sensor 2 on black");
      if(counter < 50) {
        turnRight(70);
      } else{
        turnRight(25);
      }
    }
    else if (lineFinder.readSensor1()==0 && lineFinder.readSensor2()==1) {
      Serial.println("Sensor 1 on black and Sensor 2 on white");
      turnLeft(50);
    }
    else { //(lineFinder.readSensor1()==1 && lineFinder.readSensor2()==1) 
      Serial.println("Sensor 1 on white and Sensor 2 on white");
      moveBackward(75);
      counter++;
    }
  }
  if(counter >= 200) {
    turnAround();
    counter = 0;
  }
} //hi
