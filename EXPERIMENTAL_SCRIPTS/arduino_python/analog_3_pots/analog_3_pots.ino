#include <ResponsiveAnalogRead.h>

const int SIZE = 3;
const int ANALOG_PIN[] = { A0, A1, A2 };
byte d[] = { 0,0,0 };

// make a ResponsiveAnalogRead object, pass in the pin, and either true or false depending on if you want sleep enabled
// enabling sleep will cause values to take less time to stop changing and potentially stop changing more abruptly,
//   where as disabling sleep will cause values to ease into their correct position smoothly and more accurately
// ResponsiveAnalogRead analog(ANALOG_PIN, true);
ResponsiveAnalogRead *analog_reads[SIZE];

// the next optional argument is snapMultiplier, which is set to 0.01 by default
// you can pass it a value from 0 to 1 that controls the amount of easing
// increase this to lessen the amount of easing (such as 0.1) and make the responsive values more responsive
// but doing so may cause more noise to seep through if sleep is not enabled

void setup() {
  // begin serial so we can see analog read values through the serial monitor
  Serial.begin(115200);
  //analog.setAnalogResolution(1024);
  for (int i=0; i<SIZE; i++) {
    analog_reads[i] = new ResponsiveAnalogRead(ANALOG_PIN[i], true);
  }
}

void loop() {
  // update the ResponsiveAnalogRead object every loop
  for (int i=0; i<SIZE; i++) {
    analog_reads[i]->update();
  
    // if the repsonsive value has change, print out 'changed'
    if(analog_reads[i]->hasChanged()) {
      uint32_t value = analog_reads[i]->getValue();
      get_bytes(d, (byte)i, value);
    }
  }
  
  delay(10);
}

void get_bytes(byte x[], byte label, uint32_t number) {
  number = number >> 2;
  //Serial.println((String)number);
  byte dx = (byte)(number & 255);
  byte sx = (byte)((number >> 8) & 255); 
  //sx = sx + (label << 4);
  x[2] = dx;
  x[1] = sx;
  x[0] = label;
  Serial.write(x, 3);
  /*
  Serial.print(x[0]);
  Serial.print(",");
  Serial.println(x[1]);
  */
  return 1;
}
