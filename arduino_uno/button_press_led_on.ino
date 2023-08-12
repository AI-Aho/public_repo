const int pinLed = 13;
const int button = 2;
int button_stage = 0;



void setup() {
pinMode(pinLed, OUTPUT);
pinMode(button, INPUT);


}

void loop() {
button_stage = digitalRead(button);
if (button_stage == HIGH){
  digitalWrite(pinLed, HIGH);

  } else {
    digitalWrite(pinLed, LOW);
  }

}
