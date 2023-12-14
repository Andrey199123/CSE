//Andrey Vasilyev
#include <Arduino.h>
#include <MeMCore.h>
MeUltrasonicSensor ultraSonic(PORT_3);
MeDCMotor motor1(M1);
MeDCMotor motor2(M2);
MeRGBLed led(0,30);
int speed = 100;
void moveForward(int d) {
    motor1.run(-speed);
    motor2.run(speed-8 );
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
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("Distance: ");
  Serial.print(ultraSonic.distanceCm());
  Serial.println(" cm");
  moveForward(100);
  if(ultraSonic.distanceCm() < 7) {
    turnLeft(810);
    delay(500);
    if(ultraSonic.distanceCm() < 7) {
      turnRight(1450);
      if(ultraSonic.distanceCm() < 7) {
        turnLeft(810);
        moveBackward(1800);
        turnRight(740);
      }
    }
  }
}//hi
