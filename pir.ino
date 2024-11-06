const int pirPin = 2; 
const int ledPin = 13;

void setup() {
   Serial.begin(9600);
   pinMode(pirPin, INPUT);
   pinMode(ledPin, OUTPUT);
}

void loop() {
  int motionDetected = digitalRead(pirPin);
  if (motionDetected == HIGH) {
    Serial.println("Motion Detected!");
    digitalWrite(ledPin, HIGH); // Turn on the LED
  } else {
    digitalWrite(ledPin, LOW); // Turn off the LED
  }
  delay(100);
}
