# define led 2

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0 ){ 
     String input = Serial.readString();
     input.trim();
   
    if (input=="ON"){ 
      Serial.println("The led is on");
      digitalWrite(led, HIGH);
      }
    else if (input=="OFF"){
      Serial.println("The led is off");
      digitalWrite(led, LOW);
    }
    else{
      Serial.println("No such command");
    }
  }
}