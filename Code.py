#define enA 5  
#define in1 6 
#define in2 7  
#define in3 9 
#define in4 10
#define enB 8  
#define R_S 4
#define L_S 2  

void setup(){
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



   if ((digitalRead(R_S) == 0) && (digitalRead(L_S) == 0)) {
     forward();
   }
   

   if ((digitalRead(R_S) == 1) && (digitalRead(L_S) == 0)) {
     turnRight();
   }
   

   if ((digitalRead(R_S) == 0) && (digitalRead(L_S) == 1)) {
     turnLeft();
   }
 

   if ((digitalRead(R_S) == 1) && (digitalRead(L_S) == 1)) {
     Stop();
   } 
 
   void forward() {
     digitalWrite(in1, HIGH);
     digitalWrite(in2, LOW);
     digitalWrite(in3, LOW);
     digitalWrite(in4, HIGH);
   }
   
   void turnRight() {
     digitalWrite(in1, LOW);
     digitalWrite(in2, HIGH);
     digitalWrite(in3, LOW);
     digitalWrite(in4, HIGH);
   }

      void turnLeft() {
     digitalWrite(in1, HIGH);
     digitalWrite(in2, LOW);
     digitalWrite(in3, HIGH);
     digitalWrite(in4, LOW);
   }
   
   
   void Stop() {
     digitalWrite(in1, LOW);
     digitalWrite(in2, LOW);
     digitalWrite(in3, LOW);
     digitalWrite(in4, LOW);
   }
