const int pinLed = 13;
const int pinLed2 = 12;
const int button = 2;
int button_stage = 0;



void setup() {
pinMode(pinLed, OUTPUT);
pinMode(pinLed2, OUTPUT);
pinMode(button, INPUT);


}

void loop() {
button_stage = digitalRead(button);
if (button_stage == HIGH){
  digitalWrite(pinLed, HIGH);
  digitalWrite(pinLed2, LOW);

  } else {
    digitalWrite(pinLed, LOW);
    digitalWrite(pinLed2, HIGH);
  }

}
