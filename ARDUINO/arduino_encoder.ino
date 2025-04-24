const int potMaster = A0;
const int pot1 = A1;
const int pot2 = A2;
const int pot3 = A3;
const int pot4 = A4;
const int MaxADC = 1023;

// Master output mapping range
const float MasterMinOutput = -65.0;
const float MasterMaxOutput = 0.0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  float masterValue = MasterConverter(analogRead(potMaster));

  float pot1Value = AppsConverter(analogRead(pot1));
  float pot2Value = AppsConverter(analogRead(pot2));
  float pot3Value = AppsConverter(analogRead(pot3));
  float pot4Value = AppsConverter(analogRead(pot4));

  Serial.print(masterValue);
  Serial.print(":");
  Serial.print(pot1Value);
  Serial.print(":");
  Serial.print(pot2Value);
  Serial.print(":");
  Serial.print(pot3Value);
  Serial.print(":");
  Serial.println(pot4Value);
  
  delay(100);
}

float MasterConverter(float raw){
  float norm = (float)raw / MaxADC;  // Normalize to 0.0 – 1.0

  // Apply curve: higher exponent = faster drop near 1023 | 0.27 is set almost that half pot range sets volume to 50%
  float curved = pow(norm, 0.27);

  // Map to desired output range
  float output = MasterMinOutput + (MasterMaxOutput - MasterMinOutput) * curved; 

  return output;
}

float AppsConverter(float raw){
  float output = raw / MaxADC;  // Normalize to 0.0 – 1.0

  return output;
}