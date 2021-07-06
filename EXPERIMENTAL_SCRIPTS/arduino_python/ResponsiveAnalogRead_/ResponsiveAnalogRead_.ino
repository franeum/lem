#include <ResponsiveAnalogRead.h>

// define the pin you want to use
const int ANALOG_PIN = A0;
byte d[] = { 0,0,0 };

// make a ResponsiveAnalogRead object, pass in the pin, and either true or false depending on if you want sleep enabled
// enabling sleep will cause values to take less time to stop changing and potentially stop changing more abruptly,
//   where as disabling sleep will cause values to ease into their correct position smoothly and more accurately
ResponsiveAnalogRead analog(ANALOG_PIN, true);

// the next optional argument is snapMultiplier, which is set to 0.01 by default
// you can pass it a value from 0 to 1 that controls the amount of easing
// increase this to lessen the amount of easing (such as 0.1) and make the responsive values more responsive
// but doing so may cause more noise to seep through if sleep is not enabled

void setup() {
  // begin serial so we can see analog read values through the serial monitor
  Serial.begin(115200);
  analog.setAnalogResolution(1024);
}

void loop() {
  // update the ResponsiveAnalogRead object every loop
  analog.update();
  
  // if the repsonsive value has change, print out 'changed'
  if(analog.hasChanged()) {
    uint32_t value = analog.getValue();
    get_bytes(d, 0, value);
  }
  
  //Serial.println("");
  delay(10);
}

void get_bytes(byte x[], byte label, uint32_t number) {
  number = number >> 1;
  byte dx = (byte)(number & 255);
  byte sx = (byte)((number >> 8) & 255); 
  x[2] = dx;
  x[1] = sx;
  x[0] = label;
  Serial.write(x, 3);
  return 1;
}
