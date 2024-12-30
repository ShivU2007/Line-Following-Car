 Step 1: Defining Pins
First I need to define all the Arduino pins that we are going to use. I began by setting up the motor driver pins and the sensor pins.


#define enA 5  
#define in1 6 
#define in2 7  
#define in3 9 
#define in4 10
#define enB 8  
#define R_S 4  
#define L_S 2  

Step 2: Setting Pin Modes 

In the setup I am declaring the modes for each pin. Since the outputs are the IR sensors, those pins are set as inputs. The motor driver pins, which will be controlled by the Arduino, are set as outputs. Lastly the  pins are set to HIGH to activate the motors.


void setup() {
  pinMode(R_S, INPUT);
  pinMode(L_S, INPUT);
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(enB, OUTPUT);
  digitalWrite(enA, HIGH);
  digitalWrite(enB, HIGH);
}


Step 3: Reading Sensors and Controlling Motors
In the loop section, you take the values from the IR sensors and use if statements to control the motor movements based on the 
instructions.  The 4 types of instructions in this code are:


1. Moving Forward:
   If both sensors detect white (output 0), the robot moves forward.

   if ((digitalRead(R_S) == 0) && (digitalRead(L_S) == 0)) {
     forward();
   }
   

2. Turning Right:
   If the right sensor detects black (output 1) and the left sensor detects white (output 0), the robot turns right.

   if ((digitalRead(R_S) == 1) && (digitalRead(L_S) == 0)) {
     turnRight();
   }
   

3. Turning Left:
   If the right sensor detects white (output 0) and the left sensor detects black (output 1), the robot turns left.

   if ((digitalRead(R_S) == 0) && (digitalRead(L_S) == 1)) {
     turnLeft();
   }
 

4. Stopping:
   If both sensors detect black (output 1), the robot stops.

   if ((digitalRead(R_S) == 1) && (digitalRead(L_S) == 1)) {
     Stop();
   }
  


Step 4: Defining Movement Functions
Here are the functions that define the robot's movements:

1. Forward Function:
   This function makes both motors move forward by setting the appropriate pins HIGH and LOW.

 
   void forward() {
     digitalWrite(in1, HIGH);
     digitalWrite(in2, LOW);
     digitalWrite(in3, LOW);
     digitalWrite(in4, HIGH);
   }
   

2. Turn Right Function
   This function makes the robot turn right by reversing the left motor and moving the right motor forward.

   
   void turnRight() {
     digitalWrite(in1, LOW);
     digitalWrite(in2, HIGH);
     digitalWrite(in3, LOW);
     digitalWrite(in4, HIGH);
   }
   

3. Turn Left Function
   This function makes the robot turn left by reversing the right motor and moving the left motor forward.

      void turnLeft() {
     digitalWrite(in1, HIGH);
     digitalWrite(in2, LOW);
     digitalWrite(in3, HIGH);
     digitalWrite(in4, LOW);
   }
   

4. Stop Function:
   This function stops both motors by setting all the motor control pins to LOW.

   
   void Stop() {
     digitalWrite(in1, LOW);
     digitalWrite(in2, LOW);
     digitalWrite(in3, LOW);
     digitalWrite(in4, LOW);
   }
   

 Final Step: Uploading the Code
After writing the code, the last step is to upload it to the Arduino. Connect the Arduino to your computer using a USB cable, and upload the code using the Arduino IDE. Now you are done the code and it will allow your car to become a line following car
