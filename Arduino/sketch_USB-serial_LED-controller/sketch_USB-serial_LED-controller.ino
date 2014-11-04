const int ledPin = 12;
unsigned long time = 0;

void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop(){
  if(Serial.available()) {
    String buffer = Serial.readString();
    light(buffer);
  }
  
  if(millis() - time > 5000){
    Serial.println("Connected...");
    time = millis();
  }
}

void light(String s){
  if (s.equals("on") || s.equals("ON")){
    digitalWrite(ledPin, HIGH);
  }
  else if (s.equals("off") || s.equals("OFF")){
    digitalWrite(ledPin, LOW);
  }
  else if (s.equals("status") || s.equals("STATUS")){
    if (digitalRead(ledPin) == HIGH){
      Serial.println("on");
    }
    else if (digitalRead(ledPin) == LOW){
      Serial.println("off");
    }
    else{
      Serial.println("ERROR");
    }
  }
}
    
