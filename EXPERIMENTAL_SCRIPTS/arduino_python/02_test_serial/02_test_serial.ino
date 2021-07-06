
byte d[] = { 0, 0 };
byte counter = 0;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  d[0] = 1;
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH); 
  count();
  d[1] = counter;
  Serial.write(d, 2);
  delay(200);                      
  
  
  digitalWrite(LED_BUILTIN, LOW);    
  count();
  d[1] = counter;
  Serial.write(d, 2);
  delay(200);                      
}

void count() {
  counter += 1;
  if (counter > 127) counter = 0;
}
