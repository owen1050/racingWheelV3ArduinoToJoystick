void setup() {
  Serial.begin(250000);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);

  pinMode(A8, INPUT);
  pinMode(A9, INPUT);
  pinMode(A10, INPUT);
  pinMode(A11, INPUT);
  
}

void loop() {
  String o = "";
  int a0 = analogRead(A0);
  int a1 = analogRead(A1);
  int a2 = analogRead(A2);
  int a3 = analogRead(A3);

  int i7 = analogRead(A11);
  int i6 = analogRead(A10);
  int i5 = analogRead(A9);
  int i4 = analogRead(A8);
  
  String out0 = "A0:" + String(a0) + "!\t";
  String out1 = "A1:" + String(a1) + "!\t";
  String out2 = "A2:" + String(a2) + "!\t";
  String out3 = "A3:" + String(a3) + "!\t";
  String out7 = "A11:" + String(i7) + "!\t";
  String out6 = "A10:" + String(i6) + "!\t";
  String out5 = "A9:" + String(i5) + "!\t";
  String out4 = "A8:" + String(i4) + "!\t";
  
  String outOut = out0 + out1 + out2 + out3 + out4 + out5 + out6 + out7;
  Serial.println(outOut);
  delay(10);

}
