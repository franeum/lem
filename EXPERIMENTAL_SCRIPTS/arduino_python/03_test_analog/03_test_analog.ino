
#define POT_0 A0 

byte d[] = { 0, 0 };
byte counter = 0;
byte prev;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  d[0] = 0;
}

// the loop function runs over and over again forever
void loop() {
  byte val_pot_0 = (byte)(analogRead(POT_0) >> 3);
    if (val_pot_0 != prev) {
    d[1] = val_pot_0;
    Serial.write(d, 2); 
    //Serial.println(val_pot_0);     
    prev = val_pot_0;  
  } 
  delay(10);     
}
