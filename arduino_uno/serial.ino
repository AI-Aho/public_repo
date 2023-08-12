
int my_array[3] = {1,2,3};
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("My array: ");
  for (int i = 0; i < 3; i++){
    Serial.print("My index: ");
    Serial.print(i);
    Serial.print(" Value: ");
    Serial.println(my_array[i]);
  }
}
void loop() {

}
