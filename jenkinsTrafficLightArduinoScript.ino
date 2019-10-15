int incomingByte = 0; // for incoming serial data

void setup() {
  // Green
  pinMode(6, OUTPUT);

  // Yellow
  pinMode(9, OUTPUT);

  // Red
  pinMode(5, OUTPUT);

  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

void loop() {

  if (Serial.available() > 0) {
    incomingByte = Serial.read();
  }
  if (incomingByte == 'b') {
    green();
  }
  else if (incomingByte == 'y') {
    yellow();
  }
  else if (incomingByte == 'r') {
    red();
  }
  else if (incomingByte == "all") {
    all();
  }
//green();
//red();
//yellow();
//all();
}

void green() {
  digitalWrite(6, HIGH);
  digitalWrite(9, LOW);
  digitalWrite(5, LOW);
  delay(500);
}

void yellow() {
  digitalWrite(6, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(5, LOW);
  delay(500);
}

void red() {
  digitalWrite(6, LOW);
  digitalWrite(9, LOW);
  digitalWrite(5, HIGH);
  delay(500);
}

void all() {
  digitalWrite(6, HIGH);
  delay(200);
  digitalWrite(9, HIGH);
  delay(200);
  digitalWrite(5, HIGH);
  delay(200);
  digitalWrite(6, LOW);
  delay(200);
  digitalWrite(9, LOW);
  delay(200);
  digitalWrite(5, LOW);
  delay(300);
}
