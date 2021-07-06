#include <ResponsiveAnalogRead.h>

const int ANALOG_PIN = A0;
//byte d[] = { 0,0 };

// make a ResponsiveAnalogRead object, pass in the pin, and either true or false depending on if you want sleep enabled
// enabling sleep will cause values to take less time to stop changing and potentially stop changing more abruptly,
//   where as disabling sleep will cause values to ease into their correct position smoothly and more accurately
// ResponsiveAnalogRead analog(ANALOG_PIN, true);
ResponsiveAnalogRead analog_pin(ANALOG_PIN, true);

// the next optional argument is snapMultiplier, which is set to 0.01 by default
// you can pass it a value from 0 to 1 that controls the amount of easing
// increase this to lessen the amount of easing (such as 0.1) and make the responsive values more responsive
// but doing so may cause more noise to seep through if sleep is not enabled

void setup() {
  // begin serial so we can see analog read values through the serial monitor
  Serial.begin(115200);
  //analog_pin = new ResponsiveAnalogRead(ANALOG_PIN, true);
}

void loop() {
  // update the ResponsiveAnalogRead object every loop
  analog_pin.update();

  if (analog_pin.hasChanged()) {
    uint32_t value = analog_pin.getValue();
    //get_bytes(d, value);
    byte val = byte(value >> 2);
    Serial.write(val);
  }
  
  delay(10);
}

void get_bytes(byte x[], uint32_t number) {
  //number = number >> 2;
  //Serial.println((String)number);
  byte val = byte(number >> 2);
  x[0] = 1;
  x[1] = val;
  Serial.print(x[0]);
  Serial.print("\t");
  Serial.println(x[1]);
  /*
  byte dx = (byte)(number & 255);
  byte sx = (byte)((number >> 8) & 15); 
  sx = sx + (label << 4);
  x[1] = dx;
  x[0] = sx;
  Serial.write(x, 2);*/
  /*
  Serial.print(x[0]);
  Serial.print(",");
  Serial.println(x[1]);
  */
  return 1;
}
